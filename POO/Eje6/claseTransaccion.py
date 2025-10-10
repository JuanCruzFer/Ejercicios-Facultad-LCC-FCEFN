class Transaccion:
    __cvu: str
    __nroT: int
    __importe: float
    __tipo: str

    def __init__(self,cvu,nroT,importe,tipo):
        self.__cvu= cvu
        self.__nroT= nroT
        self.__importe= float(importe)
        self.__tipo= tipo

    def getCvu(self):
        return self.__cvu
    
    def getnroT(self):
        return self.__nroT
    
    def getImp(self):
        return self.__importe
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return(f"{self.__cvu}  {self.__nroT}   {self.__importe}  {self.__tipo}")