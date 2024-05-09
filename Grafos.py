from Cola import Cola

class GrafoMA:
    def __init__(self, tamanio, dirigido):
        self.__nVertices= tamanio
        self.__dirigido = dirigido
        self.__nunAristas = 0
        self.__matrizAD =[]
        self.__matrizAD = [[False] * self.__nVertices for _ in range(self.__nVertices)]


    def getDirigido(self):
        return self.__dirigido

    def getNumVertices(self):
        return self.__nVertices

    def verticeEnRango(self, vertice):
        return vertice < self.__nVertices and vertice >= 0

    def numeroAristas(self):
        return self.__nunAristas

    def existeArista(self, origen, destino):
        resul= False
        if self.verticeEnRango(origen) and self.verticeEnRango(destino):
            if self.__matrizAD[origen][destino]:
                resul = True
        else:
            print("Error, los vertices " + origen + ", " + destino + " Están fuera de rango")
        return resul

    def insertarArista(self, origen, destino):
        if self.verticeEnRango(origen) and self.verticeEnRango(destino):
            if ( not self.existeArista(origen, destino)):
                self.__matrizAD[origen][destino]= True
                self.__nunAristas = self.__nunAristas +1
                if not self.getDirigido() and destino != origen:
                    self.__matrizAD[destino][origen] = True
                    self.__nunAristas = self.__nunAristas + 1

            else:
                print("la arista con origen en " + str(origen) + " y destino en " + str(destino) + " ya existe")
        else:
            print("Error, los vertices " + str(origen) + ", " + str(destino) + " Están fuera de rango")

    def eliminaArista(self, origen, destino):
        if self.verticeEnRango(origen) and self.verticeEnRango(destino):
            if ( self.existeArista(origen, destino)):
                self.__matrizAD[origen][destino]= False
                self.__nunAristas = self.__nunAristas -1
                if not self.getDirigido() and destino != origen:
                    self.__matrizAD[destino][origen] = False
                    self.__nunAristas = self.__nunAristas - 1
            else:
                print("la arista con origen en " + str(origen) + " y destino en " + str(destino) + " no existe")
        else:
            print("Error, los vertices " + str(origen) + ", " + str(destino) + " Están fuera de rango")

    def gradoEmtrada(self, v):
        resul = 0
        if self.verticeEnRango(v):
            for ele in range(self.__nVertices):
                if self.__matrizAD[ele][v]:
                    resul = resul + 1
        return resul


    def gradoSalida(self, v):
        resul = 0
        if self.verticeEnRango(v):
            for ele in range(self.__nVertices):
                if self.__matrizAD[v][ele]:
                    resul = resul + 1
        return resul

    def incidencia(self,v):
        resul= 0
        if self.verticeEnRango(v):
            if not self.getDirigido():
                resul = self.gradoEmtrada(v) + self.gradoSalida(v)
            else:
                resul = self.gradoEmtrada(v) - self.gradoSalida(v)
        return resul




    def mostrar(self):
        print("El Grafo tiene una Matriz de ", self.__nVertices, " x ", self.__nVertices )
        if self.getDirigido():
            print("De un Grafo Dirigido")
        else:
            print("De un Grafo No Dirigido")
        for i in range(self.__nVertices):
            for j in range(self.__nVertices):
                 if (self.__matrizAD[i][j]):
                    print(" T ",end="")
                 else:
                    print(" F ", end="")
            print()

    def mostrarAmpliado(self):#imprime la matriz por consola con numeros en las filas y columnas si es menor de 10 vertices
        print("El Grafo tiene una Matriz de ", self.__nVertices, " x ", self.__nVertices )
        if self.getDirigido():
            print("De un Grafo Dirigido")
        else:
            print("De un Grafo No Dirigido")
        if self.__nVertices < 10 :
            print("   ",end="")
            for ele in range(self.__nVertices):
                print("", ele, "",end="")
            print()
        for i in range(self.__nVertices):
            if self.__nVertices < 10:
                print("", i, "", end="")
            for j in range(self.__nVertices):
                if (self.__matrizAD[i][j]):
                    print(" T ", end="")
                else:
                    print(" F ", end="")
            print()

    def __iniciavisitados(self):
        visitados = []
        for i in range(self.__nVertices):
            visitados.append(False)
        return visitados

    def profundidaddesdeV(self, v):#se hace un recorrido en profundidad del grafo a partir del vertice v que pasan como origen.
        if self.verticeEnRango(v):
            # se inicializa el vector de visitados que se utiliza para saber que vertice
            # he visitado ya y no volver a pasar por el(evitando bucles infinitos)
            visitados = self.__iniciavisitados()
            #Se empieza a recorrer desde el vértice v llamando a recorridoEnProfundidad.
            self.recorridoenProfundidad(v,visitados)
            print()

    def recorridoenProfundidad(self, v, visitados):
        visitados[v] = True
        print( v, " ",end="")
        # para cada vertice adyacente desde v
        for i in range(self.__nVertices):
            if self.existeArista(v,i) and not visitados[i]:
                self.recorridoenProfundidad(i,visitados)


    #Para  recorrer todos los vertices del grafo, recorriendo cada componente conexa(GN)
    #o fuertemente conexa(GD) en profundidad a partir de un vertice de la misma.
    def profundidad(self):
        visitados = self.__iniciavisitados()
        #Para cada Vertice para visitar todas las componentes conexas(GN) o fuertemente conexas(GD)
        for i in range(self.__nVertices):
            if not visitados[i]:
                self.recorridoenProfundidad(i,visitados)

# recorrido en profuncidad de una componente conexa de un grafo dirigido
    def recorreProfundidadCadena(self, v, visitados, imprimir):
        visitados[v]=True
        if imprimir:
            print( v, " ", end="")
        for i in range(self.__nVertices):
            if (self.existeArista(v,i) or self.existeArista(i,v)) and not visitados[i]:
                self.recorreProfundidadCadena(i,visitados,imprimir)

    # recorre un grafo en amplitud a partir de un vertice
    def recorridoenAmplituddesdeV(self, v):
        visitados = self.__iniciavisitados()
        self.recorreAmplitud(v, visitados)

    def recorreAmplitud(self, v,  visitados):
        cola = Cola()
        cola.encolar(v)
        visitados[v]= True
        while not cola.vacia():
            ele = cola.desencolar()
            print(ele, " ",end="")
            #encolar los vertices adyacentes desde V
            for i in range(self.__nVertices):
                if self.existeArista(ele,i) and not visitados[i]:
                    cola.encolar(i)
                    visitados[i] = True

    # recorre en amplitud a partir de cada componente del grafo
    def amplitud(self):
        cola = Cola()
        visitados = self.__iniciavisitados()
        # para cada vertice no visitado visitar
        for i in range(self.__nVertices):
            if not visitados[i]:
               self.recorreAmplitud(i, visitados)
        print()

    # funcion que determina si un grafo es conexo
    def esGrafoConexo(self):
        visitados = self.__iniciavisitados()
        if self.getDirigido():
            self.recorreProfundidadCadena(0,visitados,False)
        else:
            self.recorridoenProfundidad(0,visitados)
            print()
        return self.todosVisitados(visitados)

    def todosVisitados(self, visitados):
        ok = True
        ele = 0
        while ele< self.__nVertices and ok:
            ok = visitados[ele]
            ele = ele +1
        return ok


