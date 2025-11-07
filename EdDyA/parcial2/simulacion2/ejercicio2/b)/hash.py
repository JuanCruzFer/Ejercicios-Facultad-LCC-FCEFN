# pyrefly: ignore  # missing-import
from lista import ListaEncadenada
import numpy as np
class Tabla:
    __tamaño: int
    __tabla: np.ndarray
    def __init__(self, tamaño):
        self.__tamaño = int(np.ceil(self.obtener_primo(tamaño/0.7)))
        self.__tabla = np.empty(self.__tamaño, dtype=object)
        for i in range(self.__tamaño):
            self.__tabla[i] = ListaEncadenada()
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
    
    def buscar(self, valor):
        i = self.__hash(valor)
        aux = self.__tabla[i].getCab() 
        intentos = 1
        encontrado = False
        
        while aux != None and aux.getElem() != valor:
            aux = aux.getSig()
            intentos += 1
        if aux != None:
            encontrado = True 
            print(f"el valor {valor} está en el índice {i}")
            print(f"Se encontró en {intentos} intento(s)\n")
        else:
            print(f"el valor {valor} no se encontró después de {intentos} intento(s)")

        return encontrado

    def mostrar(self):
        for i, lista in enumerate(self.__tabla):
            if lista.getCab() != None:
                print(f"[{i}] {lista.getCab().getElem()}")                         

if __name__ == "__main__":
    tabla = Tabla(10)
    tabla.insertar(10)
    tabla.insertar(20)
    tabla.insertar(30)

    tabla.buscar(10)
    tabla.buscar(20)
    tabla.buscar(30)
    tabla.buscar(40)
    