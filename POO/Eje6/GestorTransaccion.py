import csv
# pyrefly: ignore  # missing-import
from claseTransaccion import Transaccion

class gestorTransaccion:
    def __init__(self):
        self.__lista=[]

    def cargarT_desde_CSV(self):
        with open("Eje6/transaccionesBilletera.csv", newline='') as archi:
            reader= csv.reader(archi,delimiter=';')
            next (reader)
            for row in reader:
                unaTransaccion=Transaccion(*row)
                self.__lista.append(unaTransaccion)
            print ("\n Transacciones cargadas\n")

    def mostrarTra(self):
        for trans in self.__lista:
            print(trans)

    def actualizarSaldo(self,cvu,saldo):
        
        for trans in self.__lista:
            if trans.getCvu() == cvu and trans.getTipo() == 'D':
                saldo -= trans.getImp()
                
            elif trans.getCvu() == cvu and trans.getTipo() == 'C':
                saldo += trans.getImp()
            elif trans.getCvu()!=cvu:
                next
            else:
                print("\nNo se encontro el CVU")
        return saldo
    
