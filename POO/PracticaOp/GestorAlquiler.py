import csv
# pyrefly: ignore  # missing-import
from claseAlquiler import Alquiler

class gestorAlquiler:
    def __init__(self):
        self.__lista= []

    def cargar_alquileres(self):
        with open("Alquiler.csv", newline='') as archi:
            reader= csv.reader(archi, delimiter=';')
            next (reader)
            for row in reader:
                unAlquiler= Alquiler(*row)
                self.__lista.append(unAlquiler)
            print("\nAlquileres cargados")
        

    
    def ordenarAlq(self):
        self.__lista= sorted(self.__lista)
        for alquiler in self.__lista:
            print(alquiler)

    def duracionHoras(self,alquiler):
            if alquiler.getDur() != 0:
                horas = alquiler.getDur() / 60
                return horas
            return 0
            

        

    def listarAlquiler(self,GA,GC):
        sum= 0.0
        print("\nHora    Id de Cancha    Duración alquiler    Importe por hora    Importe alquiler ")
        
        for alquiler in self.__lista:
            dur=GA.duracionHoras(alquiler)
            imp=GC.calcularImp(alquiler.getId())/60
            precio_Alq=GC.calcularImp(alquiler.getId())
            sum+=precio_Alq
            
            print(f"\n{alquiler.getHora()}:{alquiler.getMin():<10} {alquiler.getId():<10} {dur:<10} {imp:<10.2f} {precio_Alq}")
        print("                         \nTotal Recaudado: ")
        print(f"{sum:<30}")


    def totalMin(self,idd):
        cant=0
        for alquiler in self.__lista:
            if alquiler.getId()==idd:
                cant+=alquiler.getDur()
        return cant
