import numpy as np
import random

class Tablahash:
    __tabla : np.ndarray
    def __init__(self, flag, N = 100):
        if flag:
            self.__size = self.primo(int(N / 0.7))
        else:
            self.__size = int(N / 0.7)
        self.__tabla = np.ndarray(self.__size,dtype=object)
        self.__tabla.fill(None)
    def primo(self, x):
        i = 2
        while i < x and x % i != 0:
            i += 1
        if i == x:
            aux = x
        else:
            aux = self.primo(x + 1)
        return aux
    def hash(self, clave):
        return int(clave) % self.__size

    def insertar(self, clave):
        direccion = self.hash(clave)
        cont = 1
        while self.__tabla[direccion] is not None and cont != self.__size:
            direccion = (direccion + 1) % self.__size
            direccion = direccion % self.__size
            cont =+1
        if cont != self.__size:
            self.__tabla[direccion] = clave
            print(self.__tabla[direccion])
            print(f"Comparaciones: {cont}")
        else:
            return 0

    def buscar(self, clave):
        direccion = self.hash(clave)
        cont = 1
        band = False
        while self.__tabla[direccion] is not None and cont != self.__size:
            if self.__tabla[direccion] == clave:
                print(f"el valor: {self.__tabla[direccion]} se encontró en {cont} comparaciones\n")
                cont = self.__size
                band = True
            else:
                direccion = (direccion + 1) % self.__size
                cont += 1
        if not band:
            print("No se encontro")
    def mostrar(self):
        return self.__tabla

            
if __name__ == '__main__':
    op = int(input("Ingrese una opcion: 1_hash con primo 2_hash sin primo 3_buscar clave en la tabla\n"))

    while op != 0:
        if op == 1:
            tabla = Tablahash(True)
            for _ in range(1, 100):
                tabla.insertar(str(random.randint(46000000, 46999999)))
        elif op == 2:
            tabla = Tablahash(False)
            for _ in range(1, 100):
                tabla.insertar(str(random.randint(46000000, 46999999)))
        elif op == 3:
            try:
                tabla.buscar(input("Ingrese clave a buscar: "))
            except:
                print("\nError")
        elif op == 4:
            tabla.mostrar()
        op = int(input("Ingrese una opcion: 1_hash con primo 2_hash sin primo\n"))
    


    


    
    
    

