# pyrefly: ignore  # missing-import
from claseReserva import Reserva
import csv

class gestorReserva:
    def __init__(self):
        self.__lista= []
    
    def cargarReserva(self):
        with open("Reservas.csv", newline='', encoding='utf-8') as archi:
            reader = csv.reader(archi,delimiter=";")
            next (reader)
            for row in reader:
                unaReserva = Reserva(*row)
                self.__lista.append(unaReserva)
            print("\nReserva Cargada")
      
    def mostrarReserva(self):
        for reserva in self.__lista:
            print(reserva)
    
    def tieneReserva(self, num_cabaña):
        for reserva in self.__lista:
            if reserva.getNumC() == num_cabaña:
                return True
        return False


    def listarReservas(self,fecha,GC):
        i= 0 
        band= False
        print(f"\nReservas para la fecha: {fecha}")
        for reservas in self.__lista:
            if reservas.getIni()==fecha:
                print("\nN° de cabaña                 Importe diario    Cantidad días                 Seña                         Importe a cobrar") 
                tot=GC.totalImp(reservas.getNumC())
                cant= reservas.getCantD()
                tot_imp= (tot * cant) - reservas.getImpo()
                print(f"{reservas.getNumC():<30}  {tot:<15}             {reservas.getCantD():<18}  {reservas.getImpo():<20}  {tot_imp:<30}")
                
                  
            

           
           
