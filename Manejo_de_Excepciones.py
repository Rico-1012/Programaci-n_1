#!/usr/bin/env python3
"""
EJERCICIOS PARA ESTUDIANTES - MANEJO DE EXCEPCIONES
Solución completa a los ejercicios de exploración de conceptos confusos.
"""
import os
import json
import logging

# Configuración básica de logging para el Ejercicio 7
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicio del programa
limpiar_pantalla()

# ===========================================================================
# Ejercicio 1: Encuentra y arregla el except desnudo
# ===========================================================================
print("\n--- EJERCICIO 1: ARREGLA EL EXCEPT DESNUDO ---")
print("Esta función tiene un except desnudo. Arréglalo para capturar excepciones específicas.")
print()

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    ARREGLA: Usa manejo de excepciones específico en lugar de except desnudo.
    """
    try:
        total = sum(numeros)
        promedio = total / len(numeros)
        return promedio
    except ZeroDivisionError: # Para manejar len(numeros) == 0
        print("Error: No se puede calcular el promedio de una lista vacía.")
        return None
    except TypeError: # Para manejar elementos no numéricos en la lista
        print("Error: La lista debe contener solo números para calcular el promedio.")
        return None

# Prueba tu arreglo:
print(f"Promedio [1, 2, 3]: {calcular_promedio([1, 2, 3])}")
print(f"Promedio []: {calcular_promedio([])}")
print(f"Promedio [1, 2, 'a']: {calcular_promedio([1, 2, 'a'])}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 2: Añade retroalimentación al usuario
# ===========================================================================
print("\n--- EJERCICIO 2: AÑADE RETROALIMENTACIÓN ---")
print("Este código falla silenciosamente. Añade mensajes apropiados.")
print()

def guardar_datos(datos, archivo):
    """
    Guarda datos en un archivo.
    ARREGLA: Añade manejo de excepciones Y feedback al usuario.
    """
    try:
        with open(archivo, 'w') as f:
            f.write(str(datos))
        print(f"Éxito: Datos guardados correctamente en '{archivo}'.")
        return True
    except FileNotFoundError:
        print(f"Error: La ruta del archivo '{archivo}' no se encontró.")
        return False
    except PermissionError:
        print(f"Error: No tienes permiso para escribir en la ubicación '{archivo}'.")
        return False
    except Exception as e:
        print(f"Error desconocido al intentar guardar los datos: {type(e).__name__} - {e}")
        return False


# Prueba tu arreglo:
guardar_datos({"usuario": "Ana"}, "datos.txt")
guardar_datos({"usuario": "Ana"}, "/ruta/invalida/datos.txt")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 3: Usa else y finally correctamente
# ===========================================================================
print("\n--- EJERCICIO 3: USA ELSE Y FINALLY ---")
print("Implementa un manejo completo de archivos con else y finally.")
print()

def procesar_archivo(nombre_archivo):
    """
    Lee y procesa un archivo.
    TODO: Implementa try-except-else-finally:
    - try: abrir y leer archivo
    - except: manejar FileNotFoundError
    - else: procesar los datos (solo si lectura exitosa)
    - finally: asegurar que el archivo se cierre
    """
    f = None
    try:
        print(f"Intentando abrir el archivo '{nombre_archivo}'...")
        f = open(nombre_archivo, 'r')
        contenido = f.read()
    except FileNotFoundError:
        print(f"EXCEPCIÓN: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"EXCEPCIÓN DESCONOCIDA: Ocurrió un error al leer: {e}")
    else:
        # Se ejecuta SÓLO si el bloque try fue exitoso
        print("ELSE: Lectura exitosa. Procesando datos (mostrando primeras 20 letras):")
        print(f" -> '{contenido[:20]}...'")
    finally:
        # Se ejecuta SIEMPRE, haya o no excepción
        if f:
            f.close()
            print("FINALLY: Archivo cerrado de forma segura.")
        else:
            print("FINALLY: No había archivo que cerrar (falló en try o archivo no existe).")

# Creando archivo de prueba
with open("existente.txt", "w") as f_temp:
    f_temp.write("Este es el contenido del archivo existente y será procesado.")

# Prueba tu implementación:
procesar_archivo("existente.txt")
print("-" * 50)
procesar_archivo("faltante.txt")
os.remove("existente.txt") # Limpieza

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 4: Lanza excepciones apropiadas
# ===========================================================================
print("\n--- EJERCICIO 4: LANZA EXCEPCIONES ---")
print("Implementa validación con excepciones específicas.")
print()

def crear_usuario(nombre_usuario, edad, email):
    """
    Crea un nuevo usuario con validación.
    TODO: Lanza excepciones apropiadas si:
    - nombre_usuario tiene menos de 3 caracteres (ValueError)
    - edad no es un entero (TypeError)
    - edad es negativa o mayor a 150 (ValueError)
    - email no contiene '@' (ValueError)
    """
    if len(nombre_usuario) < 3:
        raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
    
    if not isinstance(edad, int):
        raise TypeError(f"La edad debe ser un número entero, no '{type(edad).__name__}'.")

    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años.")

    if '@' not in email:
        raise ValueError("El correo electrónico no es válido (falta '@').")
    
    return {"nombre_usuario": nombre_usuario, "edad": edad, "email": email}

# Prueba tu implementación:
print("\nPruebas (deberían fallar):")
try:
    print(f"Usuario Válido: {crear_usuario('Ana', 25, 'ana@example.com')}")
except Exception as e:
    print(f"Error inesperado con usuario válido: {e}")

try:
    crear_usuario("Ab", 25, "ana@example.com")
except ValueError as e:
    print(f"Error esperado (nombre corto): {e}")

try:
    crear_usuario("Ana", "25", "ana@example.com")
except TypeError as e:
    print(f"Error esperado (edad tipo incorrecto): {e}")

try:
    crear_usuario("Ana", -5, "ana@example.com")
except ValueError as e:
    print(f"Error esperado (edad negativa): {e}")

try:
    crear_usuario("Ana", 25, "anaexample.com")
except ValueError as e:
    print(f"Error esperado (email sin @): {e}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 5: Crea excepciones personalizadas
# ===========================================================================
print("\n--- EJERCICIO 5: EXCEPCIONES PERSONALIZADAS ---")
print("Crea excepciones personalizadas para un sistema bancario.")
print()

# Excepciones personalizadas
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        self.saldo = saldo
        self.monto = monto
        super().__init__(f"Saldo insuficiente: Necesitas ${monto}, tienes ${saldo}.")

class MontoInvalidoError(Exception):
    def __init__(self, monto):
        super().__init__(f"Monto de transacción inválido: {monto}. Debe ser positivo.")

def retirar(saldo, monto):
    """
    Retira dinero de una cuenta.
    TODO: 
    - Lanza MontoInvalidoError si monto <= 0
    - Lanza SaldoInsuficienteError si monto > saldo
    - Retorna nuevo saldo si exitoso
    """
    if monto <= 0:
        raise MontoInvalidoError(monto)
    
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
        
    return saldo - monto

# Prueba tu implementación:
print("\nPruebas (deberían fallar y mostrar mensaje):")
print(f"Nuevo saldo: {retirar(100, 50)}")

try:
    retirar(100, 150)
except SaldoInsuficienteError as e:
    print(f"Error esperado (SaldoInsuficienteError): {e}")

try:
    retirar(100, -10)
except MontoInvalidoError as e:
    print(f"Error esperado (MontoInvalidoError): {e}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 6: Maneja excepciones en bucles
# ===========================================================================
print("\n--- EJERCICIO 6: EXCEPCIONES EN BUCLES ---")
print("Procesa una lista con manejo de errores.")
print()

def procesar_lista_numeros(lista_strings):
    """
    Convierte strings a números y los duplica.
    TODO: 
    - Intenta convertir cada elemento a int
    - Si falla, registra el error pero continúa con los demás
    - Retorna tupla (resultados_exitosos, lista_errores)
    """
    resultados_exitosos = []
    lista_errores = []

    for elemento in lista_strings:
        try:
            numero = int(elemento)
            resultados_exitosos.append(numero * 2)
        except ValueError as e:
            # Registra el error y el elemento que lo causó, pero no detiene el bucle
            lista_errores.append((elemento, str(e)))
        except TypeError as e:
            # Solo por seguridad si la lista tuviera elementos de tipos extraños
            lista_errores.append((elemento, str(e)))
            
    return resultados_exitosos, lista_errores

# Prueba tu implementación:
resultados, errores = procesar_lista_numeros(["1", "2", "abc", "4", "xyz", 5])
print(f"Exitosos: {resultados}")
print(f"Errores (Elemento, Causa): {errores}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 7: Re-lanza excepciones apropiadamente
# ===========================================================================
print("\n--- EJERCICIO 7: RE-LANZA EXCEPCIONES ---")
print("Registra errores pero permite que el llamador los maneje.")
print()

def operacion_critica(valor):
    """
    Realiza operación crítica con logging.
    TODO:
    - Intenta procesar valor
    - Si falla, registra el error (print)
    - Re-lanza la excepción para que el llamador pueda manejarla
    """
    try:
        resultado = 100 / int(valor)
        return resultado
    except (ValueError, ZeroDivisionError) as e:
        # Registra el error
        print(f"LOG INTERNO: Error crítico al procesar el valor '{valor}': {type(e).__name__} - {e}")
        # Re-lanza la excepción
        raise

# Prueba tu implementación:
print(f"Resultado (10): {operacion_critica('10')}")

try:
    print("\nLanzando error (0):")
    operacion_critica("0")
except ZeroDivisionError:
    print("Llamador: Manejo el error de división por cero.")
except Exception as e:
    print(f"Llamador: Manejo cualquier otro error: {e}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 8: Excepción con múltiples except
# ===========================================================================
print("\n--- EJERCICIO 8: MÚLTIPLES EXCEPT ---")
print("Maneja diferentes tipos de errores de manera diferente.")
print()

def calculadora_segura(operacion, a, b):
    """
    Realiza operaciones matemáticas con manejo de errores.
    TODO: Implementa try con múltiples except:
    - ZeroDivisionError: retorna mensaje específico
    - TypeError: retorna mensaje específico
    - ValueError: retorna mensaje específico (para operación inválida)
    """
    try:
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        elif operacion == "multiplicacion":
            return a * b
        elif operacion == "division":
            return a / b
        else:
            raise ValueError(f"Operación inválida: '{operacion}'.")

    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Los operandos deben ser números."
    except ValueError as e:
        # Captura la excepción lanzada si la operación es inválida
        return f"Error de Valor: {e}"
    except Exception as e:
        return f"Error desconocido: {e}"

# Prueba tu implementación:
print(f"Suma (10, 5): {calculadora_segura('suma', 10, 5)}")
print(f"División (10, 0): {calculadora_segura('division', 10, 0)}")
print(f"Suma (10, '5'): {calculadora_segura('suma', 10, '5')}")
print(f"Operación Invalida: {calculadora_segura('invalida', 10, 5)}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 9: Contexto de excepción
# ===========================================================================
print("\n--- EJERCICIO 9: CONTEXTO DE EXCEPCIÓN ---")
print("Preserva el contexto al lanzar nuevas excepciones.")
print()

def parsear_configuracion(json_string):
    """
    Parsea configuración JSON.
    TODO: 
    - Intenta parsear JSON
    - Si falla, lanza ValueError con 'from' para preservar el error original
    """
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as original_error:
        # Lanzamos una nueva excepción (ValueError) que es más significativa para el llamador,
        # pero mantenemos el error original (JSONDecodeError) como causa.
        raise ValueError("Error al parsear la configuración JSON. Revise la sintaxis.") from original_error

# Prueba tu implementación:
print("\nJSON Válido:")
print(parsear_configuracion('{"nombre": "Ana", "edad": 30}'))

print("\nJSON Inválido:")
try:
    parsear_configuracion('json invalido')
except ValueError as e:
    print(f"Error (ValueError): {e}")
    # Accediendo a la excepción original
    print(f"Causado por (Original Error): {e.__cause__}") 

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Ejercicio 10: Proyecto completo
# ===========================================================================
print("\n--- EJERCICIO 10: PROYECTO COMPLETO ---")
print("Crea un sistema de gestión de inventario con manejo completo de excepciones.")
print()

# Excepciones personalizadas
class ErrorInventario(Exception):
    """Clase base para errores de inventario."""
    pass
 
class ProductoNoEncontrado(ErrorInventario):
    """Se lanza cuando un producto no existe en el inventario."""
    def __init__(self, codigo):
        super().__init__(f"Producto con código '{codigo}' no encontrado.")
 
class StockInsuficiente(ErrorInventario):
    """Se lanza cuando se intenta retirar más stock del disponible."""
    def __init__(self, codigo, requerido, disponible):
        super().__init__(f"Stock insuficiente para '{codigo}'. Requerido: {requerido}, Disponible: {disponible}.")

class ProductoExistente(ErrorInventario):
     """Se lanza cuando se intenta agregar un producto con un código que ya existe."""
     def __init__(self, codigo):
        super().__init__(f"El producto con código '{codigo}' ya existe.")


class Inventario:
    """Sistema de inventario con manejo completo de excepciones."""
    
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, codigo, nombre, cantidad):
        """
        Añade producto al inventario.
        TODO: 
        - Validar que cantidad sea positiva (ValueError)
        - Validar que codigo no exista ya (ProductoExistente)
        """
        if cantidad <= 0:
            raise ValueError("La cantidad inicial debe ser positiva.")
        
        if codigo in self.productos:
            raise ProductoExistente(codigo)
            
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        print(f"INFO: Producto '{nombre}' ({codigo}) agregado con {cantidad} unidades.")
        
    def retirar_stock(self, codigo, cantidad):
        """
        Retira cantidad de un producto.
        TODO:
        - Verificar que producto existe (ProductoNoEncontrado)
        - Verificar que hay suficiente stock (StockInsuficiente)
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(codigo)
            
        producto = self.productos[codigo]
        stock_actual = producto["cantidad"]
        
        if cantidad > stock_actual:
            raise StockInsuficiente(codigo, cantidad, stock_actual)
            
        producto["cantidad"] -= cantidad
        print(f"INFO: Retiradas {cantidad} unidades de '{producto['nombre']}'. Stock restante: {producto['cantidad']}.")
        
    def obtener_producto(self, codigo):
        """
        Obtiene información de un producto.
        TODO:
        - Lanzar ProductoNoEncontrado si no existe
        """
        if codigo not in self.productos:
            raise ProductoNoEncontrado(codigo)
        
        return self.productos[codigo]

