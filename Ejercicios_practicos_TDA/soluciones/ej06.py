# Cristian Marquez Arcila
# Valery Torres

pila = []

pila.append(1)
print(pila.pop())

class Pila:
    def __init__(self):
        self.datos = []
    def push(self, x):
        self.datos.append(x)
        
p = Pila()
p.push(5)
print(p.datos)