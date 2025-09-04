import numpy as np

class ColaSec:
    __max : int
    __pr : int
    __ul : int
    __cant : int
    __elementos : int
    def __init__(self,max = 0):
        self.__max = max
        self.__elementos = np.zeros(max, dtype=int)
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elem):
        if self.__cant < self.__max:
            self.__elementos[self.__ul] = elem
            self.__ul = (self.__ul + 1) % self.__max
            self.__cant += 1
            return elem
        else :
            return 0
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            elem = self.__elementos[self.__pr]
            self.__pr = (self.__pr + 1) % self.__max
            self.__cant -= 1
            return elem
    

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__pr, self.__pr + self.__cant):
                print(self.__elementos[i])
    

class Nodo:
    def __init__(self, elem = None, sig = None):
        self.__elem = elem
        self.__sig = sig

    def getElem(self):
        return self.__elem
    
    def cargar(self, elem):
        self.__elem = elem
    
    def cargarSig(self, tope):
        self.__sig = tope
    
    def getSig(self):
        return self.__sig

class ColaEnc:
    def __init__(self, pr = None, ul = None, cant = 0):
        self.__pr = pr
        self.__ul = ul
        self.__cant = cant
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, x):
        # Crea una nueva nodo y asigna el valor x a su elemento
        newNodo = Nodo(x)
        newNodo.cargarSig(None)  # La nueva nodo no tiene una nodo siguiente

        if self.__ul is None:  # Si la cola está vacía
            self.__pr = newNodo  # La primera nodo es también la última
        else:
            self.__ul.cargarSig(newNodo)  # Conecta la nueva nodo al final de la cola

        self.__ul = newNodo  # Actualiza el puntero al último elemento de la cola
        self.__cant += 1  # Incrementa la cantidad de elementos en la cola
        return self.__ul.getElem()  # Devuelve el valor insertado
    
    def suprimir(self):
        aux = Nodo()

        if self.vacia():
            print("Cola vacia")
            return 0
        else:
            aux = self.__pr
            elem = self.__pr.getElem()
            self.__pr = self.__pr.getSig()
            self.__cant -= 1

            if self.__pr == None:
                self.__ul = None
            del aux
            return elem
    
    def recuperar(self):
        return self.__pr
    
    def recorrer(self):
        aux = self.__pr
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Cargar Cola")
    print("2. Mostrar Cola")
    print("3. Suprimir elemento de la Cola")
    print("0. Finalizar")
    print("------------------------")
        
if __name__ == '__main__':
    cola = ColaEnc()
    op = -1
    while op != 0:
        mostrar_menu()
        try:
            op = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if op == 1:
            try:
                numero = int(input("\nIngrese un número: "))
                cola.insertar(numero)
                print(f"Número {numero} agregado a la Cola.\n")
            except ValueError:
                print("Por favor, ingrese un número válido.\n")
        elif op == 2:
            print("\n--- Mostrando Cola ---")
            cola.recorrer()
        elif op == 3:
            suprimido = cola.suprimir()
            if suprimido != 0:
                print(f"Elemento {suprimido} eliminado de la Cola.\n")
        else:
            print("Opción no válida. Intente nuevamente.\n")
