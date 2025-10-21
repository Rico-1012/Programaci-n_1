 #!/usr/bin/env python3
from datetime import datetime, time
import uuid
from collections import defaultdict, Counter

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass

class PlatoNoEncontrado(ErrorRestaurante):
    def __init__(self, codigo_plato):
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")

class MesaNoDisponible(ErrorRestaurante):
    def __init__(self, numero_mesa, hora_disponible=None):
        msg = f"Mesa {numero_mesa} ocupada."
        if hora_disponible: msg += f" Disponible a las {hora_disponible.strftime('%H:%M')}"
        super().__init__(msg)

class CapacidadExcedida(ErrorRestaurante):
    def __init__(self, numero_mesa, capacidad, comensales):
        super().__init__(f"Mesa {numero_mesa} (Capacidad: {capacidad}) no puede albergar {comensales} comensales.")

class PedidoInvalido(ErrorRestaurante):
    def __init__(self, razon):
        super().__init__(f"Pedido inválido: {razon}")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""
    
    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        self.num_mesas = num_mesas
        self.tasa_impuesto = tasa_impuesto
        self.propina_sugerida = propina_sugerida
        self.menu = {} 
        self.mesas = {i: {'capacidad': 2, 'ocupada_hasta': None, 'comensales': 0, 'id_pedido_actual': None} for i in range(1, num_mesas + 1)}
        self.pedidos = {}
        self.historial_ventas = {}
    
    
    
    def agregar_plato(self, codigo, nombre, categoria, precio):
        if not all([codigo, nombre, categoria]) or precio <= 0:
            raise ValueError("Datos de plato inválidos.")
        if codigo in self.menu:
            raise KeyError(f"El código '{codigo}' ya existe.")
        self.menu[codigo] = {'nombre': nombre, 'categoria': categoria, 'precio': round(float(precio), 2), 'disponible': True}
    
    def cambiar_disponibilidad(self, codigo, disponible):
        if codigo not in self.menu: raise PlatoNoEncontrado(codigo)
        self.menu[codigo]['disponible'] = disponible
    
    def buscar_platos(self, categoria=None, precio_max=None):
        resultados = []
        for codigo, plato in self.menu.items():
            if not plato['disponible']: continue
            cumple_cat = (categoria is None) or (plato['categoria'].lower() == categoria.lower())
            cumple_precio = (precio_max is None) or (plato['precio'] <= precio_max)
            if cumple_cat and cumple_precio:
                plato_info = plato.copy()
                plato_info['codigo'] = codigo
                resultados.append(plato_info)
        return resultados
    
        
    
    def configurar_mesa(self, numero, capacidad):
        if numero not in self.mesas or capacidad <= 0:
            raise ValueError("Número de mesa o capacidad inválida.")
        self.mesas[numero]['capacidad'] = capacidad
    
    def reservar_mesa(self, numero, comensales, hora):
        if numero not in self.mesas or comensales <= 0:
            raise ValueError("Datos de reserva inválidos.")
        mesa = self.mesas[numero]
        if comensales > mesa['capacidad']:
            raise CapacidadExcedida(numero, mesa['capacidad'], comensales)
        if mesa['id_pedido_actual'] is not None:
            raise MesaNoDisponible(numero)
            
        self.mesas[numero].update({'comensales': comensales, 'ocupada_hasta': None})
        return f"Mesa {numero} asignada."
    
    def liberar_mesa(self, numero):
        if numero not in self.mesas: raise ValueError(f"Mesa {numero} no existe.")
        mesa = self.mesas[numero]
        if mesa['id_pedido_actual'] is None: raise ValueError(f"Mesa {numero} no está ocupada.")
            
        pedido_id = mesa['id_pedido_actual']
        if not self.pedidos.get(pedido_id, {}).get('pagado', False):
             raise PedidoInvalido(f"El pedido ID {pedido_id} debe ser pagado antes.")
            
        self.mesas[numero].update({'comensales': 0, 'ocupada_hasta': datetime.now(), 'id_pedido_actual': None})
    
    def mesas_disponibles(self, comensales):
        return [num for num, mesa in self.mesas.items() 
                if mesa['id_pedido_actual'] is None and mesa['capacidad'] >= comensales]
    
        
    
    def crear_pedido(self, numero_mesa):
        if numero_mesa not in self.mesas or self.mesas[numero_mesa]['comensales'] == 0:
            raise ValueError(f"Mesa {numero_mesa} no asignada o sin comensales.")
        if self.mesas[numero_mesa]['id_pedido_actual'] is not None:
            raise PedidoInvalido(f"Mesa {numero_mesa} ya tiene un pedido activo.")
            
        id_pedido = str(uuid.uuid4())
        self.pedidos[id_pedido] = {'mesa': numero_mesa, 'items': {}, 'pagado': False, 'hora_creacion': datetime.now()}
        self.mesas[numero_mesa]['id_pedido_actual'] = id_pedido
        return id_pedido
    
    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        if id_pedido not in self.pedidos or self.pedidos[id_pedido]['pagado']:
            raise PedidoInvalido(f"Pedido '{id_pedido}' inválido o pagado.")
        if codigo_plato not in self.menu: raise PlatoNoEncontrado(codigo_plato)
        if not self.menu[codigo_plato]['disponible']: raise ValueError(f"Plato '{codigo_plato}' no disponible.")
        if cantidad <= 0: raise ValueError("Cantidad inválida.")
            
        items = self.pedidos[id_pedido]['items']
        items[codigo_plato] = items.get(codigo_plato, 0) + cantidad
        self._recalcular_totales_pedido(id_pedido)
    
    def _recalcular_totales_pedido(self, id_pedido, propina_porcentaje=None):
        pedido = self.pedidos[id_pedido]
        subtotal = sum(self.menu.get(c, {}).get('precio', 0.0) * cant 
                       for c, cant in pedido['items'].items())
        
        propina_rate = propina_porcentaje if propina_porcentaje is not None else self.propina_sugerida
        
        subtotal = round(subtotal, 2)
        impuesto = round(subtotal * self.tasa_impuesto, 2)
        propina = round(subtotal * propina_rate, 2)
        total = round(subtotal + impuesto + propina, 2)
        
        pedido.update({'subtotal': subtotal, 'impuesto': impuesto, 'propina': propina, 'total': total})
        return {'subtotal': subtotal, 'impuesto': impuesto, 'propina': propina, 'total': total}

    def calcular_total(self, id_pedido, propina_porcentaje=None):
        if id_pedido not in self.pedidos: raise PedidoInvalido(f"Pedido '{id_pedido}' no encontrado.")
        return self._recalcular_totales_pedido(id_pedido, propina_porcentaje)
    
    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        if id_pedido not in self.pedidos: raise PedidoInvalido(f"Pedido '{id_pedido}' no encontrado.")
        pedido = self.pedidos[id_pedido]
        if pedido['pagado']: raise PedidoInvalido(f"Pedido '{id_pedido}' ya fue pagado.")
             
        totales = self._recalcular_totales_pedido(id_pedido, propina_porcentaje)
        
        pedido['pagado'] = True
        self.historial_ventas[id_pedido] = pedido.copy()
        return totales
    
            
                
    def platos_mas_vendidos(self, n=5):
        contador = Counter()
        for pedido in self.historial_ventas.values():
            contador.update(pedido['items'])
                
        return [(codigo, self.menu.get(codigo, {}).get('nombre', 'DESCONOCIDO'), cantidad) 
                for codigo, cantidad in contador.most_common(n)]
    
    def ventas_por_categoria(self):
        ventas = defaultdict(float)
        for pedido in self.historial_ventas.values():
            for codigo, cantidad in pedido['items'].items():
                plato_info = self.menu.get(codigo)
                if plato_info:
                    ventas[plato_info['categoria']] += plato_info['precio'] * cantidad
        return {k: round(v, 2) for k, v in ventas.items()}
    
    def reporte_ventas_dia(self):
        total_sub, total_imp, total_prop, total_ventas = 0.0, 0.0, 0.0, 0.0
        for p in self.historial_ventas.values():
            total_sub += p.get('subtotal', 0)
            total_imp += p.get('impuesto', 0)
            total_prop += p.get('propina', 0)
            total_ventas += p.get('total', 0)
            
        return {
            'total_pedidos_pagados': len(self.historial_ventas),
            'resumen_financiero': {'subtotal_acumulado': round(total_sub, 2), 'impuesto_acumulado': round(total_imp, 2),
                                   'propina_acumulada': round(total_prop, 2), 'total_general': round(total_ventas, 2)},
            'ventas_por_categoria': self.ventas_por_categoria(),
            'platos_top_5': self.platos_mas_vendidos(n=5)
        }
    
    def estado_restaurante(self):
        mesas_ocupadas = sum(1 for m in self.mesas.values() if m['id_pedido_actual'] is not None)
        mesas_estado = [{'numero': num, 'capacidad': info['capacidad'], 
                         'estado': 'Ocupada' if info['id_pedido_actual'] else 'Disponible',
                         'comensales': info['comensales'], 'pedido_actual': info['id_pedido_actual']}
                        for num, info in self.mesas.items()]
            
        return {'total_mesas': self.num_mesas, 'mesas_ocupadas': mesas_ocupadas,
                'mesas_disponibles': self.num_mesas - mesas_ocupadas,
                'pedidos_activos': len(self.pedidos) - len(self.historial_ventas), 
                'detalle_mesas': mesas_estado}
    
    
    
    def exportar_menu(self, archivo='menu.txt'):
        try:
            with open(archivo, 'w') as f:
                for c, p in self.menu.items():
                    f.write(f"{c}|{p['nombre']}|{p['categoria']}|{p['precio']}|{p['disponible']}\n")
            return True
        except IOError: return False
    
    def importar_menu(self, archivo='menu.txt'):
        resultados = {'exitosos': 0, 'errores': []}
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    try:
                        codigo, nombre, categoria, precio_str, disponible_str = linea.strip().split('|')
                        self.agregar_plato(codigo, nombre, categoria, float(precio_str))
                        self.menu[codigo]['disponible'] = disponible_str.lower() == 'true'
                        resultados['exitosos'] += 1
                    except Exception as e:
                        resultados['errores'].append(f"Error en línea '{linea.strip()}': {e}")
        except FileNotFoundError:
            resultados['errores'].append(f"Archivo '{archivo}' no encontrado.")
        except IOError as e:
            resultados['errores'].append(f"Error al leer el archivo {archivo}: {e}")
        return resultados

