# Ejercicios Prácticos: Operadores Lógicos

## 📝 Instrucciones

- Resuelve los ejercicios en orden
- Intenta predecir el resultado antes de ejecutar el código
- Verifica tus respuestas con Python
- Si te equivocas, analiza por qué

---

## 🟢 NIVEL 1: Básico (Operadores Fundamentales)

### Ejercicio 1.1: Predice los Resultados
```python
# Evalúa sin ejecutar:
print(True and False)
print(True or False)
print(not True)
print(not False)
```
**Tu predicción**: False, True, False, True
**Resultado real**: False, True, False, True
**Explicación**: 1 - Es falso ya que una de las condiciones es falsa, para ser verdadera tendrian que ser las dos true por el conndicional. 
2 - Es verdadero porque este da a elegir cualquiera de las dos.
3 - Es Falso porque me inidica lo contrario.
4 - Es Verdadero porque me indica lo contrario.

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
False
True
False
True
```
**Explicación**: Aplicación directa de las tablas de verdad para operadores lógicos.
</details>

### Ejercicio 1.2: Operadores Combinados
```python
a, b, c = True, False, True

print(a and b)  # ?
print(a or b)   # ?
print(b or c)   # ?
print(a and c)  # ?
```
**Tus predicciones**: False, True, True, True

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
False
True
True
True
```
**Explicación**: 
- `True and False` = `False`
- `True or False` = `True`
- `False or True` = `True`
- `True and True` = `True`
</details>

### Ejercicio 1.3: Precedencia
```python
a, b, c = True, False, True

print(a and b or c)      # ?
print(a or b and c)      # ?
print(not a or b)        # ?
print(not (a or b))      # ?
```
**Tus predicciones**: True, True, False, False

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
True
True
False
False
```
**Explicación**:
- `a and b or c` = `(True and False) or True` = `False or True` = `True`
- `a or b and c` = `True or (False and True)` = `True or False` = `True` 
- `not a or b` = `not True or False` = `False or False` = `False`
- `not (a or b)` = `not (True or False)` = `not True` = `False`
</details>

### Ejercicio 1.4: Comparaciones y Lógica
```python
x = 5
print(x > 3 and x < 10)  # ?
print(x < 3 or x > 10)   # ?
print(not x > 3)         # ?
```
**Tus predicciones**: True, False , False

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
True
False
False
```
**Explicación**:
- `x > 3 and x < 10` = `5 > 3 and 5 < 10` = `True and True` = `True`
- `x < 3 or x > 10` = `5 < 3 or 5 > 10` = `False or False` = `False`
- `not x > 3` = `not (5 > 3)` = `not True` = `False`
</details>

### Ejercicio 1.5: Comparaciones Encadenadas
```python
x = 5
print(3 < x < 10)        # ?
print(1 <= x <= 3)       # ?
print(10 > x > 3)        # ?
```
**Tus predicciones**: True, False, True

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
True
False
True
```
**Explicación**:
- `3 < x < 10` = `3 < 5 < 10` = `True and True` = `True`
- `1 <= x <= 3` = `1 <= 5 <= 3` = `True and False` = `False`
- `10 > x > 3` = `10 > 5 > 3` = `True and True` = `True`
</details>

---

## 🟡 NIVEL 2: Intermedio (Valores y Cortocircuito)

### Ejercicio 2.1: Valores Retornados
```python
print("hola" and "mundo")  # ?
print("hola" and "")       # ?
print("" and "mundo")      # ?
print("hola" or "mundo")   # ?
print("" or "mundo")       # ?
```
**Tus predicciones**: Mundo, "", "", Hola, Mundo

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
"mundo"
""
""
"hola"
"mundo"
```
**Explicación**:
- `and` retorna el primer valor falsy o el último valor
- `or` retorna el primer valor truthy o el último valor
- `""` es falsy, `"hola"` y `"mundo"` son truthy
</details>

