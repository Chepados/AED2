from NodoCola import NodoCola

class Cola:
    def __init__(self):
        self.__tamanio = 0
        self.__primero = None
        self.__ultimo = None

    def longitud(self):
        return self.__tamanio

    def vacia(self):
        return self.__tamanio == 0

    def encolar(self, elem):
        nodo = NodoCola(elem) # creamos el nuevo elemento introduciendo elem en la propiedad valor
        if not self.vacia(): # si la cola no esta vacia
            self.__ultimo.set_siguiente(nodo) # enlazamos el campo siguiente del ultimo elemento con el nuevo
        else:
            self.__primero= nodo # si esta vacia ponemos al primero apuntando al nuevo elemento
        self.__ultimo = nodo # ponemos ultimo apuntando al nuevo elemento
        self.__tamanio= self.__tamanio +1 #incrementamos el tamaño

    def desencolar(self):
        elemento = None
        if not self.vacia():
            elemento= self.__primero.get_valor() # a elemento le asignamos el primer elemento
            self.__primero = self.__primero.get_siguiente() # hacemos que primero apunte al segundo elemento
            self.__tamanio = self.__tamanio -1 #decrementamos el tamaño
            if self.vacia():
                self.__ultimo = None #si se queda vacia el ultimo debe apuntar a None
        return elemento










