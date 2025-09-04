import numpy as np
class PilaSecuencial:
    __tope : int
    __tamaño : int
    __lista: list
    __cantidad:int 
    def __init__(self,tamaño):
        self.__lista = np.empty(tamaño,dtype=int)
        self.__tope = -1
        self.__tamaño = tamaño
        self.__cantidad = 1
    def GetTope(self):
        return self.__tope
    def GetCantidad(self):
        return self.__cantidad
    def llena(self):
        return self.__cantidad==self.__tamaño
    def vacia(self):
        return self.__tope ==-1
    def insertar(self,elem:int):
        if self.llena():
            print("La pilase Lleno")
        else:
            self.__tope += 1
            self.__lista[self.__tope]=elem
            self.__cantidad+=1
    def suprimir(self):
        if self.vacia():
            print("La Lista esta vacia")
        else:
            borrado = self.__lista[self.__tope]
            self.__tope-=1
            return borrado
class Celda:
    __elem:int
    __sig:None
    def __init__(self,elem:int):
        self.__elem = elem
        self.__sig = None
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
    def getElem(self):
        return self.__elem
class PilaEncadenada:
    __cabeza : Celda
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def insertar(self,elem:int):
        aux  = Celda(elem)
        aux.setSig(self.__cabeza)
        self.__cabeza = aux
        self.__cant += 1
    def suprimir(self):
        self.__cant-=1
        borrado = self.__cabeza.getElem()
        self.__cabeza = self.__cabeza.getSig()
        return borrado
    def vacia(self):
        return self.__cant == 0
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    def cantidad(self):
        return self.__cant
    def tope(self):
        return self.__cabeza.getElem()
    def grafico(self):
        aux= self.__cabeza
        while aux!=None:
            print(aux.getElem())
            aux = aux.getSig()
if __name__ == '__main__':
    pilaS = PilaSecuencial(30)
    # pilaE = PilaEncadenada()
    pilaS.insertar(1)
    pilaS.insertar(2)
    pilaS.insertar(3)
    pilaS.insertar(4)
    pilaS.insertar("a")
    while pilaS.vacia() != True:
        pilaS.suprimir()

    # print("Pila Encadenada")
    # pilaE.insertar(1)
    # pilaE.insertar(2)
    # pilaE.insertar(3)
    # pilaE.insertar(4)
    # pilaE.insertar(5)
    # pilaE.recorrer()
    # pilaE.suprimir()
    # pilaE.recorrer()

    