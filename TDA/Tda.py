from collections import deque

# Implementación 1 con lista
class PilaLista:
    def __init__(self):
        self.datos = []

    def push(self, elemento):
        self.datos.append(elemento)

    def pop(self):
        if len(self.datos) > 0:
            return self.datos.pop()
        return "La pila está vacía"


# Implementación 2 con deque
class PilaDeque:
    def __init__(self):
        self.datos = deque()

    def push(self, elemento):
        self.datos.append(elemento)

    def pop(self):
        if len(self.datos) > 0:
            return self.datos.pop()
        return "La pila está vacía"


# Prueba de PilaLista
p1 = PilaLista()

p1.push(10)
p1.push(20)

print("Pila con lista:", p1.pop())


# Prueba de PilaDeque
p2 = PilaDeque()

p2.push(30)
p2.push(40)

print("Pila con deque:", p2.pop())