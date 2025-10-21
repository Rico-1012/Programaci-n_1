
#!/usr/bin/env python3
"""
ESTRUCTURAS CONDICIONALES CONFUSAS - Versión Interactiva
Este código demuestra errores comunes y confusiones con estructuras condicionales en Python.
Optimización: Simplificación de funciones de utilidad y limpieza de código.
"""
import os

# --- Funciones de Utilidad Optimizadas ---
def limpiar_pantalla():
    """Limpia la pantalla de la terminal (más conciso)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter(mensaje="Presiona Enter para continuar..."):
    """Espera a que el usuario presione Enter"""
    input(f"\n{mensaje}")

def mostrar_titulo(texto):
    """Muestra un título formateado"""
    separador = "=" * 70
    print(f"\n{separador}")
    print(texto.center(70))
    print(f"{separador}\n")

def mostrar_seccion(texto):
    """Muestra un encabezado de sección"""
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50)

def ejecutar_codigo_y_mostrar(codigo_str, variables=None):
    """Ejecuta un bloque de código y captura la salida si es posible."""
    if variables is None:
        variables = globals()
    
    # Prepara un entorno para la ejecución del código
    temp_globals = variables.copy()
    temp_locals = {}
    
    # El código interactivo usa print() directamente, lo ejecutamos tal cual
    exec(codigo_str, temp_globals, temp_locals)


# --- Inicio del programa interactivo ---
limpiar_pantalla()
mostrar_titulo("ESTRUCTURAS CONDICIONALES EN PYTHON - Sesión Interactiva")

print("Bienvenidos a la exploración interactiva de estructuras condicionales.")
print("Iremos descubriendo conceptos a través de ejemplos confusos.")
print("Participa activamente respondiendo a las preguntas y predicciones.")
esperar_enter()

# ===========================================================================
# Ejercicio 1: Confusión con indentación
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 1: INDENTACIÓN EN CONDICIONALES")

codigo_ej1 = """
edad = 17
if edad < 18:
    print("Eres menor de edad")
    print("No puedes entrar")
print("Verificación completada")
"""
mostrar_seccion("Analiza este código:")
print(codigo_ej1)

mostrar_seccion("PREDICCIÓN:")
print("Discute con tu compañero: ¿Qué líneas se ejecutarán si edad = 17?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO REAL:")
exec(codigo_ej1)

mostrar_seccion("REFLEXIÓN:")
print("¿Coincidió con tu predicción?")
print("¿Qué líneas forman parte del bloque if y cuáles no?")
print("¿Qué determina si una línea es parte del bloque if?")
print("""
---
EXPLICACIÓN:
- Las líneas que forman parte del bloque `if` son las que están **indentadas** (con espacios o tabulaciones) a la derecha del `if:`.
- La **indentación** (el nivel de espacios) es lo que determina si una línea pertenece o no al bloque de código de una estructura condicional.
- `print("Verificación completada")` se ejecuta siempre porque no está indentada.
---
""")
esperar_enter()

mostrar_seccion("EXPERIMENTO:")
print("Ahora probemos con edad = 19")
esperar_enter("Presiona Enter para ejecutar con edad = 19...")

codigo_ej1_b = """
edad = 19
if edad < 18:
    print("Eres menor de edad")
    print("No puedes entrar")
print("Verificación completada")
"""
print("\nRESULTADO CON edad = 19:")
exec(codigo_ej1_b)

esperar_enter()

# ===========================================================================
# Ejercicio 2: Confusión con operador de asignación vs. comparación
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 2: ASIGNACIÓN VS COMPARACIÓN")

codigo_ej2 = """
x = 5
if x = 10:
    print("x es igual a 10")
else:
    print("x no es igual a 10")
