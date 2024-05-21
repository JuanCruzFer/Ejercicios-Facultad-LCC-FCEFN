import csv
import numpy as np
from claseCancha import Cancha

class gestorCancha:
    def __init__(self):
        self.__lista= np.array([],'object')

    def cargar_canchas(self):
        with open("Canchas.csv",newline='') as archi:
            reader= csv.reader(archi, delimiter=';')
            next (reader)
            for row in reader:
                unaCancha=Cancha(*row)
                self.__lista= np.append(self.__lista,unaCancha)
            print("\nCanchas Cargadas")
    
    def mostrar_canchas(self):
        for canchas in self.__lista:
            print(canchas)
    

    def calcularImp(self,idd):
        total= 0.0
        for canchas in self.__lista:
            if canchas.getIdd()==idd:
                total+=canchas.getImp()
        return (total)
    
    def CantMin(self,idd,GA):
        i= 0
        band= False

        while i < len(self.__lista) and not band:
            if self.__lista[i].getIdd()==idd:
                band= True
            else:
                i+=1
        if band:
            total=GA.totalMin(idd)
            print(f"\nMinutos totales: {total}")
                
            