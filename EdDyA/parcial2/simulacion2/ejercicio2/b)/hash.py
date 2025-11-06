# pyrefly: ignore  # missing-import
from lista import ListaEncadenada
import numpy as np
class Tabla:
    __tamaño: int
    __tabla: np.ndarray
    def __init__(self,tamaño : int)->None:
        self.__tamaño = self.obtener_primo(round(tamaño/ 0.7))
        self.__tabla = np.array([ListaEncadenada() for _ in range(self.__tamaño)], dtype=list)
    def obtener_primo(self, n):
        if self.es_primo(n):
            return n
        siguiente = n + 1
        while not self.es_primo(siguiente):
            siguiente += 1
        return siguiente
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def __hash(self, elem: int) -> int:
        return elem % self.__tamaño
    def insertar(self, elem):
        indice = self.__hash(elem)
        self.__tabla[indice].insertar(elem)
    
    def buscar(self, elem):
        i = self.__hash(elem)
        encontrado = False
        cont = 0
        if self.__tabla[i] == elem:
            cont += 1
            encontrado = True
        else:
            fin = i
            i = (i + 1) % self.__tamaño
            while i != elem and i != fin:
                cont += 1
                i = (i + 1) % self.__tamaño
            if i != fin:
                encontrado = True
        return encontrado

    def mostrar(self):
        for i in range(self.__tamaño):
            if self.__tabla[i].getCabeza() != None:
                print(f"{i}: {self.__tabla[i].recorrer()}")                          

if __name__ == "__main__":
    tabla = Tabla(10)
    tabla.insertar(10)
    tabla.insertar(20)
    tabla.insertar(30)
    print(tabla.buscar(10))
    print(tabla.buscar(20))
    print(tabla.buscar(30))
    print(tabla.buscar(40))
    tabla.mostrar()