"""
mostrar_seccion("Analiza este código:")
print(codigo_ej2.replace("if x = 10:", "if x = 10:  # ERROR DE SINTAXIS A PROPÓSITO"))

mostrar_seccion("PREDICCIÓN:")
print("¿Este código funcionará? ¿Qué resultado tendría?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para intentar ejecutar...")

print("\nRESULTADO:")
print("SyntaxError: invalid syntax")
print("Python no permite usar '=' (asignación) en una condición.")
print("El operador de comparación correcto es '==' (igualdad).")

mostrar_seccion("REFLEXIÓN:")
print("¿Cuál es la diferencia entre = y == en Python?")
print("¿Qué pasaría si corrigiéramos el código usando == en lugar de =?")
print("""
---
EXPLICACIÓN:
- **`=`** es el operador de **asignación** (establece un valor a una variable).
- **`==`** es el operador de **comparación** (pregunta si dos valores son iguales).
- Al corregir el código con `x == 10`, se evaluaría `False` (ya que `x` es 5), y se ejecutaría la rama `else` imprimiendo: "x no es igual a 10".
---
""")
esperar_enter("Presiona Enter para ver el código corregido...")

print("\nCÓDIGO CORREGIDO:")
x = 5
if x == 10:
    print("x es igual a 10")
else:
    print("x no es igual a 10")

esperar_enter()

# ===========================================================================
# Ejercicio 3: Confusión con valores como condiciones
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 3: VALORES COMO CONDICIONES")

codigo_ej3 = """
valores = [0, 1, "", "texto", [], [1, 2], None, True, False]

for valor in valores:
    if valor:
        print(f"{repr(valor)} se evalúa como True")
    else:
        print(f"{repr(valor)} se evalúa como False")
"""

mostrar_seccion("Analiza este código:")
print(codigo_ej3)

mostrar_seccion("PREDICCIÓN:")
print("¿Cuáles de estos valores crees que se evaluarán como True y cuáles como False?")
esperar_enter("Cuando tengas tus predicciones, presiona Enter para ver los resultados...")

print("\nRESULTADO REAL:")
# Ejecución directa del bloque
valores = [0, 1, "", "texto", [], [1, 2], None, True, False]
for valor in valores:
    if valor:
        print(f"{repr(valor)} se evalúa como True")
    else:
        print(f"{repr(valor)} se evalúa como False")


mostrar_seccion("REFLEXIÓN:")
print("¿Puedes identificar un patrón sobre qué valores se consideran True/False?")
print("¿Qué tienen en común los valores que se evalúan como False?")
print("""
---
EXPLICACIÓN:
- Los valores que se evalúan como **False (Falsy)** son: `0` (cero numérico), `None`, `False`, y colecciones **vacías** (ej. `""`, `[]`, `{}`, `()`).
- Cualquier otro valor se considera **True (Truthy)**.
- El patrón es que los valores Falsy representan la **ausencia de valor** o un **valor numérico cero**.
---
""")
esperar_enter()

# ===========================================================================
# Ejercicio 4: Confusión con múltiples condiciones anidadas
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 4: ANIDACIÓN DE CONDICIONALES")

codigo_ej4 = """
edad = 16
tiene_permiso = True

if edad < 18:
    if tiene_permiso:
        print("Es menor de edad pero tiene permiso")
    else:
        print("Es menor de edad y no tiene permiso")
else:
    print("Es mayor de edad")
    if not tiene_permiso:
        print("Pero no tiene permiso")
