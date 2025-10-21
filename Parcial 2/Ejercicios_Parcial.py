#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: [Tu Nombre]
Fecha: [Fecha de Hoy]
"""
import math
import string
from collections import Counter
import copy

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones matemáticas con validación.
    
    Args:
        operacion: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
        a: Primer número (int o float)
        b: Segundo número (int o float)
    
    Returns:
        float: Resultado con 2 decimales de precisión
    
    Raises:
        ValueError: Si la operación es inválida o tipos incorrectos
        ZeroDivisionError: Si intenta dividir por cero
    """
    # 1. Validación de tipos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos 'a' y 'b' deben ser números (int o float).")
    
    # 2. Validación de operación y cálculo
    operacion = operacion.lower()
    
    if operacion == "suma":
        resultado = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiplicacion":
        resultado = a * b
    elif operacion == "division":
        # Manejo de ZeroDivisionError
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        resultado = a / b
    elif operacion == "potencia":
        resultado = a ** b
    elif operacion == "modulo":
        # Manejo de ZeroDivisionError para módulo
        if b == 0:
            raise ZeroDivisionError("No se puede calcular el módulo con divisor cero.")
        resultado = a % b
    else:
        # Manejo de operación inválida
        raise ValueError(f"Operación inválida: {operacion}. Operaciones permitidas: suma, resta, multiplicacion, division, potencia, modulo.")
        
    # 3. Retornar resultado con 2 decimales
    return round(resultado, 2)


# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    """Validador de contraseñas con reglas configurables."""
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        """
        Inicializa el validador con reglas específicas.
        """
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        self.caracteres_especiales = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        """
        errores = []
        es_valido = True

        # 1. Longitud
        if len(password) < self.min_longitud:
            errores.append(f"Debe tener al menos {self.min_longitud} caracteres (tiene {len(password)}).")
            es_valido = False

        # 2. Mayúscula
        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Debe contener al menos una mayúscula.")
            es_valido = False

        # 3. Minúscula
        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Debe contener al menos una minúscula.")
            es_valido = False

        # 4. Número
        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Debe contener al menos un número.")
            es_valido = False

        # 5. Carácter especial
        if self.requiere_especial and not any(c in self.caracteres_especiales for c in password):
            errores.append("Debe contener al menos un carácter especial.")
            es_valido = False

        return es_valido, errores
    
    def es_fuerte(self, password):
        """
        Determina si el password es fuerte.
        Un password fuerte tiene al menos 12 caracteres,
        mayúsculas, minúsculas, números y caracteres especiales.
        """
        # Reglas para 'fuerte': 
        # min_longitud=12, requiere_mayuscula=True, requiere_minuscula=True, 
        # requiere_numero=True, requiere_especial=True.
        
        largo_ok = len(password) >= 12
        tiene_mayuscula = any(c.isupper() for c in password)
        tiene_minuscula = any(c.islower() for c in password)
        tiene_numero = any(c.isdigit() for c in password)
        tiene_especial = any(c in self.caracteres_especiales for c in password)
        
        # Expresión lógica y relacional para determinar si es fuerte
        return largo_ok and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario.
        Estructura: {codigo: {'nombre': str, 'precio': float, 'cantidad': int, 'categoria': str}}
        """
        self.inventario = {} # Diccionario principal
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un producto al inventario.
        
        Raises:
            ValueError: Si el código ya existe, o si precio/cantidad son inválidos
        """
        if codigo in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' ya existe.")
        
        if not (isinstance(precio, (int, float)) and precio >= 0):
             raise ValueError("El precio debe ser un número no negativo.")
        if not (isinstance(cantidad, int) and cantidad >= 0):
             raise ValueError("La cantidad debe ser un entero no negativo.")

        self.inventario[codigo] = {
            'nombre': nombre,
            'precio': round(float(precio), 2),
            'cantidad': int(cantidad),
            'categoria': categoria
        }
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        
        Args:
            cantidad_cambio: Positivo para añadir, negativo para reducir
        
        Raises:
            ValueError: Si producto no existe o stock resultante sería negativo
        """
        if codigo not in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' no existe.")
        
        if not isinstance(cantidad_cambio, int):
             raise ValueError("La cantidad de cambio debe ser un entero.")
             
        nuevo_stock = self.inventario[codigo]['cantidad'] + cantidad_cambio
        
        if nuevo_stock < 0:
            raise ValueError(f"El stock resultante ({nuevo_stock}) no puede ser negativo.")
            
        self.inventario[codigo]['cantidad'] = nuevo_stock
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Returns:
            list: Lista de tuplas (codigo, nombre, precio)
        """
        productos_categoria = []
        for codigo, datos in self.inventario.items():
            if datos['categoria'].lower() == categoria.lower():
                productos_categoria.append((codigo, datos['nombre'], datos['precio']))
        
        return productos_categoria
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite.
        
        Returns:
            dict: {codigo: cantidad} de productos bajo el límite
        """
        productos_bajos = {}
        for codigo, datos in self.inventario.items():
            if datos['cantidad'] < limite:
                productos_bajos[codigo] = datos['cantidad']
        
        return productos_bajos
    
    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de (precio * cantidad) de todos los productos
        """
        valor_total = 0.0
        for datos in self.inventario.values():
            valor_total += datos['precio'] * datos['cantidad']
            
        return round(valor_total, 2)
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        
        Returns:
            list: Lista de tuplas (codigo, valor_total) ordenadas descendentemente
        """
        valores_productos = []
        for codigo, datos in self.inventario.items():
            valor_total_producto = round(datos['precio'] * datos['cantidad'], 2)
            valores_productos.append((codigo, valor_total_producto))
            
        # Ordenar descendentemente por el valor total (elemento en índice 1)
        valores_productos.sort(key=lambda x: x[1], reverse=True)
        
        # Retornar los N primeros
        return valores_productos[:n]


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si divisible por 100: no bisiesto
    - EXCEPTO si divisible por 400: bisiesto
    
    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    # Usando la lógica anidada
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
    
    # Alternativa compacta: return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    
    Args:
        mes: Número del mes (1-12)
        anio: Año (considera bisiestos)
    
    Returns:
        int: Número de días en el mes
    
    Raises:
        ValueError: Si mes es inválido (no está entre 1 y 12)
    """
    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
        
    # Meses con 31 días
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    # Meses con 30 días
    elif mes in (4, 6, 9, 11):
        return 30
    # Febrero (mes 2)
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    
    # Esto no debería ejecutarse si la validación 1-12 es correcta
    return 0 

def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    
    Args:
        mes: Mes (1-12)
        anio: Año
        dia_inicio: Día de la semana del primer día (0=Lunes, 6=Domingo).
                    Nota: La función asume que el día 1 del mes *cae* en este día.
                    En un sistema real, se usaría un módulo de fecha para calcularlo.
    
    Returns:
        str: Calendario formateado
    """
    try:
        num_dias = dias_en_mes(mes, anio)
    except ValueError as e:
        return f"Error: {e}"

    # Encabezado del calendario
    encabezado = "Lu Ma Mi Ju Vi Sa Do\n"
    
    # 1. Rellenar espacios iniciales (padding)
    # Se usa 3 caracteres de ancho por día ('Lu ', 'Ma ', etc.)
    calendario_str = "   " * dia_inicio
    
    # 2. Agregar los días
    dia_actual = 1
    dia_semana_actual = dia_inicio
    
    while dia_actual <= num_dias:
        # Añadir el número de día, alineado a la derecha con 2 espacios, seguido de un espacio
        calendario_str += f"{dia_actual:2d} "
        
        dia_semana_actual += 1
        
        # Si es Domingo (índice 7, que es 0) o el último día del mes, añadir salto de línea
        if dia_semana_actual % 7 == 0:
            calendario_str += "\n"
            dia_semana_actual = 0 # Reiniciar el conteo del día de la semana
            
        dia_actual += 1
        
    return encabezado + calendario_str.strip()


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas.
    """
    if not ventas:
        return {
            'total_ventas': 0.0,
            'promedio_por_venta': 0.0,
            'producto_mas_vendido': None,
            'venta_mayor': None,
            'total_descuentos': 0.0
        }

    total_ventas = 0.0
    total_descuentos = 0.0
    cantidad_vendida_por_producto = Counter()
    venta_mayor_monto = -1.0
    venta_mayor = None

    for venta in ventas:
        # Calcular el valor de la venta
        monto_bruto = venta['cantidad'] * venta['precio']
        monto_descuento = monto_bruto * (venta.get('descuento', 0) / 100.0)
        monto_neto = monto_bruto - monto_descuento
        
        total_ventas += monto_neto
        total_descuentos += monto_descuento
        
        # Actualizar producto más vendido (por cantidad de unidades)
        cantidad_vendida_por_producto[venta['producto']] += venta['cantidad']
        
        # Actualizar venta de mayor monto (por el monto neto)
        if monto_neto > venta_mayor_monto:
            venta_mayor_monto = monto_neto
            # Usar deepcopy para guardar una copia de la venta original si fuera necesario
            # o simplemente añadir el monto_neto si solo se pide el dict original
            venta_mayor = {
                'producto': venta['producto'],
                'cantidad': venta['cantidad'],
                'precio': venta['precio'],
                'descuento': venta.get('descuento', 0),
                'monto_neto': round(monto_neto, 2)
            }
            
    # Calcular promedio
    promedio_por_venta = total_ventas / len(ventas)
    
    # Encontrar el producto más vendido
    producto_mas_vendido = cantidad_vendida_por_producto.most_common(1)[0][0] if cantidad_vendida_por_producto else None

    return {
        'total_ventas': round(total_ventas, 2),
        'promedio_por_venta': round(promedio_por_venta, 2),
        'producto_mas_vendido': producto_mas_vendido,
        'venta_mayor': venta_mayor,
        'total_descuentos': round(total_descuentos, 2)
    }

def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    """
    if len(numeros) < 2:
        return {
            'secuencias_ascendentes': 0,
            'secuencias_descendentes': 0,
            'longitud_max_ascendente': len(numeros),
            'longitud_max_descendente': len(numeros),
            'numeros_repetidos': Counter(numeros) if numeros else {}
        }
        
    num_ascendentes = 0
    num_descendentes = 0
    max_ascendente = 1
    max_descendente = 1
    
    longitud_actual_ascendente = 1
    longitud_actual_descendente = 1

    for i in range(1, len(numeros)):
        anterior = numeros[i-1]
        actual = numeros[i]
        
        # 1. Secuencias Ascendentes
        if actual > anterior:
            longitud_actual_ascendente += 1
            longitud_actual_descendente = 1 # Rompe secuencia descendente
            
            if longitud_actual_ascendente == 2: # Primer incremento, inicia una secuencia
                num_ascendentes += 1
                
        # 2. Secuencias Descendentes
        elif actual < anterior:
            longitud_actual_descendente += 1
            longitud_actual_ascendente = 1 # Rompe secuencia ascendente

            if longitud_actual_descendente == 2: # Primer decremento, inicia una secuencia
                num_descendentes += 1
                
        # 3. Igualdad (Rompe ambas secuencias)
        else:
            longitud_actual_ascendente = 1
            longitud_actual_descendente = 1
            
        # 4. Actualizar máximos
        max_ascendente = max(max_ascendente, longitud_actual_ascendente)
        max_descendente = max(max_descendente, longitud_actual_descendente)

    # 5. Conteo de repeticiones
    numeros_repetidos = {num: count for num, count in Counter(numeros).items() if count > 1}
    
    return {
        'secuencias_ascendentes': num_ascendentes,
        'secuencias_descendentes': num_descendentes,
        'longitud_max_ascendente': max_ascendente,
        'longitud_max_descendente': max_descendente,
        'numeros_repetidos': numeros_repetidos
    }