### Ejercicio 2.2: Truthy y Falsy
```python
print(bool(0))          # ?
print(bool(""))         # ?
print(bool([]))         # ?
print(bool([0]))        # ?
print(bool(" "))        # ?
print(bool(None))       # ?
```
**Tus predicciones**: Falso, False, False, True, True, False

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
False
False
False
True
True
False
```
**Explicación**:
- `0`, `""`, `[]`, `None` son valores falsy (evalúan a `False`)
- `[0]` (lista con elementos) y `" "` (cadena no vacía) son truthy
</details>

### Ejercicio 2.3: Evaluación de Cortocircuito

Evalúa qué se imprime:

```python
def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Caso 1
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")

# Caso 2
print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")

# Caso 3
print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")
```

**Tu predicción**: 1- False, 2- False, 3- True


<details>
<summary>Ver Solución</summary>

**Resultado**:
```
Caso 1:
f1 ejecutada
f2 ejecutada
Resultado: False

Caso 2:
f2 ejecutada
Resultado: False

Caso 3:
f1 ejecutada
Resultado: True
```

**Explicación**:
- Caso 1: `f1()` es `True`, por lo que debe evaluar `f2()` también
- Caso 2: `f2()` es `False`, así que no evalúa `f1()` (cortocircuito)
- Caso 3: `f1()` es `True`, así que no evalúa `f2()` (cortocircuito)
</details>

### Ejercicio 2.4: Operadores de Pertenencia
```python
nums = [1, 2, 3, 4, 5]
print(3 in nums)        # ?
print(6 in nums)        # ?
print(6 not in nums)    # ?

word = "Python"
print("P" in word)      # ?
print("p" in word)      # ?
print("th" in word)     # ?
```
**Tus predicciones**: True, False, True, True , False, True

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
True
False
True
True
False
True
```
**Explicación**:
- `in` comprueba si el elemento está en la colección
- `not in` comprueba si el elemento no está en la colección
- Las comparaciones en cadenas son sensibles a mayúsculas/minúsculas
- Subcadenas también funcionan con `in`
</details>

### Ejercicio 2.5: Identidad vs Igualdad
```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # ?
print(lista1 is lista2)  # ?
print(lista1 == lista3)  # ?
print(lista1 is lista3)  # ?
```
**Tus predicciones**: True, False, True, True

<details>
<summary>Ver Solución</summary>

**Resultado**: 
```python
True
False
True
True
```
**Explicación**:
- `==` compara el contenido (valor)
- `is` compara la identidad (referencia en memoria)
- `lista1` y `lista2` tienen el mismo contenido pero son objetos diferentes
- `lista1` y `lista3` son el mismo objeto (misma referencia)
</details>

---

## 🔴 NIVEL 3: Avanzado (Aplicaciones Prácticas)

### Ejercicio 3.1: Validación de Formulario
Implementa la función `validar_datos` que verifica si:
- El nombre tiene entre 2 y 30 caracteres
- El email contiene '@'
- La edad es mayor o igual a 18
- La contraseña tiene al menos 8 caracteres

```python
def validar_datos(nombre, email, edad, password):
    return (nombre and 2 <= len(nombre) <= 30 and
            email and '@' in email and
            edad and edad >= 18 and
            password and len(password) >= 8)     
    

# Pruebas
print(validar_datos("Ana", "ana@email.com", 25, "secreto123"))  # Debe ser True
print(validar_datos("", "no-email", 15, "123"))  # Debe ser False
```

<details>
<summary>Ver Solución</summary>

```python
def validar_datos(nombre, email, edad, password):
    return (nombre and 2 <= len(nombre) <= 30 and
            email and '@' in email and
            edad and edad >= 18 and
            password and len(password) >= 8)
```
</details>

### Ejercicio 3.2: Sistema de Autorización
Implementa un sistema que determine si un usuario puede acceder a un recurso basado en:
- Debe estar autenticado
- Debe ser administrador O tener el permiso específico
- No debe estar en la lista negra

