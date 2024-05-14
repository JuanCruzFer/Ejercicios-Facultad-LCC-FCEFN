class Cuenta:
    __apellido: str
    __nombre: str
    __dni: str
    __telefono: str
    __saldo: float
    __cvu: str
    __porcentaje: float

    def __init__(self,ape,nombre,dni,telefono,saldo,cvu,porcentaje):
        self.__apellido= ape
        self.__nombre= nombre
        self.__dni= dni
        self.__telefono= telefono
        self.__saldo= float(saldo)
        self.__cvu= cvu
        self.__porcentaje= float(porcentaje)
    
    def getApe(self):
        return self.__apellido
    
    def getNom(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getTele(self):
        return self.__telefono
    
    def getSaldo(self):
        return float(self.__saldo)
    
    def setSaldo(self,saldo):
        self.__saldo= saldo
        return self.__saldo
    
    def getCvu(self):
        return self.__cvu
    
    def setPor(self,por):
        self.__porcentaje= por
        return self.__porcentaje
    
    def getPor(self):
        return float(self.__porcentaje)
        
    
    def __str__(self):
        return(f"{self.__apellido} {self.__nombre}   {self.__dni}  {self.__telefono}  {self.__saldo}  {self.__cvu}  {self.__porcentaje}")