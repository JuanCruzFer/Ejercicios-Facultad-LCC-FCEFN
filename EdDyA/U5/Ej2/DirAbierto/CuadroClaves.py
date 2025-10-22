
from socket import inet_pton
import numpy as np
class CuadroClaves:
    __tamaño : int
    __tabla: np.ndarray
    def __init__(self, tamaño: int):
        self.__tamaño = self.obtener_primo(round(tamaño / 0.7))
        self.__tabla = np.full(self.__tamaño, None, dtype = object)
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_primo(self, n):
        if self.es_primo(n):
            return n
        siguiente = n + 1
        while not self.es_primo(siguiente):
            siguiente += 1
        return siguiente
    
    def hashDiv(self, valor):
        return valor % self.__tamaño
    
    def hashAscii(self, palabra : str):
        indice = 0
        base = 31
        for letra in palabra:
            indice = (indice * base + ord(letra)) % self.__tamaño
        return indice

    def insertar(self, valor, metodo):
        if metodo == "ascii":
            direccion = self.hashAscii(valor)
        else:
            direccion = self.hashDiv(valor)

        repetido = False #En tablas hash no se insertan valores repetidos
        
        if self.__tabla[direccion] == None: #Si en la posicion del valor hasheado esta libre se inserta
            self.__tabla[direccion] = valor
        elif self.__tabla[direccion] == valor: #si en la posicion del valor hasheado esta otro valor igual  no se inserta
            repetido = True
        else: #Hubo una colisicion guardamos en una variable final el indice en el que estabamos esto nos servira para saber que reccorimos toda la tabla
            final = direccion
            direccion = (direccion + 1) % self.__tamaño # aqui nos movemos a la siguiente posicion, el % self.__tamaño hara que el recorrido sea circular es decir posamos recorrer toda la tabla, si! como en cola circular XD
            while self.__tabla[direccion] != None and direccion != final:
                if self.__tabla[direccion] == valor:
                    repetido = True
                direccion = (direccion + 1) % self.__tamaño
            if repetido is False: #si el valor se repite no se inserta nada
                if direccion != final:# si el indice es igual al final quiere decir que se recorrio todo el arreglo y no se encontro posicion valida, osea que si son distintos se encontro lugar disponible
                    self.__tabla[direccion] = valor
        if repetido is True:
                print("Valor no insertador por esta ya en la lista")
                
    def buscar(self, valor, metodo):
        if metodo == "ascii":
            dir = self.hashAscii(valor)
        else:
            dir = self.hashDiv(valor)
        encontrado = False
        cont = 1
        if self.__tabla[dir] == valor:
            encontrado = True
            print(f"Valor {valor} encontrado en la direccion {dir}")
        else:
            fin = dir
            dir = (dir + 1) % self.__tamaño
            if dir != fin:
                cont += 1
                while self.__tabla[dir] != valor and dir != fin:
                    dir = (dir + 1) % self.__tamaño
                    cont += 1
            if dir != fin:
                encontrado = True
                print(f"Valor {valor} encontrado en la direccion {dir}")
        print(cont)
        return encontrado  
    def mostrar(self):
        print(self.__tabla)
if __name__ == '__main__':
    tabla = CuadroClaves(10)
    
    
    tabla.insertar(17, "")
    tabla.insertar("hola", "ascii")  
    tabla.insertar(2, "") 
    tabla.insertar(34, "")
    tabla.insertar(51, "")
    tabla.mostrar()
    op = input("\nIngrese si la clave a buscar es un string o un integer: ")
    if op == "cadena":
        tabla.buscar(input("\nIngrese clave a buscar: "), input("\nEliga metodo de transformacion: "))
    elif op == "entero":
        tabla.buscar(int(input("\nIngrese clave a buscar: ")), input("\nEliga metodo de transformacion: "))
    