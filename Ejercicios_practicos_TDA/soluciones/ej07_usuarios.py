usuarios = []

def crear(nombre):
    usuarios.append(nombre)

def eliminar(nombre):
    if nombre in usuarios:
        usuarios.remove(nombre)

def actualizar(viejo, nuevo):
    if viejo in usuarios:
        indice = usuarios.index(viejo)
        usuarios[indice] = nuevo