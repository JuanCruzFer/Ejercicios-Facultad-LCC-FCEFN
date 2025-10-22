# pyrefly: ignore  # missing-import
from nodo import Nodo
class PilaEncadenada:
    __cabeza : Nodo
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def insertar(self,elem:int):
        aux  = Nodo(elem)
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

    def chequear_parentesis(self, expresion):
        for i , simbolo in enumerate(expresion, start = 1):
            if simbolo == '(':
                # pyrefly: ignore  # bad-argument-type
                self.insertar(simbolo)
            elif simbolo == ')':
                if self.vacia():
                    print(f"Error en la posicion {i}, No hay par '(' de apertura")
                    return False
                self.suprimir()
            i +=1
        if self.vacia():
            print("Expresion Balanceada\n")
            return True
        else:
            print("Quedaron parentesis sin cerrrar\n")
            return False
                
if __name__ == '__main__':
    PE = PilaEncadenada()

    PE.chequear_parentesis(input("Ingrese una expresion: "))
    PE.recorrer()
