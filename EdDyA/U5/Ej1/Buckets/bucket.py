import re
import numpy as np
class Bucket:
    __tabla : np.ndarray #Arreglo bidimensional que actúa como tabla hash. Cada fila representa un bucket, y cada columna representa un espacio dentro de ese bucket.
    __cap_bucket : int  #Define la capacidad máxima de cada bucket, es decir, cuántas claves puede almacenar un bucket antes de que ocurra un desbordamiento
    __tamaño: int #Tamaño total de la tabla hash, que se calcula en función de la cantidad de claves y la capacidad de los buckets.
    __contadores: list #Arreglo que mantiene el número de claves almacenadas en cada bucket (nos ayuda a saber cuántas posiciones en cada bucket están ocupadas.)
    def __init__(self, claves = 100, cap_bucket = 4):
        self.__cap_bucket = cap_bucket
        self.__tamaño = int(claves / cap_bucket + (claves / cap_bucket) * 0.2)
        self.__tabla = np.zeros((self.__tamaño, cap_bucket), dtype= object)
        self.__contadores = np.zeros(self.__tamaño, dtype=int)
        self.__direccion_overflow = int(claves / cap_bucket)
        print(f"\nBucket creado con {self.__tamaño} elementos y {cap_bucket} buckets")
    
    def extraccion(self, clave):
        return int(clave[-2:]) % self.__direccion_overflow
    
    def insertar(self, clave):
        if self._buscar(clave):
            print(f"\nValor {clave} ya existe en la tabla")
            return
        direccion = self.extraccion(clave)
        if self.__contadores[direccion] < self.__cap_bucket:
            self.__tabla[direccion][self.__contadores[direccion]] = clave
            self.__contadores[direccion] += 1
            print(f"\nValor {clave} insertado en la direccion {direccion}")
            return
        else:
            print(f"\nBucket {direccion} lleno. Buscando en área de overflow...")
            encontrado_en_overflow = False
            i = self.__direccion_overflow
            while i < self.__tamaño and not encontrado_en_overflow:
                if self.__contadores[i] < self.__cap_bucket:
                    self.__tabla[i][self.__contadores[i]] = clave
                    self.__contadores[i] += 1
                    print(f"Valor {clave} insertado en bucket de overflow {i}")
                    encontrado_en_overflow = True
                    return
                i += 1
            if not encontrado_en_overflow:
                print(f"Área de overflow también está llena. No se pudo insertar {clave}.")
    def _buscar(self, clave):
        i = 0
        encontrado = False
        direccion = self.extraccion(clave)
        while i < self.__contadores[direccion] and not encontrado:
            if self.__tabla[direccion][i] == clave:
                encontrado = True
            i += 1
        if encontrado:
            return True
        dir_overflow = self.__direccion_overflow
        
        while dir_overflow < self.__tamaño and not encontrado:
            j = 0
            while j < self.__contadores[dir_overflow] and not encontrado:
                if self.__tabla[dir_overflow][j] == clave:
                    encontrado = True
                j += 1
            dir_overflow += 1
        return encontrado
    def buscar(self, clave):
        i = 0
        encontrado = False
        direccion = self.extraccion(clave)
        while i < self.__contadores[direccion] and not encontrado:
            if self.__tabla[direccion][i] == clave:
                encontrado = True
            i += 1
        if encontrado:
            print(f"\nValor {clave} encontrado en la direccion {direccion}")
            return True
        print(f"\nValor {clave} no encontrado en el area primaria")
        dir_overflow = self.__direccion_overflow
        while dir_overflow < self.__tamaño and not encontrado:
            j = 0
            while j < self.__contadores[dir_overflow] and not encontrado:
                if self.__tabla[dir_overflow][j] == clave:
                    encontrado = True
                j += 1
            if encontrado:
                print(f"\nValor {clave} encontrado en la direccion {dir_overflow}")
                return True
            dir_overflow += 1
        print(f"\nValor {clave} no encontrado en ninguna direccion")
        return False 
                
    def mostrarBuckets(self):
        for i in range(self.__tamaño):
            print(f"\nBucket {i}:")
            for j in range(self.__contadores[i]):
                print(f"{self.__tabla[i][j]}", end=" ")
            print()
    def eliminarClave(self, clave):
        direccion = self.extraccion(clave)
        i = 0
        while i < self.__contadores[direccion]:
            if self.__tabla[direccion][i] == clave:
                self.__tabla[direccion][i] = None
                self.__contadores[direccion] -= 1
                print(f"\nValor {clave} eliminado de la direccion {direccion}")
                return
            i += 1
        print(f"\nValor {clave} no encontrado en la direccion {direccion}, Buscar en Overflow")
        dir_over = self.__direccion_overflow
        while dir_over < self.__tamaño:
            j = 0
            while j < self.__contadores[dir_over]:
                if self.__tabla[dir_over][j] == clave:
                    self.__tabla[dir_over][j] = None
                    self.__contadores[dir_over] -= 1
                    print(f"\nValor {clave} eliminado de la direccion {dir_over}")
                    return
                j += 1
            dir_over += 1
        print(f"\nValor {clave} no encontrado en ninguna direccion")

if __name__ == "__main__":
    tabla = Bucket()
    
    op = -1
    
    while op != 0:
        print("\nMenu de Opciones")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Mostrar")
        print("0. Salir")
        try:
            op = int(input("\nOpcion: "))
            if op == 1:
                clave = input("\nClave: ")
                tabla.insertar(clave)
            elif op == 2:
                clave = input("\nClave: ")
                tabla.buscar(clave)
            elif op == 3:
                tabla.mostrarBuckets()
            elif op == 4:
                clave = input("\nClave: ")
                tabla.eliminarClave(clave)
            elif op == 0:
                print("Saliendo...")
            else:
                print("Opcion invalida")
        except ValueError:
            print("Opcion invalida")

        