"""
mostrar_seccion("Analiza este código confuso:")
print(codigo_ej4)

mostrar_seccion("PREDICCIÓN:")
print("Con edad = 16 y tiene_permiso = True, ¿qué mensajes se mostrarán?")
print("¿Y si cambiamos tiene_permiso a False?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO CON edad = 16, tiene_permiso = True:")
# Ejecución directa del bloque
edad = 16
tiene_permiso = True
exec(codigo_ej4)

mostrar_seccion("Ahora probemos con tiene_permiso = False")
esperar_enter("Presiona Enter para ejecutar con tiene_permiso = False...")

print("\nRESULTADO CON edad = 16, tiene_permiso = False:")
# Ejecución directa del bloque
edad = 16
tiene_permiso = False
exec(codigo_ej4)

mostrar_seccion("REFLEXIÓN:")
print("¿Cómo podríamos simplificar este código usando operadores lógicos (and/or)?")
print("""
---
EXPLICACIÓN:
- Los operadores lógicos (`and`, `or`) permiten combinar condiciones para evitar anidaciones profundas.
- La versión simplificada usa `and` para el primer caso (`if edad < 18 and tiene_permiso:`), haciendo el código más plano y legible.
---
""")
esperar_enter("Presiona Enter para ver una versión simplificada...")

print("\nVERSIÓN SIMPLIFICADA:")
edad = 16 # Usamos el valor de la prueba anterior
if edad < 18 and tiene_permiso:
    print("Es menor de edad pero tiene permiso")
elif edad < 18:
    print("Es menor de edad y no tiene permiso")
elif not tiene_permiso:
    print("Es mayor de edad pero no tiene permiso")
else:
    print("Es mayor de edad y tiene permiso")

esperar_enter()

# ===========================================================================
# Ejercicio 5: Confusión con el orden de condiciones
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 5: ORDEN DE CONDICIONES")

codigo_ej5 = """
nota = 85

if nota >= 60:
    print("Aprobado")
elif nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Notable")
else:
    print("Suspenso")
"""
mostrar_seccion("Analiza este código confuso:")
print(codigo_ej5)

mostrar_seccion("PREDICCIÓN:")
print("Con nota = 85, ¿qué mensaje se mostrará?")
print("¿Y con nota = 95?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO CON nota = 85:")
nota = 85
exec(codigo_ej5)

mostrar_seccion("Ahora probemos con nota = 95")
esperar_enter("Presiona Enter para ejecutar con nota = 95...")

print("\nRESULTADO CON nota = 95:")
nota = 95
exec(codigo_ej5)

mostrar_seccion("REFLEXIÓN:")
print("¿Por qué no se muestra 'Sobresaliente' incluso cuando la nota es 95?")
print("¿Cómo influye el orden de las condiciones en el resultado?")
print("""
---
EXPLICACIÓN:
- El código se ejecuta desde el primer `if` y se detiene en la **primera condición** que sea **verdadera**.
- Como `nota >= 60` es verdadera para 85 y 95, el código imprime "Aprobado" y **nunca evalúa** las condiciones más específicas siguientes.
- Para rangos de valores, es crucial ordenar las condiciones de **más específica/estricta a menos específica/general** (ej. de 90+ a 60+).
---
""")
esperar_enter("Presiona Enter para ver el código corregido...")

print("\nCÓDIGO CORREGIDO:")
nota = 95 # Usamos el valor de la prueba anterior
if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Notable")
elif nota >= 60:
    print("Aprobado")
else:
    print("Suspenso")

mostrar_seccion("MINI DESAFÍO:")
print("Modifica este código para verificar tres rangos de edad:")
print("- Niños: 0-12 años")
print("- Adolescentes: 13-17 años")
print("- Adultos: 18 o más años")
esperar_enter()

# ===========================================================================
# Ejercicio 6: Confusión con el operador ternario
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 6: OPERADOR TERNARIO")

codigo_ej6 = """
edad = 20
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"estado: {estado}")

