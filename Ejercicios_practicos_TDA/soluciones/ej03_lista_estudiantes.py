class ListaEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, nombre):
        self.estudiantes.append(nombre)

    def eliminar(self, nombre):
        if nombre in self.estudiantes:
            self.estudiantes.remove(nombre)
            print("Estudiante eliminado")
        else:
            print("No encontrado")

    def buscar(self, nombre):
        if nombre in self.estudiantes:
            return "Estudiante encontrado"
        return "Estudiante no encontrado"


# Prueba
lista = ListaEstudiantes()

lista.agregar("Cristian")
lista.agregar("Jose")

print(lista.buscar("Jose"))

lista.eliminar("Jose")

print(lista.estudiantes)