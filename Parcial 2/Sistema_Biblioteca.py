
#!/usr/bin/env python3
"""
Estudiante: [Santiago Rico Cardona]
Fecha: [21/10/25]
"""

from datetime import datetime, timedelta
import os
import random

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS (5 puntos)
# ===========================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza para operaciones con préstamos vencidos."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA BIBLIOTECA (35 puntos)
# ===========================================================================

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    
    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa', 'pagada'}}
    """
    
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.
        """
        self.DIAS_PRESTAMO = dias_prestamo
        self.MULTA_POR_DIA = multa_por_dia
        self.LIMITE_PRESTAMOS = limite_prestamos
        
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self._next_prestamo_id = 1
    
    
    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.
        """
        if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
            raise ValueError("ISBN debe ser un string de 13 dígitos.")
        if not titulo or not autor:
            raise ValueError("Título y autor no pueden estar vacíos.")
        try:
            anio_int = int(anio)
            if not (1000 <= anio_int <= datetime.now().year):
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError(f"Año debe ser un número entre 1000 y {datetime.now().year}.")
        if not isinstance(copias, int) or copias < 1:
            raise ValueError("El número de copias debe ser un entero positivo (>= 1).")
        
        if isbn in self.catalogo:
            raise KeyError(f"Libro con ISBN {isbn} ya existe.")
        
        self.catalogo[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio_int,
            'categoria': categoria,
            'copias_total': copias,
            'copias_disponibles': copias
        }
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        """
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
            
        libro = self.catalogo[isbn]
        
        nueva_total = libro['copias_total'] + cantidad_cambio
        nueva_disponible = libro['copias_disponibles'] + cantidad_cambio
        
        if nueva_total < 0 or nueva_disponible < 0:
            raise ValueError("El resultado de la operación resultaría en copias negativas.")
            
        libro['copias_total'] = nueva_total
        libro['copias_disponibles'] = nueva_disponible
    
    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """
        Busca libros por diferentes criterios.
        """
        resultados = []
        valor_lower = str(valor).lower()
        
        for isbn, info in self.catalogo.items():
            coincide_criterio = False
            
            if criterio == 'titulo' and valor_lower in info['titulo'].lower():
                coincide_criterio = True
            elif criterio == 'autor' and valor_lower in info['autor'].lower():
                coincide_criterio = True
            elif criterio == 'anio' and str(info['anio']) == valor_lower:
                coincide_criterio = True
            
            if coincide_criterio:
                if categoria is None or info['categoria'].lower() == categoria.lower():
                    resultados.append({'isbn': isbn, **info})
                    
        return resultados
    
   
    
    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario.
        """
        if id_usuario in self.usuarios:
            raise ValueError(f"ID de usuario '{id_usuario}' ya está registrado.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if '@' not in email or '.' not in email:
            raise ValueError("Formato de email incorrecto (debe contener '@' y '.').")
            
        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now().strftime("%Y-%m-%d"),
            'prestamos_activos': set(),
            'historial': []
        }
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        """
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
            
        usuario = self.usuarios[id_usuario]
        
        multas_pendientes = 0.0
        for id_prestamo in usuario['historial']:
            prestamo = self.prestamos.get(id_prestamo)
            if prestamo and 'multa' in prestamo and not prestamo.get('pagada', False):
                multas_pendientes += prestamo['multa']

       
        for id_prestamo in usuario['prestamos_activos']:
            multa_actual = self._calcular_multa_actual(id_prestamo)
            multas_pendientes += multa_actual

        puede_prestar = (
            len(usuario['prestamos_activos']) < self.LIMITE_PRESTAMOS and 
            multas_pendientes <= 50.0
        )
        
        return {
            'nombre': usuario['nombre'],
            'prestamos_activos': len(usuario['prestamos_activos']),
            'puede_prestar': puede_prestar,
            'multas_pendientes': round(multas_pendientes, 2)
        }
    
   

    def _get_next_prestamo_id(self):
        """Genera y retorna el siguiente ID de préstamo."""
        id_p = f"P{self._next_prestamo_id:05d}"
        self._next_prestamo_id += 1
        return id_p

    def _calcular_dias_retraso(self, fecha_vencimiento, fecha_actual=None):
        """Calcula días de retraso."""
        fecha_actual = fecha_actual or datetime.now()
        if fecha_actual > fecha_vencimiento:
            retraso = (fecha_actual - fecha_vencimiento).days
            return retraso
        return 0

    def _calcular_multa_actual(self, id_prestamo):
        """Calcula la multa actual para un préstamo activo."""
        prestamo = self.prestamos.get(id_prestamo)
        if not prestamo or prestamo.get('fecha_devolucion'):
            return 0.0

        vencimiento_str = prestamo['fecha_vencimiento']
        fecha_vencimiento = datetime.strptime(vencimiento_str, "%Y-%m-%d")
        
        dias_retraso = self._calcular_dias_retraso(fecha_vencimiento)
        return round(dias_retraso * self.MULTA_POR_DIA, 2)

    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo.
        """
      
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        usuario = self.usuarios[id_usuario]
        
       
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        libro = self.catalogo[isbn]
        
        if libro['copias_disponibles'] < 1:
            raise LibroNoDisponible(isbn, libro['titulo'])
            
        
        if len(usuario['prestamos_activos']) >= self.LIMITE_PRESTAMOS:
            raise LimitePrestamosExcedido(id_usuario, self.LIMITE_PRESTAMOS)

        
        estado_usuario = self.obtener_estado_usuario(id_usuario)
        if estado_usuario['multas_pendientes'] > 50.0:
            raise ValueError(f"Usuario {id_usuario} tiene multas pendientes de {estado_usuario['multas_pendientes']} que exceden el límite de $50.")
            
       
        id_prestamo = self._get_next_prestamo_id()
        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.DIAS_PRESTAMO)
        
        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo.strftime("%Y-%m-%d"),
            'fecha_vencimiento': fecha_vencimiento.strftime("%Y-%m-%d"),
            'fecha_devolucion': None,
            'multa': 0.0,
            'pagada': False
        }
        
        
        usuario['prestamos_activos'].add(id_prestamo)
        usuario['historial'].append(id_prestamo)
        libro['copias_disponibles'] -= 1
        
        return id_prestamo
    
    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo con ID {id_prestamo} no encontrado.")
            
        prestamo = self.prestamos[id_prestamo]
        
        if prestamo.get('fecha_devolucion'):
            raise ValueError(f"Préstamo {id_prestamo} ya fue devuelto en {prestamo['fecha_devolucion']}.")

        fecha_vencimiento = datetime.strptime(prestamo['fecha_vencimiento'], "%Y-%m-%d")
        fecha_devolucion = datetime.now()
        
        dias_retraso = self._calcular_dias_retraso(fecha_vencimiento, fecha_devolucion)
        multa_calculada = round(dias_retraso * self.MULTA_POR_DIA, 2)

        
        prestamo['fecha_devolucion'] = fecha_devolucion.strftime("%Y-%m-%d")
        prestamo['multa'] = multa_calculada
        
      
        self.catalogo[prestamo['isbn']]['copias_disponibles'] += 1
        
       
        id_usuario = prestamo['id_usuario']
        if id_prestamo in self.usuarios[id_usuario]['prestamos_activos']:
            self.usuarios[id_usuario]['prestamos_activos'].remove(id_prestamo)
            
        mensaje = f"Devolución exitosa. Multa: ${multa_calculada}" if multa_calculada > 0 else "Devolución exitosa a tiempo."
        
        return {
            'dias_retraso': dias_retraso, 
            'multa': multa_calculada, 
            'mensaje': mensaje
        }
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo con ID {id_prestamo} no encontrado.")
        
        prestamo = self.prestamos[id_prestamo]
        
        if prestamo.get('fecha_devolucion'):
            raise ValueError("No se puede renovar un préstamo ya devuelto.")
            
        fecha_vencimiento_actual = datetime.strptime(prestamo['fecha_vencimiento'], "%Y-%m-%d")
        
        dias_retraso = self._calcular_dias_retraso(fecha_vencimiento_actual)
        
        if dias_retraso > 0:
            raise PrestamoVencido(id_prestamo, dias_retraso)
            
    
        nueva_fecha_vencimiento = fecha_vencimiento_actual + timedelta(days=self.DIAS_PRESTAMO)
        prestamo['fecha_vencimiento'] = nueva_fecha_vencimiento.strftime("%Y-%m-%d")
        
        return f"Préstamo {id_prestamo} renovado. Nueva fecha de vencimiento: {prestamo['fecha_vencimiento']}"
    
  
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        """
        conteo_prestamos = {}
        for prestamo in self.prestamos.values():
            isbn = prestamo['isbn']
            conteo_prestamos[isbn] = conteo_prestamos.get(isbn, 0) + 1
            
      
        ranking = sorted(conteo_prestamos.items(), key=lambda item: item[1], reverse=True)
        
        resultados = []
        for isbn, cantidad in ranking[:n]:
            titulo = self.catalogo.get(isbn, {}).get('titulo', 'Título Desconocido')
            resultados.append((isbn, titulo, cantidad))
            
        return resultados
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        """
        ranking_usuarios = []
        for id_usuario, info in self.usuarios.items():
            total_prestamos = len(info['historial'])
            ranking_usuarios.append((id_usuario, info['nombre'], total_prestamos))
            
        
        ranking_usuarios.sort(key=lambda item: item[2], reverse=True)
        
        return ranking_usuarios[:n]
    
    def estadisticas_categoria(self, categoria):
        """
        Genera estadísticas de una categoría.
        """
        categoria_lower = categoria.lower()
        total_libros = 0
        total_copias = 0
        copias_prestadas = 0
        
        libros_en_categoria = {}

        
        for isbn, info in self.catalogo.items():
            if info['categoria'].lower() == categoria_lower:
                total_libros += 1
                total_copias += info['copias_total']
                copias_prestadas += info['copias_total'] - info['copias_disponibles']
                libros_en_categoria[isbn] = 0

        if total_libros == 0:
            return {
                'total_libros': 0, 'total_copias': 0, 'copias_prestadas': 0,
                'tasa_prestamo': 0.0, 'libro_mas_popular': 'N/A'
            }

        
        for prestamo in self.prestamos.values():
            isbn = prestamo['isbn']
            if isbn in libros_en_categoria:
                libros_en_categoria[isbn] += 1

   
        total_prestamos_categoria = sum(libros_en_categoria.values())
        tasa_prestamo = round((total_prestamos_categoria / total_copias) if total_copias > 0 else 0.0, 4)

        
        libro_mas_popular_isbn = max(libros_en_categoria, key=libros_en_categoria.get) if libros_en_categoria else None
        
        libro_mas_popular_titulo = 'N/A'
        if libro_mas_popular_isbn and libros_en_categoria[libro_mas_popular_isbn] > 0:
            libro_mas_popular_titulo = self.catalogo[libro_mas_popular_isbn]['titulo']
        elif libro_mas_popular_isbn:
             libro_mas_popular_titulo = self.catalogo[libro_mas_popular_isbn]['titulo'] + " (0 préstamos)"

        return {
            'total_libros': total_libros,
            'total_copias': total_copias,
            'copias_prestadas': copias_prestadas,
            'tasa_prestamo': tasa_prestamo,
            'libro_mas_popular': libro_mas_popular_titulo
        }
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        """
        vencidos = []
        now = datetime.now()
        
        for id_prestamo, prestamo in self.prestamos.items():
          
            if prestamo['fecha_devolucion'] is None:
                fecha_vencimiento = datetime.strptime(prestamo['fecha_vencimiento'], "%Y-%m-%d")
                dias_retraso = self._calcular_dias_retraso(fecha_vencimiento, now)
                
                if dias_retraso > 0:
                    multa_acumulada = round(dias_retraso * self.MULTA_POR_DIA, 2)
                    
                    libro_info = self.catalogo.get(prestamo['isbn'], {'titulo': 'Desconocido'})
                    
                    vencidos.append({
                        'id_prestamo': id_prestamo,
                        'isbn': prestamo['isbn'],
                        'titulo': libro_info['titulo'],
                        'id_usuario': prestamo['id_usuario'],
                        'dias_retraso': dias_retraso,
                        'multa_acumulada': multa_acumulada
                    })
                    
        return vencidos
    
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.
        """
        total_multas = 0.0
        multas_pagadas = 0.0
        multas_pendientes = 0.0
        prestamos_con_multa = 0
        total_multas_contadas = 0

        dt_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d") if fecha_inicio else None
        dt_fin = datetime.strptime(fecha_fin, "%Y-%m-%d") if fecha_fin else None

        for id_prestamo, prestamo in self.prestamos.items():
            if prestamo['fecha_devolucion']:
                fecha_devolucion = datetime.strptime(prestamo['fecha_devolucion'], "%Y-%m-%d")
                
           
                if (dt_inicio is None or fecha_devolucion >= dt_inicio) and \
                   (dt_fin is None or fecha_devolucion <= dt_fin):

                    multa = prestamo.get('multa', 0.0)
                    total_multas += multa
                    total_multas_contadas += 1

                    if multa > 0:
                        prestamos_con_multa += 1

                    if prestamo.get('pagada', False):
                        multas_pagadas += multa
                    else:
                        multas_pendientes += multa
        
        
        if dt_fin is None or dt_fin >= datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
            for id_prestamo, prestamo in self.prestamos.items():
                if prestamo['fecha_devolucion'] is None:
                    multa_activa = self._calcular_multa_actual(id_prestamo)
                    
               
                    if multa_activa > 0:
                       
                        total_multas += multa_activa
                        multas_pendientes += multa_activa
                        prestamos_con_multa += 1
                        total_multas_contadas += 1

        promedio_multa = round((total_multas / total_multas_contadas) if total_multas_contadas > 0 else 0.0, 2)
            
        return {
            'total_multas': round(total_multas, 2),
            'multas_pagadas': round(multas_pagadas, 2),
            'multas_pendientes': round(multas_pendientes, 2),
            'prestamos_con_multa': prestamos_con_multa,
            'promedio_multa': promedio_multa
        }
    

    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        """
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for isbn, info in self.catalogo.items():
                    linea = f"{isbn}|{info['titulo']}|{info['autor']}|{info['anio']}|{info['categoria']}|{info['copias_total']}\n"
                    f.write(linea)
            print(f"Catálogo exportado exitosamente a '{archivo}'.")
        except IOError as e:
            print(f"Error al escribir en el archivo '{archivo}': {e}")
            raise
    
    def importar_catalogo(self, archivo='catalogo.txt'):
        """
        Importa catálogo desde archivo de texto.
        """
        exitosos = 0
        errores = []
        
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"El archivo '{archivo}' no existe.")
            
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for num_linea, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if not linea:
                        continue
                        
                    try:
                        partes = linea.split('|')
                        if len(partes) != 6:
                            raise ValueError("Número incorrecto de campos.")
                            
                        isbn, titulo, autor, anio_str, categoria, copias_str = partes
                        
                        if isbn in self.catalogo:
                            errores.append((num_linea, f"ISBN {isbn} ya existe (duplicado, omitido)."))
                            continue
                            
                        anio = int(anio_str)
                        copias = int(copias_str)

                        try:
                            self.agregar_libro(isbn, titulo, autor, anio, categoria, copias)
                            exitosos += 1
                        except Exception as e:
                            
                            if isbn in self.catalogo:
                                del self.catalogo[isbn] 
                            raise e

                    except Exception as e:
                        errores.append((num_linea, f"Error de formato/validación: {e}"))

        except IOError as e:
            raise IOError(f"Error al leer el archivo '{archivo}': {e}")
        
        return {'exitosos': exitosos, 'errores': errores}


