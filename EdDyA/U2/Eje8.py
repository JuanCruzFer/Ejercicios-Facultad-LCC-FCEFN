import random

class Nodo:
    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__sig = None

    def getTiempo(self):
        return self.__tiempo
    
    def setTiempo(self, tiempo):
        self.__tiempo = tiempo

    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig

class Cola:
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, tiempo):
        nuevo = Nodo(tiempo)
        if self.vacia():
            self.__pr = nuevo
        else:
            self.__ul.setSig(nuevo)
        self.__ul = nuevo
        self.__cant += 1
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            elem = self.__pr
            self.__pr = self.__pr.getSig()
            self.__cant -= 1
            return elem.getTiempo()
    
    def simularBanco(self, ):
        tiempo_total = 0
        clientes_atendidos = 0
        clientes_sinatender = 0
        promedio_espera = 0
        promedio_espera_sinatender = 0


    if __name__ == "__main__":
        cajeros = [Cola() for _ in range(3)]

        
    
