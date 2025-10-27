# pyrefly: ignore  # unsupported-operation
from Eje5 import ColaSec
import math
import numpy as np
import random
class Grafo:
    __nodos: int
    __aristas: int
    __matriz: np.ndarray
    def __init__(self, nodos: int, aristas: int):
        self.__nodos = nodos
        self.__aristas = aristas
        self.__matriz = np.zeros((nodos, nodos), dtype=int)
    def relacionar(self, u, v):
        if u < 0 or u >= self.__nodos or v < 0 or v >= self.__nodos:
            raise ValueError("\nNodos Invalidos")
        self.__matriz[u, v] = 1
        print(f"\nNodos {u} y {v} relacionados")
        self.__matriz[v, u] = 1
        print(f"\nNodos {v} y {u} relacionados")

    def adyacentes(self, u):
        for v in range(self.__nodos):
            if self.__matriz[u, v] == 1:
                    print(f"{v}", end=" ")
    def camino(self, o, d):
        if self.__matriz[o, d] == 1:
                print(f"\nExiste un camino directo entre {o} y {d}")
                return
        for k in range(self.__nodos):
            if self.__matriz[o, k] == 1 and self.__matriz[k, d] == 1:
                print(f"\nExiste un camino de longitud 2: {o} -> {k} -> {d}")
                return
        print(f"\nNo existe camino entre {o} y {d}")
    
    def conexo(self, s):
        distancias = self.bea(s)
        if distancias is None:
            return False
        for distancia in distancias:
            if distancia is None:
                return False
        return True
    
    def bea(self, s):
        cola = ColaSec(self.__nodos)
        d = [None] * self.__nodos
        for v in range(self.__nodos):
            d[v] = d[v * 0]
        d[s] = d[s * 0]
        cola.insertar(s)
        while not cola.vacia():
            cola.suprimir()
            for u in range(self.__nodos):
                if self.adyacentes(u) and d[u] == None:
                    d[u] = d[v + 1]
                    cola.insertar(u)

    def aciclico(self):
        band = True
        i = 0
        while i < self.__nodos and band:
            if self.camino(i, i):
                band = False
            else:
                i += 1
        return band

    def gradEnt(self, u):
        cont = 0
        for v in range(self.__nodos):
            if self.__matriz[v, u] == 1:
                cont += 1
        print(f"El numero de aristas que llegan a {u} es {cont}")

    def gradSal(self, u):
        cont = 0
        for v in range(self.__nodos):
            if self.__matriz[u, v] == 1:
                cont += 1
        print(f"El numero de aristas que salen de {u} es {cont}")

    def nodoFuente(self, u):
        i = 0
        while i < self.__nodos:
            if self.__matriz[i, u] == 1:
                print(f"El nodo {u} no es fuente")
                return
            i += 1
        print(f"El nodo {u} es fuente")
    
    def nodoSum(self, u):
        i = 0
        while i < self.__nodos:
            if self.__matriz[u, i] == 1:
                print(f"El nodo {u} no es sumidero")
                return
            i += 1
        print(f"El nodo {u} es sumidero")

    def mostrar(self):
        print(f"Matriz de Adyacencia:")
        print(self.__matriz)
        
if __name__ == "__main__":
    grafo = Grafo(5, 5)

    op = -1
    while op != 0:
        print("\nMenu de Opciones")
        print("1. Relacionar")
        print("2. Adyacentes")
        print("3. Camino")
        print("4. Conexo")
        print("5. Mostrar")
        print("6. Aciclico")
        print("7. Grado Entrante")
        print("8. Grado Saliente")
        print("9. Nodo Fuente")
        print("10. Nodo Sumidero")
        print("0. Salir")
        try:
            op = int(input("\nOpcion: "))
            if op == 1:
                try:
                    for i in range(5):
                        for j in range(i + 1, 5):
                            if np.random.rand() < 0.5:
                                grafo.relacionar(i, j)
                except ValueError:
                    print("\nError en la relacion")
            elif op == 2:
                u = int(input("\nNodo: "))
                grafo.adyacentes(u)
            elif op == 3:
                o = int(input("\nNodo Origen: "))
                d = int(input("\nNodo Destino: "))
                grafo.camino(o, d)
            elif op == 4:
                s = int(input("\nNodo Inicial: "))
                conexo = grafo.conexo(s)
                if conexo:
                    print("\nEl grafo es conexo")
                else:
                    print("\nEl grafo no es conexo")
            elif op == 5:
                grafo.mostrar()
            elif op == 6:
                if not grafo.aciclico():
                    print("\nGrafo Aciclico")
                else:
                    print("\nGrafo Aciclico")
            elif op == 7:
                nodo = int(input("\nIngrese nodo U: "))
                grafo.gradEnt(nodo)
            elif op ==8:
                nodo = int(input("\nIngrese nodo U: "))
                grafo.gradSal(nodo)
            elif op == 9:
                nodo = int(input("\nIngrese nodo U: "))
                grafo.nodoFuente(nodo)
            elif op == 10:
                nodo = int(input("\nIngrese nodo U: "))
                grafo.nodoSum(nodo)
            elif op == 0:
                print("\nSaliendo...")
            else:
                print("\nOpcion Invalida")
        except ValueError:
            print("\nOpcion Invalida")
