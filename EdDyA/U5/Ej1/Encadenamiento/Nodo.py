class Nodo:
    __clave: object
    __sig: object

    def __init__(self, clave):
        self.__clave = clave
        self.__sig = None
    
    def getClave(self):
        return self.__clave
    
    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig
    