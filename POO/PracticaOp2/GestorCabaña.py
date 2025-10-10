from claseCabaña import Cabaña
import numpy as np
import csv

#ARREGLO NUMPY CARGAR
class gestorCabaña:
        def __init__(self):
           self.__lista= np.array([], 'object')
  
        def cargarCabaña(self):
            with open('Cabañas.csv', newline='') as archi:
                reader = csv.reader(archi,delimiter=";")
                next(reader)
                for row in reader:
                    unaCabaña= Cabaña(*row)
                    self.__lista= np.append(self.__lista,unaCabaña)
                print("\nCabaña Cargada")
                
        def mostrarCabaña(self):
            for cabaña in self.__lista:
                print(cabaña)


        def mostrarNumC(self, canti, GR):
            print(f"\nCabañas con capacidad igual o mayor a {canti} y sin reservas:")
            for cabaña in self.__lista:
                if cabaña.capacidad() >= canti and not GR.tieneReserva(cabaña.getnum()):
                    print(f"Cabaña {cabaña.getnum()} con capacidad para {cabaña.capacidad()} huéspedes")
        

        def totalImp(self,numC):
            for cabañas in self.__lista:
                if cabañas.getnum()==numC:
                    return cabañas.getImp()
                