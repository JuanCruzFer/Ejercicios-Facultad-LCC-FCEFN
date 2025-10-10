class Nodo:
    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__sig = None

    def getTiempo(self):
        return self.__tiempo
    
    def setTiempo(self, tiempo):
        self.__tiempo = tiempo

    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig


