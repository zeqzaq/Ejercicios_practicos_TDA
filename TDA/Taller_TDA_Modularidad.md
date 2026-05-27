# Taller – Tipo de Dato Abstracto (TDA) y Modularidad

## Parte 1: Conceptual

### 1. ¿Qué es un Tipo de Dato Abstracto (TDA)?
Es un modelo matemático que define un conjunto de datos y las operaciones que se pueden realizar sobre ellos, ocultando los detalles de implementación. El usuario solo conoce *qué* hace, no *cómo* lo hace.

### 2. ¿Cuál es la diferencia entre TDA e implementación?
El TDA es la **especificación** (qué operaciones se pueden hacer y qué datos se manejan), mientras que la implementación es el **código concreto** que realiza esas operaciones. Un mismo TDA puede tener múltiples implementaciones.

### 3. ¿Por qué se dice que un TDA define el "qué" y no el "cómo"?
Porque el TDA solo especifica la interfaz (operaciones disponibles y su comportamiento), sin detallar la estructura interna ni los algoritmos usados para implementarlas.

### 4. Mencione 3 ejemplos de TDA.
- **Pila (Stack)**: operaciones push, pop, peek, isEmpty.
- **Cola (Queue)**: operaciones enqueue, dequeue, front, isEmpty.
- **Lista (List)**: operaciones insert, delete, search, size.

### 5. ¿Qué es una operación dentro de un TDA?
Es una función que puede realizarse sobre los datos del TDA, definida por su nombre, parámetros, precondiciones y postcondiciones. Ejemplo: en una pila, `push(elemento)` agrega un elemento en la cima.

### 6. ¿Qué relación existe entre estructuras de datos y TDA?
Un TDA es la **abstracción** (qué hace), mientras que la estructura de datos es la **implementación concreta** (cómo lo hace). Por ejemplo, el TDA "pila" puede implementarse con un arreglo o con una lista enlazada.

### 7. ¿Por qué es importante el uso de TDA en programación?
Porque permite separar la interfaz de la implementación, facilitando el mantenimiento, la reutilización del código, y reduciendo la complejidad al permitir trabajar con abstracciones.

### 8. ¿Qué es encapsulamiento en el contexto de TDA?
Es ocultar los detalles internos de implementación y exponer solo una interfaz pública. Los datos internos no son accesibles directamente desde fuera del TDA.

### 9. ¿Qué ventajas ofrece trabajar con abstracción?
- Reduce la complejidad.
- Facilita el mantenimiento.
- Permite reutilizar código.
- Aísla cambios (se puede cambiar la implementación sin afectar a quien usa el TDA).
- Mejora la legibilidad.

### 10. ¿Qué problemas se presentan si no se usa abstracción?
- Código difícil de mantener y modificar.
- Alta dependencia entre componentes.
- Dificultad para reutilizar código.
- Mayor probabilidad de errores al cambiar implementaciones.
- Código más extenso y difícil de entender.

### 11. ¿Qué es modularidad?
Es la técnica de dividir un programa en partes independientes llamadas módulos, cada uno con una responsabilidad bien definida, que se comunican entre sí a través de interfaces.

### 12. ¿Por qué es importante dividir un programa en módulos?
- Facilita el mantenimiento (cambiar un módulo sin afectar otros).
- Permite el trabajo en equipo (cada persona trabaja en un módulo).
- Favorece la reutilización.
- Reduce la complejidad general del sistema.

### 13. ¿Qué es cohesión en un módulo?
Es el grado en que los elementos dentro de un módulo están relacionados entre sí. Un módulo con **alta cohesión** agrupa funciones y datos que tienen un propósito único y bien definido.

### 14. ¿Qué es acoplamiento?
Es el grado de dependencia entre módulos. Un **bajo acoplamiento** significa que los módulos son independientes y se comunican solo a través de interfaces simples, lo cual es deseable.

### 15. ¿Cómo se relaciona la modularidad con el mantenimiento del software?
La modularidad facilita el mantenimiento porque permite modificar, reparar o actualizar un módulo sin afectar al resto del sistema. También facilita encontrar errores y agregar nuevas funcionalidades.

---

## Parte 2: Análisis y Aplicación

### 16. Diseñe un TDA para una pila (stack) indicando sus operaciones.

```
TDA Pila<T>
Operaciones:
  - crear() → Pila
  - push(elemento: T) → void
  - pop() → T
  - peek() → T
  - isEmpty() → booleano
  - size() → entero
```

### 17. Diseñe un TDA para una cola (queue).

```
TDA Cola<T>
Operaciones:
  - crear() → Cola
  - enqueue(elemento: T) → void
  - dequeue() → T
  - front() → T
  - isEmpty() → booleano
  - size() → entero
```

### 18. Diseñe un TDA para un carrito de compras.

```
TDA CarritoCompras
Operaciones:
  - crear() → CarritoCompras
  - agregarProducto(producto: Producto, cantidad: entero) → void
  - eliminarProducto(idProducto: string) → void
  - actualizarCantidad(idProducto: string, nuevaCantidad: entero) → void
  - calcularTotal() → real
  - listarProductos() → lista<Producto>
  - vaciar() → void
  - obtenerCantidadProductos() → entero
```

### 19. Explique cómo se aplicaría modularidad en un sistema de estudiantes.
Se crearían módulos separados: `modulo_estudiantes` (registro, actualización, eliminación), `modulo_cursos` (inscripción, notas), `modulo_pagos` (matrícula, cuotas), `modulo_reportes` (generar reportes). Cada módulo tiene su responsabilidad y se comunican mediante interfaces definidas.

