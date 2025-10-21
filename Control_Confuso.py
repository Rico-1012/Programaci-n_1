#!/usr/bin/env python
"""
ESTRUCTURAS DE CONTROL CONFUSAS - Versión Interactiva
Este código demuestra errores comunes y confusiones con estructuras de control en Python.
Los estudiantes pueden interactuar con cada ejemplo, predecir resultados y aprender activamente.
"""
import os
import time

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")

def mostrar_titulo(texto):
    """Muestra un título formateado"""
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")

def mostrar_seccion(texto):
    """Muestra un encabezado de sección"""
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)

# Inicio del programa interactivo
limpiar_pantalla()
mostrar_titulo("ESTRUCTURAS DE CONTROL EN PYTHON - Sesión Interactiva")

print("Bienvenidos a la exploración interactiva de estructuras de control.")
print("Descubriremos conceptos a través de ejemplos confusos.")
print("Participa activamente respondiendo a las preguntas y predicciones.")
esperar_enter()

# ===========================================================================
# Ejercicio 1: Modificación de una lista mientras se itera
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 1: MODIFICACIÓN DURANTE ITERACIÓN")

mostrar_seccion("Analiza este código:")
print("""
numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")

# Intento de eliminar números pares durante la iteración
for numero in numeros:
    if numero % 2 == 0:  # Si es par
        numeros.remove(numero)

print(f"Lista después del bucle: {numeros}")
""")

