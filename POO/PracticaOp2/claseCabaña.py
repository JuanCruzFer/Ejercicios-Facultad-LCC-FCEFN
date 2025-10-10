class  Cabaña:
    __numero: int
    __cant_hab: int 
    __cant_camasG: int
    __cant_camasC: int 
    __Imp: float
    
    def __init__(self,num,hab,camas_G,camas_C,Imp):
        self.__numero = num
        self.__cant_hab = hab
        self.__cant_camasG = int(camas_G)
        self.__cant_camasC = int(camas_C)
        self.__Imp = float(Imp)    
        
    def __str__(self):
        return f"numero: {self.__numero} cant_hab: {self.__cant_hab} cant_camasG: {self.__cant_camasG} cant_camasC: {self.__cant_camasC} Imp: {self.__Imp}\n"
    
    def getnum(self):
        return self.__numero
    
    def gethab(self):
        return self.__cant_hab
    
    def getcamas_G(self):
        return self.__cant_camasG
    
    def getcamas_C(self):
        return self.__cant_camasC
    
    def getImp(self):
        return self.__Imp
    
    def capacidad(self):
        return (self.__cant_camasG * 2) + self.__cant_camasC

    def __ge__(self, other):
        if isinstance(other, int):
            return self.capacidad() >= other
        
        