```python
def puede_acceder(usuario, permiso_requerido, lista_negra):
    return (usuario["autenticado"] and
            (usuario["admin"] or permiso_requerido in usuario["permisos"]) and
            usuario["id"] not in lista_negra)

# Usuario ejemplo
admin = {
    "id": 1,
    "autenticado": True,
    "admin": True,
    "permisos": ["leer", "escribir"]
}

usuario_normal = {
    "id": 2,
    "autenticado": True,
    "admin": False,
    "permisos": ["leer"]
}

usuario_bloqueado = {
    "id": 3,
    "autenticado": True,
    "admin": False,
    "permisos": ["leer", "escribir"]
}

lista_negra = [3, 4]

print(puede_acceder(admin, "borrar", lista_negra))  # True
print(puede_acceder(usuario_normal, "leer", lista_negra))  # True
print(puede_acceder(usuario_normal, "escribir", lista_negra))  # False
print(puede_acceder(usuario_bloqueado, "leer", lista_negra))  # False
```

<details>
<summary>Ver Solución</summary>

```python
def puede_acceder(usuario, permiso_requerido, lista_negra):
    return (usuario["autenticado"] and
            (usuario["admin"] or permiso_requerido in usuario["permisos"]) and
            usuario["id"] not in lista_negra)
```
</details>

### Ejercicio 3.3: Acceso Seguro a Diccionario
Implementa una función `obtener_valor_seguro` que retorne:
- El valor de la clave si existe
- Un valor predeterminado si la clave no existe

```python
def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    # Tu código aquí (sin usar .get())
    pass

config = {"timeout": 30, "retries": 3}
print(obtener_valor_seguro(config, "timeout"))  # 30
print(obtener_valor_seguro(config, "cache"))  # None
print(obtener_valor_seguro(config, "cache", 60))  # 60
```

<details>
<summary>Ver Solución</summary>

```python
def obtener_valor_seguro(diccionario, clave, predeterminado=None):
    return diccionario[clave] if clave in diccionario else predeterminado
```
</details>

### Ejercicio 3.4: Filtrar Lista
Escribe una función para filtrar una lista de productos según criterios:
- Precio dentro de un rango (min y max)
- Opcionalmente filtrar por categoría
- Solo productos disponibles

```python
def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    return [
        p for p in productos
        if precio_min <= p["precio"] <= precio_max and
           p["disponible"] and
           (categoria is None or p["categoria"] == categoria)
    ]



productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica", "disponible": True},
    {"nombre": "Teléfono", "precio": 800, "categoria": "Electrónica", "disponible": False},
    {"nombre": "Libro", "precio": 15, "categoria": "Libros", "disponible": True},
    {"nombre": "Audífonos", "precio": 200, "categoria": "Electrónica", "disponible": True},
]

print(filtrar_productos(productos, 0, 500))
print(filtrar_productos(productos, 100, 1000, "Electrónica"))
```

<details>
<summary>Ver Solución</summary>

```python
def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    return [
        p for p in productos
        if precio_min <= p["precio"] <= precio_max and
           p["disponible"] and
           (categoria is None or p["categoria"] == categoria)
    ]
```
</details>

### Ejercicio 3.5: Evaluación de Riesgo
Implementa un sistema de evaluación de riesgo crediticio:

```python
def evaluar_riesgo(cliente):
    """
    Evalúa si un cliente tiene bajo riesgo crediticio.
    
    Criterios:
    - Score crediticio alto (>700) O
    - Ingreso anual >50000 Y historial > 2 años O
    - Cliente VIP Y sin deudas pendientes
    """


def evaluar_riesgo(cliente):                                                                        
    return (cliente["score_crediticio"] > 700 or
            (cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2) or
            (cliente["vip"] and not cliente["deudas_pendientes"]))




cliente1 = {
    "nombre": "Ana García",
    "score_crediticio": 720,
    "ingreso_anual": 45000,
    "años_historial": 3,
    "vip": False,
    "deudas_pendientes": False
}

cliente2 = {
    "nombre": "Luis Pérez",
    "score_crediticio": 680,
    "ingreso_anual": 60000,
    "años_historial": 4,
    "vip": False,
    "deudas_pendientes": False
}

cliente3 = {
    "nombre": "Carmen Ruiz",
    "score_crediticio": 690,
    "ingreso_anual": 30000,
    "años_historial": 1,
    "vip": True,
    "deudas_pendientes": False
}

print(evaluar_riesgo(cliente1))  # True
print(evaluar_riesgo(cliente2))  # True
print(evaluar_riesgo(cliente3))  # True
```