mostrar_seccion("PREDICCIÓN:")
print("¿Qué resultado esperas después de ejecutar este código?")
print("¿Crees que todos los números pares serán eliminados?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

# Ejecutar el código
numeros = [1, 2, 3, 4, 5]
print(f"\nResultado - Lista original: {numeros}")

# Código problemático a propósito
for numero in numeros:
    if numero % 2 == 0:  # Si es par
        numeros.remove(numero)

print(f"Resultado - Lista después del bucle: {numeros}")

mostrar_seccion("REFLEXIÓN:")
print("¿Coincidió con tu predicción?")
print("¿Por qué no se eliminaron todos los números pares?")
print("¿Qué sucede cuando modificamos la lista mientras la recorremos?")
print("""
---
EXPLICACIÓN:
- Al eliminar un elemento, los índices de la lista se desplazan. El bucle `for`
  salta la posición del siguiente elemento, causando que se omita la revisión.
- Modificar la colección durante la iteración es una mala práctica que interfiere
  con el índice interno del bucle, llevando a resultados inconsistentes.
---
""")
esperar_enter()

mostrar_seccion("EXPERIMENTO:")
print("Intenta este enfoque alternativo:")
print("""
numeros = [1, 2, 3, 4, 5]
numeros_filtrados = [num for num in numeros if num % 2 != 0]
# o también: numeros_filtrados = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Lista filtrada: {numeros_filtrados}")
""")

# Demostración del enfoque correcto
numeros = [1, 2, 3, 4, 5]
numeros_filtrados = [num for num in numeros if num % 2 != 0]
print(f"\nResultado correcto: {numeros_filtrados}")

esperar_enter()

# ===========================================================================
# Ejercicio 2: Confusión con range()
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 2: CONFUSIÓN CON RANGE()")

mostrar_seccion("Analiza este código:")
print("""
# Intento de imprimir números del 1 al 10
print("Usando range(10):")
for i in range(10):
    print(i, end=" ")

print("\\n\\nUsando range(1, 10):")
for i in range(1, 10):
    print(i, end=" ")
""")

mostrar_seccion("PREDICCIÓN:")
print("¿Qué números se imprimirán en cada caso?")
print("¿Ambos bucles imprimirán del 1 al 10?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

# Ejecutar el código
print("\nRESULTADO:")
print("Usando range(10):")
for i in range(10):
    print(i, end=" ")

print("\n\nUsando range(1, 10):")
for i in range(1, 10):
    print(i, end=" ")

mostrar_seccion("REFLEXIÓN:")
print("¿Cuál es la diferencia entre range(10) y range(1, 10)?")
print("¿Cómo funcionan los parámetros de range(inicio, fin, paso)?")
print("¿Cómo obtendrías exactamente los números del 1 al 10?")
print("""
---
EXPLICACIÓN:
- `range(10)` genera de 0 a 9. `range(1, 10)` genera de 1 a 9. El valor final es exclusivo.
- Los parámetros son: **inicio** (incluido), **fin** (excluido) y **paso** (incremento/decremento).
- Para obtener del 1 al 10, se debe usar `range(1, 11)`.
---
""")
esperar_enter()

print("\nPara obtener exactamente del 1 al 10:")
for i in range(1, 11):  # El valor final no se incluye, por eso 11
    print(i, end=" ")
print()

esperar_enter()

# ===========================================================================
# Ejercicio 3: Bucle while infinito
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 3: BUCLE WHILE INFINITO")

mostrar_seccion("Analiza este código:")
print("""
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    # Olvidamos incrementar el contador
""")

mostrar_seccion("PREDICCIÓN:")
print("¿Qué pasará cuando se ejecute este código?")
print("¿El bucle terminará en algún momento?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
print("Este código crearía un bucle infinito porque el contador nunca cambia.")
print("El código correcto debería incluir: contador += 1")

mostrar_seccion("REFLEXIÓN:")
print("¿Por qué es importante actualizar la condición de un bucle while?")
print("¿Qué diferencias hay entre bucles for y while?")
print("¿En qué situaciones es preferible usar un bucle while en lugar de for?")
print("""
---
EXPLICACIÓN:
- Es crucial actualizar la condición para que eventualmente se vuelva `False` y
  el bucle termine. Si la condición siempre es `True`, el bucle es infinito.
- `for` se usa cuando el número de iteraciones es conocido o se itera sobre una colección.
- `while` se usa cuando el número de iteraciones es indeterminado y se basa en
  una condición (ej. esperar la entrada correcta de un usuario).
---
""")
esperar_enter()

mostrar_seccion("EXPERIMENTO:")
print("Veamos la versión corregida:")
print("""
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # No olvidamos incrementar el contador
""")

# Ejecutar código corregido
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementamos correctamente

esperar_enter()

# ===========================================================================
# Ejercicio 4: Confusión con break vs. continue
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 4: BREAK VS. CONTINUE")

mostrar_seccion("Analiza estos dos códigos:")
print("""
print("Código 1 (usando break):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saliendo del bucle.")
        break
    print(f"Procesando número {i}")

print("\\nCódigo 2 (usando continue):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saltando a la siguiente iteración.")
        continue
    print(f"Procesando número {i}")
""")

mostrar_seccion("PREDICCIÓN:")
print("¿Cuál será la diferencia en la salida de ambos códigos?")
print("¿Qué números se procesarán en cada caso?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
print("Código 1 (usando break):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saliendo del bucle.")
        break
    print(f"Procesando número {i}")

print("\nCódigo 2 (usando continue):")
for i in range(1, 10):
    if i == 5:
        print(f"Encontré el {i}. Saltando a la siguiente iteración.")
        continue
    print(f"Procesando número {i}")

mostrar_seccion("REFLEXIÓN:")
print("¿Qué diferencia hay entre break y continue?")
print("¿En qué situaciones usarías cada uno?")
print("¿Qué sucede con el código después del bucle en ambos casos?")
print("""
---
EXPLICACIÓN:
- **`break`** detiene el bucle completamente y sale. **`continue`** salta solo la
  iteración actual y pasa a la siguiente.
- `break` se usa para salir del bucle cuando se encuentra el objetivo (ej. una búsqueda).
- `continue` se usa para ignorar elementos no deseados o que no cumplen un requisito.
- En ambos casos, el código que está inmediatamente después del bucle se ejecuta.
---
""")
esperar_enter()

# ===========================================================================
# Ejercicio 5: Bucles anidados y confusión con break
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 5: BUCLES ANIDADOS Y BREAK")

mostrar_seccion("Analiza este código:")
print("""
print("Buscando combinación en matriz:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

objetivo = 6
encontrado = False

for fila in matriz:
    for elemento in fila:
        print(f"Verificando: {elemento}")
        if elemento == objetivo:
            print(f"¡Encontrado {objetivo}!")
            encontrado = True
            break  # ¿Este break sale de ambos bucles?
    
    print("Fin de la fila")

print(f"Búsqueda terminada. Encontrado: {encontrado}")
""")

mostrar_seccion("PREDICCIÓN:")
print("¿El break interno saldrá de ambos bucles o solo del bucle interno?")
print("¿Cuántas filas se procesarán?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

objetivo = 6
encontrado = False

for fila in matriz:
    for elemento in fila:
        print(f"Verificando: {elemento}")
        if elemento == objetivo:
            print(f"¡Encontrado {objetivo}!")
            encontrado = True
            break  # Solo sale del bucle interno
    
    print("Fin de la fila")

print(f"Búsqueda terminada. Encontrado: {encontrado}")

mostrar_seccion("REFLEXIÓN:")
print("¿El break solo afecta al bucle más cercano donde se encuentra?")
print("¿Cómo podrías salir de ambos bucles a la vez en Python?")
print("¿Qué estrategias hay para controlar bucles anidados?")
print("""
---
EXPLICACIÓN:
- Sí, `break` solo afecta al bucle inmediato donde se encuentra (el bucle interno).
- Para salir de ambos, se debe usar una **variable de bandera** (`encontrado = True`)
  en el bucle interno y luego añadir una comprobación `if encontrado: break` en el
  bucle externo.
- Otra estrategia es encapsular la búsqueda en una **función** y usar `return` para
  terminar la ejecución al encontrar el objetivo.
---
""")
esperar_enter()

mostrar_seccion("EXPERIMENTO:")
print("Una forma de salir de ambos bucles:")
print("""
encontrado = False
for fila in matriz:
    for elemento in fila:
        if elemento == objetivo:
            encontrado = True
            break
    if encontrado:  # Si encontramos el elemento, también salimos del bucle externo
        break
""")

esperar_enter()

# ===========================================================================
# Ejercicio 6: Comprensiones de lista vs bucles tradicionales
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 6: COMPRENSIONES VS. BUCLES TRADICIONALES")

mostrar_seccion("Analiza estos dos códigos:")
print("""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Método 1: Bucle tradicional")
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num ** 2)
print(f"Cuadrados de números pares: {pares}")

print("\\nMétodo 2: Comprensión de lista")
pares = [num ** 2 for num in numeros if num % 2 == 0]
print(f"Cuadrados de números pares: {pares}")
""")

mostrar_seccion("PREDICCIÓN:")
print("¿Ambos métodos producirán el mismo resultado?")
print("¿Cuáles son las ventajas y desventajas de cada enfoque?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Método 1: Bucle tradicional")
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num ** 2)
print(f"Cuadrados de números pares: {pares}")

print("\nMétodo 2: Comprensión de lista")
pares = [num ** 2 for num in numeros if num % 2 == 0]
print(f"Cuadrados de números pares: {pares}")

mostrar_seccion("REFLEXIÓN:")
print("¿Cuándo es preferible usar comprensiones de listas?")
print("¿Cuándo es mejor usar bucles tradicionales?")
print("¿Cómo afecta cada enfoque a la legibilidad del código?")
print("""
---
EXPLICACIÓN:
- Las comprensiones son preferibles para crear **listas nuevas** con lógica de
  filtrado/transformación simple; son más compactas, declarativas y eficientes.
- Los bucles son mejores cuando la lógica es **compleja**, requiere **múltiples
  pasos**, o si se necesita usar `break` o `continue`.
- Las comprensiones mejoran la legibilidad para tareas sencillas. Los bucles
  mejoran la legibilidad para tareas complejas al ser más explícitos.
---
""")
esperar_enter()

# ===========================================================================
# Cierre
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("CONCLUSIÓN DE LA EXPLORACIÓN INTERACTIVA")

print("""
Hemos explorado conceptos confusos sobre estructuras de control en Python:

1. Modificación de colecciones durante la iteración
2. Funcionamiento y parámetros de range()
3. Bucles infinitos y actualización de condiciones
4. Diferencias entre break y continue
5. Comportamiento de break en bucles anidados
6. Comprensiones de lista vs. bucles tradicionales

Continúa con los ejercicios prácticos para aplicar estos conceptos.
""")

esperar_enter("Presiona Enter para finalizar...")

limpiar_pantalla()
print("Gracias por participar en la exploración de estructuras de control.")
