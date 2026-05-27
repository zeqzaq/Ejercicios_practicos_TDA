class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return "La pila está vacía"

    def peek(self):
        if len(self.elementos) > 0:
            return self.elementos[-1]
        return "La pila está vacía"


# Prueba
pila = Pila()

pila.push(10)
pila.push(20)
pila.push(30)

print("Elemento superior:", pila.peek())
print("Elemento eliminado:", pila.pop())
print("Pila actual:", pila.elementos)