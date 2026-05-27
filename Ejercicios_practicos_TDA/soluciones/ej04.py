# Cristian Marquez Arcila
# Valery Torres

lista = []
def agregar (x):
    lista.append(x)

def eliminar(x):
    if x in lista:
        lista.remove(x)

agregar(5)
eliminar(5)
print(lista)#La lista queda vacia ya que eliminamos lo que agregamos