# ===========================================================================
# CASOS DE PRUEBA BÁSICOS
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("="*70)
    
 
    biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)
    
    print("\n✓ Sistema inicializado")
    
    
    print("\n--- 1. Gestión de Catálogo ---")
    
    try:
      
        biblioteca.agregar_libro("9780321765723", "The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasía", 5)
        biblioteca.agregar_libro("9788498387081", "Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción", 3)
        biblioteca.agregar_libro("9780061120084", "To Kill a Mockingbird", "Harper Lee", 1960, "Clásico", 2)
        print("✓ 3 libros agregados.")
        
    
        biblioteca.actualizar_copias("9780321765723", 2)
        print("✓ Copias de 'The Lord of the Rings' actualizadas a 7.")
        
      
        resultados = biblioteca.buscar_libros(criterio='autor', valor='garcía')
        print(f"✓ Búsqueda por autor 'garcía' encontró: {len(resultados)} libro(s).")
        
    except Exception as e:
        print(f"ERROR en Catálogo: {e}")

    
    print("\n--- 2. Gestión de Usuarios ---")
    
    try:
        biblioteca.registrar_usuario("U1001", "Ana Pérez", "ana.perez@email.com")
        biblioteca.registrar_usuario("U1002", "Juan Gómez", "juan.gomez@email.com")
        print("✓ 2 usuarios registrados.")
        
        estado = biblioteca.obtener_estado_usuario("U1001")
        print(f"✓ Estado U1001: Puede prestar: {estado['puede_prestar']}, Préstamos Activos: {estado['prestamos_activos']}")
        
    except Exception as e:
        print(f"ERROR en Usuarios: {e}")
        
    
    print("\n--- 3. Gestión de Préstamos ---")
    
    try:
        
        id_p1 = biblioteca.prestar_libro("9780321765723", "U1001")
        print(f"✓ Préstamo {id_p1} (U1001 - LOTR) realizado.")
        
        
        biblioteca.prestamos["P00002"] = { 
            'isbn': "9788498387081",
            'id_usuario': "U1002",
            'fecha_prestamo': (datetime.now() - timedelta(days=10)).strftime("%Y-%m-%d"),
            'fecha_vencimiento': (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"), 
            'fecha_devolucion': None,
            'multa': 0.0,
            'pagada': False
        }
        biblioteca.usuarios["U1002"]['prestamos_activos'].add("P00002")
        biblioteca.usuarios["U1002"]['historial'].append("P00002")
        biblioteca.catalogo["9788498387081"]['copias_disponibles'] -= 1
        biblioteca._next_prestamo_id = 3
        print("✓ Préstamo P00002 simulado como vencido (3 días de retraso).")
        
        
        try:
            biblioteca.renovar_prestamo("P00002")
        except PrestamoVencido as e:
            print(f"✓ Error esperado al renovar P00002: {e}")
            
      
        resultado_dev = biblioteca.devolver_libro("P00002")
        print(f"✓ Devolución P00002: Retraso: {resultado_dev['dias_retraso']} días, Multa: ${resultado_dev['multa']}")
        
      
        resultado_dev_ok = biblioteca.devolver_libro(id_p1)
        print(f"✓ Devolución {id_p1}: Multa: ${resultado_dev_ok['multa']}")
        
    except Exception as e:
        print(f"ERROR en Préstamos: {e}")

   
    print("\n--- 4. Reportes ---")

    
    biblioteca.prestar_libro("9780321765723", "U1001")
    biblioteca.prestar_libro("9780061120084", "U1001")
    biblioteca.prestar_libro("9780321765723", "U1002")

    libros_top = biblioteca.libros_mas_prestados(2)
    print(f"✓ Top 2 libros más prestados: {libros_top}")

    usuarios_top = biblioteca.usuarios_mas_activos(1)
    print(f"✓ Top 1 usuario más activo: {usuarios_top}")
    
    stats_fantasia = biblioteca.estadisticas_categoria("Fantasía")
    print(f"✓ Stats Fantasía: Libros: {stats_fantasia['total_libros']}, Tasa: {stats_fantasia['tasa_prestamo']}")

    reporte_fin = biblioteca.reporte_financiero()
    print(f"✓ Reporte Financiero (Total Multas): ${reporte_fin['total_multas']}")
    
    
    print("\n--- 5. Utilidades ---")
    
    try:
        biblioteca.exportar_catalogo('temp_catalogo.txt')
       
        nueva_biblioteca = SistemaBiblioteca() 
        reporte_import = nueva_biblioteca.importar_catalogo('temp_catalogo.txt')
        print(f"✓ Catálogo importado: {reporte_import['exitosos']} exitosos, {len(reporte_import['errores'])} errores.")
        os.remove('temp_catalogo.txt')
        
    except Exception as e:
        print(f"ERROR en Utilidades: {e}")

    print("="*70)
    print(" FIN DE PRUEBAS")
    print("="*70)
