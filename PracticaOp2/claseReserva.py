class  Reserva:
    __num: str
    __nombre_p: str 
    __num_cab: int
    __inicio: str
    __cant_h: int 
    __cantD: int
    __importe: float
    
    def __init__(self,num,nom_p,num_c,inicio,cant_h,cant_dias,imp):
        self.__num = num
        self.__nombre_p = nom_p
        self.__num_cab = num_c
        self.__inicio= inicio
        self.__cant_h = cant_h
        self.__cantD = int(cant_dias)
        self.__importe= float(imp)    
        
    def __str__(self):
        return f"num: {self.__num} nombre_p: {self.__nombre_p} num_cab: {self.__num_cab} fecha inicio: {self.__inicio} cant_h: {self.__cant_h} cant_dias: {self.__cantD} Importe seña: {self.__importe}\n"
    
    def getNum(self):
        return self.__num
    
    def getNomP(self):
        return self.__nombre_p
    
    def getNumC(self):
        return self.__num_cab
    
    def getCantH(self):
        return self.__cant_h
    
    def getCantD(self):
        return self.__cantD
    
    def getImpo(self):
        return self.__importe
    
    def getIni(self):
        return self.__inicio