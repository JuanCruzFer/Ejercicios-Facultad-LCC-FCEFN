import numpy as np
class Digrafo:
    __nodos: int
    __matriz: np.ndarray    
    def __init__(self, n):
        self.__nodos = n
        self.__matriz = np.zeros((n, n), dtype=int)
    def agregarArista(self, origen, destino):
        if self.__matriz[origen][destino] == 0:
            self.__matriz[origen][destino] = 1
            print(f"\nse agrego la arista de {origen} a {destino}")
        else:
            print(f"\nla arista de {origen} a {destino} ya existe")
    def mostrar(self):
        print("\nmatriz de adyacencia:")
        print(self.__matriz)

grafo = Digrafo(4)
grafo.agregarArista(0, 1)
grafo.agregarArista(0, 2)
grafo.agregarArista(1, 2)
grafo.agregarArista(2, 0)
grafo.agregarArista(2, 3)
grafo.agregarArista(3, 3)
grafo.mostrar()