# ===========================================================================
# EJEMPLO DE USO (Mismo ejemplo de prueba para validar)
# ===========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE (Resumen)")
    print("=" * 70)
    
    restaurante = SistemaRestaurante(num_mesas=3, tasa_impuesto=0.10)
    
    print("\n## Configuración Inicial ##")
    restaurante.configurar_mesa(1, 4)
    restaurante.configurar_mesa(2, 2)
    restaurante.configurar_mesa(3, 8)
    print(f"Mesas configuradas: {restaurante.mesas}")

    print("\n## Gestión de Menú ##")
    restaurante.agregar_plato('A1', 'Sopa de Tomate', 'Entrada', 45.00)
    restaurante.agregar_plato('P1', 'Pasta Carbonara', 'Principal', 150.00)
    restaurante.agregar_plato('P2', 'Rib Eye', 'Principal', 300.00)
    restaurante.agregar_plato('D1', 'Tiramisu', 'Postre', 80.00)
    restaurante.cambiar_disponibilidad('A1', False)
    print("Platos disponibles (max $160):", [p['nombre'] for p in restaurante.buscar_platos(precio_max=160)]) 

    print("\n## Gestión de Mesas y Pedidos ##")
    

    try:
        restaurante.reservar_mesa(1, 3, time(18, 0))
        id_pedido_1 = restaurante.crear_pedido(1)
        restaurante.agregar_item(id_pedido_1, 'P1', 2)
        restaurante.agregar_item(id_pedido_1, 'D1', 1)
        print(f"Pedido ID {id_pedido_1} creado para Mesa 1.")
    except Exception as e: print(f"ERROR: {e}")
        
   
    try:
        restaurante.reservar_mesa(3, 10, time(19, 0))
    except CapacidadExcedida as e: print(f"ERROR al reservar: {e.args[0]}")
        
    try:
        restaurante.reservar_mesa(3, 5, time(19, 0))
        id_pedido_3 = restaurante.crear_pedido(3)
        restaurante.agregar_item(id_pedido_3, 'P2', 3)
        print(f"Pedido ID {id_pedido_3} creado para Mesa 3.")
    except Exception as e: print(f"ERROR: {e}")

    print("\nMesas disponibles para 2 comensales:", restaurante.mesas_disponibles(2))

    
    print(f"\n## Facturación Pedido 1 ({id_pedido_1}) ##")
    totales_1 = restaurante.pagar_pedido(id_pedido_1, propina_porcentaje=0.20)
    print(f"Pedido 1 PAGADO. Total (20% propina): {totales_1['total']:.2f}")
    restaurante.liberar_mesa(1)
    print("Mesa 1 liberada.")

  
    print(f"\n## Facturación Pedido 3 ({id_pedido_3}) ##")
    totales_3 = restaurante.pagar_pedido(id_pedido_3)
    print(f"Pedido 3 PAGADO. Total: {totales_3['total']:.2f}")
    restaurante.liberar_mesa(3)
    print("Mesa 3 liberada.")

    print("\n## Reportes ##")
    print("\nEstado actual del restaurante:")
    print(restaurante.estado_restaurante())
    print("\nPlatos más vendidos (Top 1):", restaurante.platos_mas_vendidos(n=1))
    print("\nReporte de Ventas del Día:")
    print(restaurante.reporte_ventas_dia())
