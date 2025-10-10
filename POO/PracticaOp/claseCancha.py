class Cancha:
    __id: str
    __tipo_p: str
    __importe: float

    def __init__(self,id,tipo,imp):
        self.__id= id
        self.__tipo_p= tipo
        self.__importe= float(imp)
    
    def getIdd(self):
        return self.__id
    
    def getTipo(self):
        return self.__tipo_p
    
    def getImp(self):
        return self.__importe
    

    def __str__(self):
        return(f"{self.__id}  {self.__tipo_p}   {self.__importe}")