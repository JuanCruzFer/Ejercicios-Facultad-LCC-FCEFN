
import numpy as np

class TablasHash:
    def __init__(self, tamaño, band = True):
        self.__tamaño = int(tamaño/0.7)
        if band:
            self.__tamaño = self.primo(int(tamaño/0.7))
        else:
            self.__tamaño = (int(tamaño/0.7))
        self.__cantidad_actual = 0
        self.__tabla = np.ndarray(self.__tamaño, dtype=object)
        self.__tabla.fill(None)

    def primo(self, n):
        i = 2
        while i < n and n % i != 0:
            i += 1
        if i == n:
            return n
        else:
            return self.primo(n + 1)
    def hash(self, clave):
        return hash(clave) % self.__tamaño
    
    def insertar(self, clave, valor: int, metodo):
        direccion = self.hash(clave)
        i = 0

        while i < self.__tamaño:
            direccion = (direccion + i) % self.__tamaño
            if self.__tabla[direccion] == None:
                self.__tabla[direccion] = (clave, valor)
                self.__cantidad_actual += 1
                return
            i += 1
        print("Tabla llena")
    


if __name__ == "__main__":
    try:
        tabla = int(input("Ingrese el tamaño de la tabla: "))
        tabla = TablasHash(tabla)
        print("Tabla hash creada para " + str(tabla.__tamaño) + " elementos")
    except:
        print("Error al ingresar el tamaño de la tabla, creando predeterminada de 100 elementos")
        tabla = TablasHash(100)

    op = -1
    while op != 0:
        print("\nMenu de Opciones")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("0. Salir")

        try:
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                clave = input("Ingrese la clave: ")
                valor = int(input("Ingrese el valor: "))
                tabla.insertar(clave, valor, 1)
                print("Valor insertado correctamente")
            elif op == 2:
                print("Metodo aun no implementado")
            elif op == 3:
                print("Metodo aun no implementado")
            elif op == 0:
                print("Saliendo...")
            
            else:
                print("Opcion invalida")
        except:
            print("Error al ingresar opcion")
            op = -1
        