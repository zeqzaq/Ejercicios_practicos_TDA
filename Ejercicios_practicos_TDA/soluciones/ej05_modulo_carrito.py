# Cristian Marquez Arcila
# Valery Torres

carrito = []

def agregar_producto(producto):
    carrito.append(producto)

def eliminar_producto(producto):
    if producto in carrito:
        carrito.remove(producto)

def mostrar_carrito():
    return carrito