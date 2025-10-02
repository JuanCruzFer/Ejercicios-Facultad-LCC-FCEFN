from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None

    def vacio(self):
        return self.__raiz == None

    def insertar(self, value):
        if not self.__raiz:
            self.__raiz = Nodo(value)
        else:
            self._insertar(self.__raiz, value)
    def _insertar(self, nodo, elemento):
        if self.__raiz == None:
            self.__raiz = Nodo(elemento)
        
        if elemento < self.__raiz.getElem():
            if nodo.getIzq() == None:
                nodo.setIzq(Nodo(elemento))
            else:
                self._insertar(nodo.getIzq(), elemento)
        else:
            if nodo.getDer() == None:
                nodo.setDer(Nodo(elemento))
            else:
                self._insertar(nodo.getDer(), elemento)

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado

    def suprimir(self, value):
        self._suprimir(self.__raiz, value)

    def _suprimir(self, nodo, elem):
        if not nodo:
            return None
        elif elem < nodo.getElem():
            nodo.setIzq(self._suprimir(nodo.getIzq(), elem))
        elif elem > nodo.getElem():
            nodo.setDer(self._suprimir(nodo.getDer(), elem))
        else:
            if self.grado(nodo) == 0:
                return None
            if self.grado(nodo) == 1:
                return nodo.getDer() if nodo.getDer() else nodo.getIzq()
            if self.grado(nodo) == 2:
                maximo = nodo.getIzq()
                while maximo.getDer() != None:
                    maximo = maximo.getDer()
                nodo.setElem(self._suprimir(nodo.getIzq(), maximo.getElem()))
        return nodo
    def preorden(self):
        self._preorden(self.__raiz)
    
    def _preorden(self, nodo):
        if nodo:
            print(f"{nodo.getElem()}")
            self._preorden(nodo.getIzq())
            self._preorden(nodo.getDer())


if __name__ == '__main__':
    arbol = Arbol()

    arbol.insertar(2)
    arbol.insertar(5)
    arbol.insertar(3)
    
    arbol.suprimir(5)
    arbol.preorden()


