class Nodo:
    __elem: int
    __izq: object
    __der: object
    def __init__(self, elem):
        self.__elem = elem
        self.__izq = None
        self.__der = None
    def getElem(self):
        return self.__elem
    def getIzq(self):
        return self.__izq
    def setIzq(self, izq):
        self.__izq = izq
    def getDer(self):
        return self.__der
    def setDer(self, der):
        self.__der = der
    def grado(self):
        grado = 0
        if self.__izq:
            grado += 1
        if self.__der:
            grado += 1
        return grado