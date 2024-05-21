class Alquiler:
    __nom_persona: str
    __id_c: str
    __hora: str
    __Min: str
    __duracion: int

    def __init__(self,nom,idd,hora,min,duracion):
        self.__nom_persona= nom
        self.__id_c= idd
        self.__hora= hora
        self.__Min= min
        self.__duracion= int(duracion)
    
    def getId(self):
        return self.__id_c
    
    def getHora(self):
        return self.__hora
    
    def getMin(self):
        return self.__Min
    
    def getDur(self):
        return self.__duracion

    def __str__(self):
        return(f"{self.__nom_persona}  {self.__id_c}   {self.__hora}:{self.__Min}   {self.__duracion}")
    


    def __gt__(self,other):
        if self.__hora== other.__hora:
            return self.__Min > other.__Min
        else:
            return self.__hora > other.__hora
    
    