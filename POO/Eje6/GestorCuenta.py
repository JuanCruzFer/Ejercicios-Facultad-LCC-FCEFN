import csv
import numpy as np
# pyrefly: ignore  # missing-import
from claseCuenta import Cuenta

class gestorCuenta:
    
    def __init__(self):
        self.__lista=np.array([],dtype='object')

    def carga_desde_CSV(self):
        with open("Eje6/cuentasBilletera.csv", newline='') as archi:
            reader= csv.reader(archi,delimiter=';')
            next (reader)
            for row in reader:
                unaCuenta= Cuenta(*row)
                self.__lista=np.append(self.__lista,unaCuenta)
            print("Cuenta cargadas\n")

    def mostrarCuenta(self):
        for cuenta in self.__lista:
            print(cuenta)
                
    
    def mostrarDatos(self,dni,GT):
        i=0
        band=False

        while i < len(self.__lista) and not band:
            if self.__lista[i].getDni()==dni:
                band=True
                cvu=self.__lista[i].getCvu()
                saldo=self.__lista[i].getSaldo()
                saldo_actualizado= GT.actualizarSaldo(cvu,saldo)
                print(f"\n {self.__lista[i].getSaldo()}")
                self.__lista[i].setSaldo(saldo_actualizado)
            else:
                i+=1

        if band:
                print(f"\nApellido y Nombre: {self.__lista[i].getApe()} {self.__lista[i].getNom()}    Cvu: {self.__lista[i].getCvu()}    Saldo Actualizado: {self.__lista[i].getSaldo()}")
        
            
    def nuevoPor(self, porcentaje):
        for cuenta in self.__lista:
            cuenta.setPor(porcentaje)
        print(f"\nPorcentaje actualizado para todas las cuentas es: {cuenta.getPor()}")        
    
    def actualizarSaldoPorRendimiento(self, porcentaje_anual):
        porcentaje_diario = porcentaje_anual / 365
        for cuenta in self.__lista:
            rendimiento_diario = cuenta.getSaldo() * (porcentaje_diario / 100)  # Utilizamos el saldo original
            nuevo_saldo = cuenta.getSaldo() + rendimiento_diario
            cuenta.setSaldo(nuevo_saldo)
            print(f"\nSaldo actualizado para las cuentas es de: {round(nuevo_saldo,3)}")

    
    def informarSaldo(self,cvu,GT):
        i=0
        band=False
        
        while i < len(self.__lista) and not band:
            if self.__lista[i].getCvu()==cvu:
                band=True
                print(f"\nSaldo inicial: {self.__lista[i].getSaldo()}")
                saldo_t=GT.actualizarSaldo(cvu,self.__lista[i].getSaldo())
                self.__lista[i].setSaldo(saldo_t)
            else: 
                i+=1
        if band:
            print(f"\n El saldo actualizado de la cuenta con cvu: {self.__lista[i].getCvu()} despues de procesar las transacciones es de: {round(self.__lista[i].getSaldo(),3)}") 
          
    def almacenarDatos(self):
        nuevo_csv="Eje6/transaccionesActualizadas.csv"
        with open(nuevo_csv,'w',newline='') as archi:
            writer= csv.writer(archi)
            for cuentas in self.__lista:
                row=[cuentas.getApe(),cuentas.getNom(),cuentas.getDni(),round(cuentas.getSaldo(),2),cuentas.getCvu()]
                writer.writerow(row)