# Intento incorrecto de ternario múltiple (confuso)
nivel = "Niño" if edad < 13 else "Adolescente" if edad < 18 else "Adulto"
print(f"nivel: {nivel}")
"""
mostrar_seccion("Analiza este código:")
print(codigo_ej6)

mostrar_seccion("PREDICCIÓN:")
print("¿Qué valores tendrán las variables 'estado' y 'nivel'?")
print("¿Es correcta la sintaxis del segundo caso (nivel)?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
# Ejecución directa del bloque
edad = 20
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"estado: {estado}")
nivel = "Niño" if edad < 13 else "Adolescente" if edad < 18 else "Adulto"
print(f"nivel: {nivel}")

mostrar_seccion("REFLEXIÓN:")
print("El segundo ejemplo con múltiples condiciones funciona, pero:")
print("1. ¿Es fácil de leer?")
print("2. ¿Cómo se evalúa?")
print("3. ¿Cuándo es preferible usar if-elif-else tradicional?")
print("""
---
EXPLICACIÓN:
1. No es fácil de leer. Los ternarios anidados son complejos y oscurecen la intención del código.
2. Se evalúa como: [Valor_True] **if** [Condición] **else** [Siguiente_Ternario/Valor_False].
3. Es preferible usar `if-elif-else` tradicional en cuanto se necesita **más de una condición** (más de un `else`), ya que la legibilidad se deteriora rápidamente con el ternario anidado.
---
""")
esperar_enter()

# ===========================================================================
# Ejercicio 7: Confusión con is vs. ==
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("EJERCICIO 7: OPERADORES IS VS. ==")

codigo_ej7 = """
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")
print(f"a is b: {a is b}")
print(f"a == c: {a == c}")
print(f"a is c: {a is c}")
"""
mostrar_seccion("Analiza este código:")
print(codigo_ej7)

mostrar_seccion("PREDICCIÓN:")
print("¿Qué resultados esperarías de las cuatro comparaciones?")
print("¿Cuál es la diferencia entre '==' e 'is' en Python?")
esperar_enter("Cuando tengas tu predicción, presiona Enter para ver el resultado...")

print("\nRESULTADO:")
# Ejecución directa del bloque
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")
print(f"a == c: {a == c}")
print(f"a is c: {a is c}")

mostrar_seccion("REFLEXIÓN:")
print("¿Por qué 'a == b' es True pero 'a is b' es False?")
print("¿Cuándo deberías usar 'is' y cuándo deberías usar '=='?")
print("¿Por qué es especialmente importante entender esto para 'None'?")
print("""
---
EXPLICACIÓN:
- **`==`** comprueba la **igualdad de valor** (el contenido de los objetos).
- **`is`** comprueba la **identidad** (si los objetos son la misma instancia en memoria).
- `a == b` es `True` porque ambas listas tienen el mismo contenido. `a is b` es `False` porque son dos listas diferentes creadas en distintas ubicaciones de memoria.
- Usa **`==`** para comparar valores (ej. números, cadenas, listas).
- Usa **`is`** para verificar si dos variables apuntan al mismo objeto, especialmente para singletons como **`None`** (se recomienda usar `x is None`).
---
""")
esperar_enter()

print("\nEJEMPLO CON None:")
x = None
print(f"x is None: {x is None}")
print(f"x == None: {x == None}")
print("\nAunque ambos funcionan, 'is None' es la forma pythónica correcta.")

esperar_enter()

# ===========================================================================
# Cierre
# ===========================================================================
limpiar_pantalla()
mostrar_titulo("CONCLUSIÓN DE LA EXPLORACIÓN INTERACTIVA")

print("""
Hemos explorado conceptos confusos sobre estructuras condicionales en Python:

1. Indentación y bloques de código
2. Operadores de asignación (=) vs. comparación (==)
3. Evaluación de valores como condiciones (truthy/falsy)
4. Condicionales anidados vs. operadores lógicos
5. Importancia del orden en condiciones encadenadas
6. El operador ternario y sus limitaciones
7. Diferencia entre igualdad (==) e identidad (is)

A continuación, trabajaremos con los ejercicios prácticos para
aplicar estos conceptos de forma correcta y elegante.
""")

esperar_enter("Presiona Enter para finalizar...")

limpiar_pantalla()
print("Gracias por participar en la exploración de estructuras condicionales.")
