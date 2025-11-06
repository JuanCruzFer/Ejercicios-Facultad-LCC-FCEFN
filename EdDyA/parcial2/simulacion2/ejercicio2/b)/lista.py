#pyrefly: ignore #missing-import
from nodo import Nodo
class ListaEncadenada:
    __cabeza : Nodo
    __cant : int
    def __init__(self) -> None:
        self.__cabeza = None
        self.__cant = 0
    def getCabeza(self):
        return self.__cabeza
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:int):
        nuevo = Nodo(elem)
        nuevo.setSig(self.__cabeza)
        self.__cabeza = nuevo
        self.__cant += 1
    def suprimir(self,posicion:int):
        if 0 <= posicion <= self.__cant:
            if not self.vacia():
                anterior = None
                actual = self.__cabeza
                for _ in range(posicion):
                    anterior = actual
                    actual = anterior.getSig()
                if anterior:
                    anterior.setSig(actual.getSig())
                else:
                    self.__cabeza = actual.getSig()
                self.__cant-=1
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    def buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and aux.getElem() != elemento:
            aux = aux.getSig()
        if aux:
            encontrado = True
        return encontrado
LE = ListaEncadenada()