from ast import main
from os import name
from nodo import Nodo

class Arbol:
    __raiz: None
    __nodo: Nodo
    def __init__(self):
        self.__raiz = None
        self.__nodo = Nodo
    
    def vacio(self):
        return True
    def insertar(self, elemento):
        if self.vacio():
            self.__raiz = Nodo(elemento)
        elif elemento < self.__nodo.getElem():
            if self.__nodo.getIzq == None:
                self.__nodo.setIzq(Nodo(elemento))
            else:
                self.insertar(self.__nodo.getIzq(), elemento)
        else:
            if self.__nodo.getDer == None:
                self.__nodo.setDer(Nodo(elemento))
            else:
                self.insertar(self.__nodo.getDer(), elemento)

    def preorden(self):
        if not self.vacio():
            print(f"{self.__raiz}")
            self.preorden(self.__nodo.getIzq())
            self.preorden(self.__nodo.getDer())

if __name__ == '__main__':
    arbol = Arbol()

    arbol.insertar(2)
    arbol.preorden()

