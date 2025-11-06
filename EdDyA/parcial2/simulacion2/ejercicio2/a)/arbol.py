# pyrefly: ignore  # unsupported-operation
from nodo import Nodo
class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def vacia(self):
        return self.__raiz == None

    def insertar(self, nodo, valor):
        if self.vacia() == True:
            self.__raiz = Nodo(valor)
        elif valor == nodo.getElem():
            print("\nEl valor ya existe en el arbol")
        elif valor < nodo.getElem():
            if nodo.getIzq():
                self.insertar(nodo.getIzq(), valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self.insertar(nodo.getDer(), valor)
            else:
                nodo.setDer(Nodo(valor))
    def preorden(self, nodo, n):
        if nodo:
            if self.nivel(nodo, nodo.getElem(), 0) == n:
                print(nodo.getElem(), end=' ')
            self.preorden(nodo.getIzq(), n-1)
            self.preorden(nodo.getDer(), n-1)

    def nivel(self, nodo, valor, nivel):
        if nodo == None:
            nivel = 0
        elif valor < nodo.getElem():
            nivel += 1
            nivel = self.nivel(nodo.getIzq(), valor, nivel)
        elif valor > nodo.getElem():
            nivel += 1
            nivel = self.nivel(nodo.getDer(), valor, nivel)
        else:
            nivel += 1
        return nivel
if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 3)
    arbol.insertar(arbol.getRaiz(), 7)
    arbol.insertar(arbol.getRaiz(), 2)
    arbol.insertar(arbol.getRaiz(), 4)
    arbol.insertar(arbol.getRaiz(), 6)
    arbol.insertar(arbol.getRaiz(), 8)
    n = int(input("Ingrese el nivel a imprimir: "))
    arbol.preorden(arbol.getRaiz(), n)