<details>
<summary>Ver Solución</summary>

```python
def evaluar_riesgo(cliente):                                                                        
    return (cliente["score_crediticio"] > 700 or
            (cliente["ingreso_anual"] > 50000 and cliente["años_historial"] > 2) or
            (cliente["vip"] and not cliente["deudas_pendientes"]))
```
</details>

---

## 🎯 PROYECTO FINAL: Sistema de Control de Acceso

### Descripción
Crea un sistema de control de acceso para una plataforma digital que determine qué recursos puede ver un usuario.

### Requisitos Mínimos
1. Función que verifica si un usuario puede acceder a un recurso
2. Múltiples reglas de acceso
3. Manejo de diferentes tipos de usuarios
4. Justificación para cada decisión

```python
# Ejemplo de usuarios y recursos
usuarios = [
    {
        "id": 1,
        "nombre": "Admin",
        "roles": ["admin"],
        "permisos": ["leer", "escribir", "eliminar"],
        "plan": "premium",
        "activo": True,
        "edad": 35
    },
    {
        "id": 2,
        "nombre": "Usuario Regular",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "basico",
        "activo": True,
        "edad": 17
    },
    # Añade más usuarios...
]

recursos = [
    {
        "id": 1,
        "nombre": "Panel Admin",
        "requiere_rol": ["admin"],
        "requiere_permiso": "eliminar",
        "solo_adultos": False
    },
    {
        "id": 2,
        "nombre": "Contenido Premium",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": True,
        "solo_adultos": False
    },
    {
        "id": 3,
        "nombre": "Contenido para Adultos",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": False,
        "solo_adultos": True
    },
    
]
s
# Tu implementación aquí
def puede_acceder_recurso(usuario, recurso):
    if not usuario["activo"]:
        return False
    
    if "necesita_rol" in recurso and not any(rol in recurso["necesita_rol"] for rol in usuario["roles"]):
        return False


    if "necesota_permiso" in recurso and recurso["necesita_permiso"] not in usuario["permisos"]:
        return False
    

    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False
    
  
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False
    
    return True

# Sistema para probar todas las combinaciones
def probar_accesos():
    for usuario in usuarios:
        for recurso in recursos:
            acceso = puede_acceder_recurso(usuario, recurso)
            print(f"Usuario: {usuario['nombre']}, Recurso: {recurso['nombre']}, Acceso: {acceso}")
```

### Solución Básica

<details>
<summary>Ver Solución Básica</summary>

```python
def puede_acceder_recurso(usuario, recurso):
    """Determina si un usuario puede acceder a un recurso."""
    
    # Verificar si el usuario está activo
    if not usuario["activo"]:
        return False
    
    # Verificar roles
    if "requiere_rol" in recurso and not any(rol in recurso["requiere_rol"] for rol in usuario["roles"]):
        return False
    
    # Verificar permisos específicos
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False
    
    # Verificar plan premium
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False
    
    # Verificar restricción de edad
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False
    
    # Si pasa todas las verificaciones, puede acceder
    return True
```
</details>

### Solución Avanzada (Con explicaciones)

<details>
<summary>Ver Solución Avanzada</summary>

