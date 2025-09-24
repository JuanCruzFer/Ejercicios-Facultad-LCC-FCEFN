from nodo import Nodo
import random

class Cola:
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0
    
    def getCant(self):
        return self.__cant

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
    
    def simularPensiones(self, simulacion, cajeros):
        reloj = 0
        cajero_1 = 0
        cajero_2 = 0
        tiempo_espera = 0
        cont = 0
        cont1 = 0
        cont2 = 0
        acum_t = 0
        while reloj < simulacion:
            num = random.random()
            if num <= 1/3:
                if cajero_1 == 0 or cajero_2 == 0:
                    cajero_elegido = random.choice([i for i, x in enumerate([cajero_1, cajero_2]) if x == 0])
                    cajeros[cajero_elegido].insertar(reloj)
                else:
                    cajero_menos_cola = min(cajeros, key=lambda c: c.getCant())
                    cajero_menos_cola.insertar(reloj)
            if cajero_1 == 0 and not cajeros[0].vacia():
                pensionado1 = cajeros[0].suprimir()
                t_espera = reloj - pensionado1
                acum_t += t_espera
                cont += 1
                cont1 += 1
                cajero_1 = 6
            if cajero_2 == 0 and not cajeros[1].vacia():
                pensionado2 = cajeros[1].suprimir()
                t_espera = reloj - pensionado2
                acum_t += t_espera
                cont += 1
                cont2 += 1
                cajero_2 = 4

            if cajero_1 > 0:
                cajero_1 -= 1
            if cajero_2 > 0:
                cajero_2 -= 1
            reloj += 1
        print(f"El tiempo espera de los clientes atendidos es: {acum_t/cont}")
        print(f"El cajero 1 Atendio a {cont1} El cajero 2 Atendio a {cont2}")
    

if __name__ == '__main__':
    cola = Cola()
    cajeros = [Cola() for x in range(2)]
    cola.simularPensiones(300, cajeros)