# Prueba tu implementación:
inventario = Inventario()
print("\nPruebas funcionales:")
inventario.agregar_producto("001", "Laptop", 10)
inventario.agregar_producto("002", "Mouse", 20)
print(f"Producto 001: {inventario.obtener_producto('001')}")
inventario.retirar_stock("001", 5)

print("\nPruebas de error (manejando las excepciones personalizadas):")
try:
    inventario.agregar_producto("001", "Tablet", 5) # Existente
except ProductoExistente as e:
    print(f"ERROR: {e}")

try:
    inventario.retirar_stock("003", 1) # No encontrado
except ProductoNoEncontrado as e:
    print(f"ERROR: {e}")

try:
    inventario.retirar_stock("001", 10) # Stock insuficiente (queda 5, pide 10)
except StockInsuficiente as e:
    print(f"ERROR: {e}")

print("¿Completado? [Sí/No]: Sí")


# ===========================================================================
# Reflexión Final
# ===========================================================================
print("\n" + "=" * 70)
print(" REFLEXIÓN")
print("=" * 70 + "\n")

print("Después de completar estos ejercicios, reflexiona:")
print()
print("1. ¿Qué tipos de excepciones usaste más frecuentemente?")
print("   - Mayormente `ValueError`, `TypeError`, `ZeroDivisionError`, y `FileNotFoundError`.")
print("2. ¿Cuándo decidiste crear excepciones personalizadas?")
print("   - Las creé cuando las excepciones estándar de Python no representaban con precisión un error específico del *dominio* del negocio (ej. `SaldoInsuficienteError` en lugar de un simple `ValueError`).")
print("3. ¿Qué patrón de manejo de excepciones te pareció más útil?")
print("   - El patrón `try-except-else-finally` fue muy útil para las operaciones con archivos, ya que asegura que la limpieza (`finally`) se realice independientemente del éxito o fracaso, y el `else` ejecuta lógica que *solo* debe ocurrir si no hubo error.")
print("4. ¿Cómo ayuda el manejo de excepciones a la experiencia del usuario?")
print("   - Permite que el programa falle con gracia, proporcionando mensajes de error *útiles* y *específicos* al usuario (ej. 'El archivo no fue encontrado' en lugar de un críptico traceback). También evita la pérdida de datos y asegura que los recursos (archivos) se cierren correctamente.")
print("5. ¿Qué errores comunes evitaste con el manejo apropiado?")
print("   - Evité fallas catastróficas por `ZeroDivisionError`, errores silenciosos (`except desnudo`), y mensajes de error genéricos que no ayudan a la depuración o al usuario.")
print()
print("Discute tus respuestas con un compañero o con el profesor.")
print()

print("=" * 70)
print(" ¡EJERCICIOS COMPLETADOS!")
print("=" * 70)
