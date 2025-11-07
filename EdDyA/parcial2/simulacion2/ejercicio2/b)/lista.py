#pyrefly: ignore # unsupported-operation
from nodo import Nodo
class ListaEncadenada:
    __cabeza : Nodo
    def __init__(self):
        self.__cabeza = None
        
    def getCab(self): return self.__cabeza

    def insertar(self, valor:int):
        nuevo = Nodo(valor)
        actual = self.__cabeza
        repetido = False

        if not actual:
            self.__cabeza = nuevo
        else:
            while actual.getSig() != None:
                if actual.getElem() == valor:
                    repetido = True
                actual = actual.getSig()
            if actual.getElem() == valor:
                repetido = True
                print(f"el elemento {valor} no se inserto ya esta en la tabla")
            if not repetido:
                actual.setSig(nuevo)