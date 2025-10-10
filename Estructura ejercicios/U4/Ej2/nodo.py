class Nodo:
    __elem: int
    __izq: None
    __der: None

    def __init__(self,elem: int):
        self.__elem = elem
        self.__izq = None
        self.__der = None

    def getIzq(self):
        return self.__izq
    def setIzq(self,izq):
        self.__izq = izq
    def getDer(self):
        return self.__der
    def setDer(self, der):
        self.__der = der
    
    def getElem(self):
        return self.__elem