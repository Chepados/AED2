from Grafos import GrafoMA
from Persona import Persona
from copy import deepcopy

class AmigosETSISI:
    def __init__(self, n, contactos):
        self.__red = GrafoMA(n, False)
        self.__contactos = contactos

    def getNumPersonas(self):
        return self.__red.getNumVertices()

    # MÉTODOS PARA INSERTAR Y ELIMINAR relaciones(ARISTAS)

    #  método que inserta una relación de amistad directa (una arista en el grafo)
    def insertaRelacion(self, o, d):
        self.__red.insertarArista(o, d)

    #  método que elimina una relación de amistad directa (una arista en el grafo)
    def eliminaRelacion(self, o, d):
        self.__red.eliminaArista(o, d)

    #  método que indica si existe una relación de amistad directa (una arista en el grafo)
    def existeRelacion(self, o, d):
        return self.__red.existeArista(o, d)

    #  Metodo que compara dos cadenas que representan dos nombres ignorando mayusculas y minusculas
    def nombresIguales(self, cad1, cad2):
        return cad1.lower() == cad2.lower()

    #  devuelve un vector de visitados igual al número de personas con todos los elementos  a False
    def __iniciavisitados(self):
        visitados = []
        for i in range(self.getNumPersonas()):
            visitados.append(False)
        return visitados

    #  encuentra la posición asociada a un nombres.txt de persona en la tabla de contactos que
    #  además se corresponde con el vertice que le representa en el grafo

    def devuelvePosNombre(self, nombre):
        resul = -1
        i = 0
        encontrado = False
        while i< len(self.__contactos) and not encontrado:
            encontrado = self.nombresIguales(nombre, self.__contactos[i].getNombre())
            if not encontrado:
                i= i+1
            else: resul = i
        return resul

    #  Imprime la Matriz de relaciones por consola
    def imprimeRelaciones(self):
        print("Contenido de la matriz")
        print("  ", end=" ")
        for i in range(self.getNumPersonas()):
            if i < 10:
                print(" " + str(i) + " ", end=" ")
            else:
                print(str(i) + " ", end=" ")
        print()
        for i in range(self.getNumPersonas()):
            if i < 10:
                print(" " + str(i), end=" ")
            else:
                print(str(i), end=" ")
            for j in range(self.getNumPersonas()):
                if (self.existeRelacion(i, j)):
                    print(" S ", end=" ")
                else:
                    print(" N ", end=" ")
            print()

    #  Imprime la información de la red y la matriz de Relaciones por consola
    def mostrarRed(self):
        print("Existen "+ str(self.getNumPersonas()) +  " contactos: ")
        i=0
        for nombre in self.__contactos:
            print((str(i)+ ": " + nombre.getNombre()))
            i= i+1
        self.imprimeRelaciones()
        print()


    #  Métodos a completar

    #  Apartado 2.2 primer método
    def contarGrupos(self):
        counter = 0
        visitados = self.__iniciavisitados()
        for i in range(self.getNumPersonas()):
            if not visitados[i]:
                self.__red.recorridoenProfundidad(i,visitados)
                counter += 1
        return counter

        #  Apartado 2.2 Segundo método
    def mostrarAmigos(self, nombre):
        pos_nombre = self.devuelvePosNombre(nombre)
        lista_adyacentes = []
        assert self.getNumPersonas() > pos_nombre > -1 , "El nombre no se encuentra en la base de datos"
        for i in range(self.getNumPersonas()):
            if self.existeRelacion(pos_nombre,i):
                lista_adyacentes.append(i)

        print(f"Los amigos directos de {nombre} son:")
        for a in lista_adyacentes:
            print(self.__contactos[a].getNombre())

        #  Apartado 2.2 Tercer método
    def sonDelMismoGrupo(self, persona1, persona2):
        persona1 = self.devuelvePosNombre(persona1.getNombre())
        persona2 = self.devuelvePosNombre(persona2.getNombre())
        if self.__red.verticeEnRango(persona1) and self.__red.verticeEnRango(persona2):
            visitados = self.__iniciavisitados()
            self.__red.recorridoenProfundidad(persona1,visitados)
        return visitados[persona2]

        #comprobar si esta en la tabla de contactos

        #  Apartado 2.2 cuarto método
    def mostrarMiembrosGrupo(self, persona1):
        pos_nombre = self.devuelvePosNombre(persona1.getNombre())
        if self.__red.verticeEnRango(pos_nombre):
            visitados = self.__iniciavisitados()
            self.__red.recorridoenProfundidad(pos_nombre, visitados)
            miembros_grupo = [i for i,e in enumerate(visitados) if e == True]

            print(f"Los miembros del grupo de {persona1.getNombre()}")
            for m in miembros_grupo:
                print(self.__contactos[m].getNombre())
        else:
            raise ValueError("La persona introducida no se encuentra en la lista de contactos")

