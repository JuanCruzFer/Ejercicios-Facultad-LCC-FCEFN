class Nodo:
    __elem : int
    __tel : int
    __sig : None
    def __init__(self,elem : int, tel : int)->None:
        self.__elem = elem
        self.__tel = tel
        self.__sig = None
    def getElem(self)->int:
        return self.__elem
    def setElem(self,elem)->None:
        self.__elem = elem
    def getTel(self)-> None:
        return self.__tel
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig
