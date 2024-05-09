class Persona:
    def __init__(self, nombre, telefono, dirección):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = dirección

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def getDireccion(self):
        return self.__direccion
    def setDireccion(self, direccion):
        self.__direccion = direccion

    def mostrarPersona(self):
        return ""+ self.getNombre() + "(" + self.getTelefono() + ")" + self.getDireccion()