### 20. ¿Qué pasaría si todo el código de un sistema se hace en un solo archivo?
- Sería extremadamente difícil de mantener y entender.
- Cualquier cambio podría afectar todo el sistema.
- Imposible trabajar en equipo de forma eficiente.
- Dificultad para reutilizar código.
- Mayor probabilidad de errores.

### 21. Dé un ejemplo donde el TDA sea independiente de la implementación.
El TDA **Lista** puede implementarse con un arreglo (acceso O(1) por índice pero inserción O(n)) o con una lista enlazada (inserción O(1) pero acceso O(n)). El usuario de la lista no necesita saber cuál se usa.

### 22. ¿Por qué una pila puede implementarse con lista o arreglo?
Porque el TDA Pila solo define las operaciones (push, pop, peek, isEmpty). Tanto un arreglo como una lista enlazada pueden soportar estas operaciones, solo cambia la eficiencia: arreglo tiene capacidad fija, lista enlazada es dinámica.

### 23. Diseñe un módulo para manejar usuarios en un sistema.

```
Módulo: GestionUsuarios
Funciones públicas:
  - registrar(nombre, email, password) → Usuario
  - autenticar(email, password) → booleano
  - actualizarPerfil(idUsuario, datos) → void
  - eliminarUsuario(idUsuario) → void
  - buscarPorEmail(email) → Usuario
Datos privados:
  - lista de usuarios (base de datos o archivo)
```

### 24. ¿Qué ventajas tiene separar funciones en diferentes módulos?
- **Reutilización**: una función puede usarse en varios lugares.
- **Mantenibilidad**: es más fácil encontrar y corregir errores.
- **Legibilidad**: el código es más organizado.
- **Escalabilidad**: es más fácil agregar nuevas funcionalidades.
- **Pruebas**: se pueden probar módulos de forma independiente.

### 25. Explique con un ejemplo la diferencia entre alta cohesión y bajo acoplamiento.

**Alta cohesión**: un módulo `Facturacion` solo contiene funciones relacionadas con facturas (crearFactura, anularFactura, calcularImpuestos). Todo está relacionado con un solo propósito.

**Bajo acoplamiento**: el módulo `Facturacion` se comunica con `Inventario` solo mediante una función `descontarStock(producto, cantidad)`. Si cambia la implementación interna de `Inventario`, `Facturacion` no se ve afectada siempre que la interfaz se mantenga.

---

## Parte 3: Python

### 26. Cree una clase en Python que represente una pila (push y pop).

```python
class Pila:
    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        return self._elementos.pop()

    def peek(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def size(self):
        return len(self._elementos)
```

### 27. Cree una función en Python que represente un módulo para agregar elementos a una lista.

```python
# modulo_listas.py
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def agregar_si_no_existe(lista, elemento):
    if elemento not in lista:
        lista.append(elemento)
    return lista

def agregar_varios(lista, elementos):
    lista.extend(elementos)
    return lista
```

### 28. Cree un ejemplo de modularidad separando funciones en Python.

```python
# archivo: operaciones_matematicas.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# archivo: operaciones_texto.py
def mayusculas(texto):
    return texto.upper()

def minusculas(texto):
    return texto.lower()

# archivo: main.py
import operaciones_matematicas as mat
import operaciones_texto as txt

print(mat.suma(5, 3))
print(txt.mayusculas("hola"))
```

### 29. Explique cómo Python permite implementar un TDA.

Python permite implementar un TDA mediante **clases**. La clase define la interfaz pública (métodos) y encapsula los datos internos (atributos privados con `_` o `__`). El usuario interactúa con los objetos a través de los métodos públicos sin conocer la implementación interna. Además, Python soporta **duck typing** y **protocolos** (como `__len__`, `__iter__`) que permiten definir comportamientos abstractos.

### 30. Escriba un ejemplo donde un mismo TDA tenga dos implementaciones diferentes.

```python
from abc import ABC, abstractmethod

# TDA Pila (interfaz abstracta)
class PilaTDA(ABC):
    @abstractmethod
    def push(self, elemento): pass
    @abstractmethod
    def pop(self): pass
    @abstractmethod
    def esta_vacia(self): pass

# Implementacion 1: con lista de Python
class PilaConLista(PilaTDA):
    def __init__(self):
        self._datos = []
    def push(self, elemento):
        self._datos.append(elemento)
    def pop(self):
        return self._datos.pop()
    def esta_vacia(self):
        return len(self._datos) == 0

# Implementacion 2: con nodos enlazados
class _Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class PilaConListaEnlazada(PilaTDA):
    def __init__(self):
        self._cima = None
        self._tamano = 0
    def push(self, elemento):
        self._cima = _Nodo(elemento, self._cima)
        self._tamano += 1
    def pop(self):
        if self.esta_vacia():
            raise IndexError("Pila vacia")
        valor = self._cima.valor
        self._cima = self._cima.siguiente
        self._tamano -= 1
        return valor
    def esta_vacia(self):
        return self._cima is None

# Uso: ambas implementaciones comparten la misma interfaz
pila1 = PilaConLista()
pila2 = PilaConListaEnlazada()
pila1.push(10)
pila2.push(10)
print(pila1.pop())  # 10
print(pila2.pop())  # 10
```