def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    """
    historial = []
    balance_actual = principal
    
    # Validaciones básicas
    if anios <= 0:
        return []
    if tasa_anual < 0 or principal < 0 or aporte_anual < 0:
        # Se podría elevar un ValueError, pero para la simulación, se asume valores válidos
        pass 
        
    for anio in range(1, anios + 1):
        # 1. Agregar aporte anual al inicio del año
        balance_inicio_anio = balance_actual + aporte_anual
        
        # 2. Calcular interés ganado (sobre el balance al inicio del año)
        interes_ganado = balance_inicio_anio * tasa_anual
        
        # 3. Calcular balance al final del año
        balance_final_anio = balance_inicio_anio + interes_ganado
        
        # 4. Registrar en el historial
        historial.append({
            'anio': anio,
            'balance': round(balance_final_anio, 2),
            'interes_ganado': round(interes_ganado, 2)
        })
        
        # 5. Actualizar balance para el próximo año
        balance_actual = balance_final_anio
        
    return historial


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    print("\n--- Ejercicio 1: Calculadora ---")
    try:
        print(f"Suma (10.5, 2.3): {calculadora_cientifica('suma', 10.5, 2.3)}") # 12.80
        print(f"División (10, 3): {calculadora_cientifica('division', 10, 3)}") # 3.33
        print(f"Potencia (2, 4): {calculadora_cientifica('potencia', 2, 4)}") # 16.00
        print(f"Módulo (10, 3): {calculadora_cientifica('modulo', 10, 3)}") # 1.00
        # Prueba de error de división por cero
        # print(f"División (10, 0): {calculadora_cientifica('division', 10, 0)}") 
    except (ValueError, ZeroDivisionError) as e:
        print(f"ERROR: {e}")
    
    print("\n" + "-"*70)

    print("\n--- Ejercicio 2: Validador de Password ---")
    validador_estandar = ValidadorPassword()
    validador_simple = ValidadorPassword(min_longitud=6, requiere_mayuscula=False, requiere_especial=False)

    p1 = "aBcd123!" # Válida estándar
    p2 = "short1!" # Larga, pero no cumple min_longitud 8
    p3 = "abcdefghij123" # No tiene especial/mayuscula (para el simple si pasaría)

    # Prueba estándar
    valido, errores = validador_estandar.validar(p1)
    print(f"'{p1}' (Estándar): Válido={valido}, Errores={errores}")
    print(f"'{p1}' es fuerte: {validador_estandar.es_fuerte(p1)}") # Falso (largo < 12)

    valido, errores = validador_estandar.validar(p2)
    print(f"'{p2}' (Estándar): Válido={valido}, Errores={errores}")
    
    p_fuerte = "PassWordFuerte123!" # Válida fuerte
    print(f"'{p_fuerte}' es fuerte: {validador_estandar.es_fuerte(p_fuerte)}") # Verdadero

    # Prueba simple
    valido, errores = validador_simple.validar(p3)
    print(f"'{p3}' (Simple): Válido={valido}, Errores={errores}")

    print("\n" + "-"*70)

    print("\n--- Ejercicio 3: Gestor de Inventario ---")
    gestor = GestorInventario()
    try:
        gestor.agregar_producto("A001", "Laptop G-Pro", 1200.50, 20, "Electrónica")
        gestor.agregar_producto("B002", "Mouse Óptico", 15.99, 5, "Electrónica")
        gestor.agregar_producto("C003", "Cuaderno A4", 2.50, 100, "Papelería")
        gestor.agregar_producto("A004", "Monitor 27'", 350.00, 8, "Electrónica")
        # gestor.agregar_producto("A001", "Duplicado", 10, 1, "Error") # Debe lanzar ValueError
        
        gestor.actualizar_stock("A001", -5) # Venta de 5 Laptops
        # gestor.actualizar_stock("B002", -10) # Debe lanzar ValueError por stock negativo

        print(f"Productos Electrónica: {gestor.buscar_por_categoria('Electrónica')}")
        print(f"Productos bajo stock (<10): {gestor.productos_bajo_stock(10)}")
        print(f"Valor total inventario: ${gestor.valor_total_inventario():.2f}")
        print(f"Top 2 productos por valor: {gestor.top_productos(2)}")
        
    except ValueError as e:
        print(f"ERROR en Inventario: {e}")

    print("\n" + "-"*70)

    print("\n--- Ejercicio 4: Calendario ---")
    print(f"1999 es bisiesto: {es_bisiesto(1999)}") # False
    print(f"2000 es bisiesto: {es_bisiesto(2000)}") # True (Divisible por 400)
    print(f"2100 es bisiesto: {es_bisiesto(2100)}") # False (Divisible por 100, no por 400)
    print(f"2024 es bisiesto: {es_bisiesto(2024)}") # True

    try:
        print(f"\nDías en Feb 2024: {dias_en_mes(2, 2024)}") # 29
        print(f"Días en Feb 2023: {dias_en_mes(2, 2023)}") # 28
        print(f"Días en Abril 2024: {dias_en_mes(4, 2024)}") # 30
    except ValueError as e:
        print(f"ERROR: {e}")
        
    # Asumimos que el 1 de Marzo de 2024 cae en Viernes (4 si Lunes=0)
    print("\nCalendario Marzo 2024 (1er día = Viernes)")
    print(generar_calendario(3, 2024, dia_inicio=4))

    print("\n" + "-"*70)

    print("\n--- Ejercicio 5: Análisis de Datos ---")
    ventas_data = [
        {'producto': 'A', 'cantidad': 10, 'precio': 5.00, 'descuento': 10}, # 50 - 5 = 45.00
        {'producto': 'B', 'cantidad': 3, 'precio': 20.00, 'descuento': 0}, # 60.00
        {'producto': 'A', 'cantidad': 5, 'precio': 5.00, 'descuento': 0}, # 25.00
        {'producto': 'C', 'cantidad': 1, 'precio': 100.00, 'descuento': 5}, # 100 - 5 = 95.00 (Venta Mayor)
    ]
    
    analisis = analizar_ventas(ventas_data)
    print("Análisis de Ventas:")
    for k, v in analisis.items():
        print(f"- {k}: {v}")

    
    numeros_data = [1, 2, 2, 4, 3, 5, 6, 6, 6, 4, 2, 1]
    patrones = encontrar_patrones(numeros_data)
    print("\nAnálisis de Patrones (1, 2, 2, 4, 3, 5, 6, 6, 6, 4, 2, 1):")
    for k, v in patrones.items():
        print(f"- {k}: {v}")
    # Resultado esperado: 
    # sec_asc: 2 (2->4, 3->6)
    # sec_desc: 3 (4->3, 6->4, 4->1)
    # max_asc: 3 (3, 5, 6)
    # max_desc: 4 (6, 4, 2, 1)

    print("\nSimulación de Crecimiento (1000, 5%, 3 años, +100 anual):")
    simulacion = simular_crecimiento(1000, 0.05, 3, 100)
    for registro in simulacion:
        print(f"Año {registro['anio']}: Balance={registro['balance']:.2f}, Interés={registro['interes_ganado']:.2f}")

    print("\n" + "="*70)