```python
def puede_acceder_recurso(usuario, recurso):
    """
    Determina si un usuario puede acceder a un recurso específico.
    
    Args:
        usuario (dict): Diccionario con datos del usuario
        recurso (dict): Diccionario con datos del recurso
        
    Returns:
        tuple: (acceso, motivo) donde acceso es un booleano y motivo explica la decisión
    """
    # Verificar si el usuario está activo
    if not usuario["activo"]:
        return False, "Usuario inactivo"
    
    # Verificar roles permitidos
    if "requiere_rol" in recurso:
        tiene_rol = any(rol in recurso["requiere_rol"] for rol in usuario["roles"])
        if not tiene_rol:
            return False, f"Requiere rol: {recurso['requiere_rol']}"
    
    # Verificar permisos específicos
    if "requiere_permiso" in recurso and recurso["requiere_permiso"] not in usuario["permisos"]:
        return False, f"Falta permiso: {recurso['requiere_permiso']}"
    
    # Verificar si es contenido premium
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return False, "Requiere plan premium"
    
    # Verificar restricción de edad
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return False, "Solo para mayores de 18 años"
    
    # Si pasa todas las verificaciones, puede acceder
    return True, "Acceso permitido"

def probar_accesos():
    """Prueba todas las combinaciones de usuario y recurso."""
    resultados = []
    
    for usuario in usuarios:
        print(f"\nUsuario: {usuario['nombre']} ({usuario['roles'][0]})")
        print("-" * 50)
        
        for recurso in recursos:
            acceso, motivo = puede_acceder_recurso(usuario, recurso)
            print(f"Recurso: {recurso['nombre']}")
            print(f"Acceso: {'✅ PERMITIDO' if acceso else '❌ DENEGADO'}")
            print(f"Motivo: {motivo}")
            print()
            
            resultados.append({
                "usuario": usuario["nombre"],
                "recurso": recurso["nombre"],
                "acceso": acceso,
                "motivo": motivo
            })
    
    return resultados
```
</details>

---

## 📊 Ejercicios de Debugging

### Debug 1: Encuentra el Error
```python
# Este código debería verificar si el usuario tiene permisos
def verificar_permisos(usuario, accion):
    if usuario["permisos"] and accion in usuario["permisos"]:
        return True
    else:
        return False

# Prueba
usuario = {"id": 1, "nombre": "Juan"}
print(verificar_permisos(usuario, "leer"))
```

**¿Qué está mal?** El error se encuentra en 'Usuario', ya que no tiene la clave de permisos.

<details>
<summary>Ver Solución</summary>

**Error**: `KeyError` porque el diccionario `usuario` no tiene la clave "permisos"  

**Correcto**:
```python
def verificar_permisos(usuario, accion):
    return "permisos" in usuario and accion in usuario["permisos"]
```

**Explicación**: El código original intenta acceder a `usuario["permisos"]` sin verificar si existe primero. La solución usa evaluación de cortocircuito para evitar el error.
</details>

### Debug 2: Encuentra el Error
```python
# Este código debería filtrar estudiantes aprobados
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": None},
    {"nombre": "Carmen", "nota": 92}
]

aprobados = [e for e in estudiantes if e["nota"] >= 60]
print(aprobados)
```

**¿Qué está mal?** En la lista estudiantes se ve un diccionario con un valor "nota" : 'none', y en python no es posible comoparar un valor 'none' con un valor de tipo entero.

<details>
<summary>Ver Solución</summary>

**Error**: `TypeError` al comparar `None` con un número en el caso de Luis.

**Correcto**:
```python
aprobados = [e for e in estudiantes if e["nota"] is not None and e["nota"] >= 60]
```

**Explicación**: El código debe verificar primero si la nota existe (no es None) antes de hacer la comparación.
</details>

---

## ✅ Autoevaluación

Marca los ejercicios que completaste correctamente:

### Nivel 1 (Básico)
- [ ] Ejercicio 1.1
- [ ] Ejercicio 1.2
- [ ] Ejercicio 1.3
- [ ] Ejercicio 1.4
- [ ] Ejercicio 1.5

### Nivel 2 (Intermedio)
- [ ] Ejercicio 2.1
- [ ] Ejercicio 2.2
- [ ] Ejercicio 2.3
- [ ] Ejercicio 2.4
- [ ] Ejercicio 2.5

### Nivel 3 (Avanzado)
- [ ] Ejercicio 3.1
- [ ] Ejercicio 3.2
- [ ] Ejercicio 3.3
- [ ] Ejercicio 3.4
- [ ] Ejercicio 3.5

### Proyecto Final
- [ ] Sistema de Control de Acceso

---

## 🎯 Próximos Pasos

Si completaste todos los ejercicios:
1. ✅ Experimenta con combinaciones más complejas
2. ✅ Implementa tus propios sistemas usando operadores lógicos
3. ✅ Optimiza código existente usando estas técnicas
4. ✅ Explora más sobre evaluación de expresiones lógicas

**¡Excelente trabajo! 🚀**
