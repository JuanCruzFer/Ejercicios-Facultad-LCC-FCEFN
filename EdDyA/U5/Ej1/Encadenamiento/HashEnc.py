import random
# pyrefly: ignore  # missing-import
from Nodo import Nodo
import numpy as np
class HashEnc:
    __lista : np.ndarray
    __tamaño: int
    __colisiones: list

    def __init__(self, N = 100, M = 5):
        self.__tamaño = int(N / M)
        # pyrefly: ignore  # bad-assignment
        self.__colisiones = np.zeros(self.__tamaño, dtype=int)
        self.__lista = np.ndarray(self.__tamaño, dtype=object)
    
    def plegado(self, clave):
        clave_str = str(clave)
        suma = 0
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        return suma % self.__tamaño
    
    def insertar(self, clave):
        direccion = self.plegado(clave)
        nuevo_nodo = Nodo(clave)
        nodo_actual = self.__lista[direccion]
        existe = nodo_actual
        while existe is not None:
            if nodo_actual.getClave() == clave:
                print(f"Valor {clave} ya existe en la tabla")
                return
            existe = existe.getSig()
        nuevo_nodo.setSig(nodo_actual)
        self.__lista[direccion] = nuevo_nodo
        print(f"\nValor {clave} insertado en la direccion {direccion}")
        if nodo_actual is not None:
            self.__colisiones[direccion] += 1
            print(f"\nColision en la direccion {direccion}, Clave {clave}")
    
    def buscar(self, clave):
        direccion = self.plegado(clave)
        nodo_actual = self.__lista[direccion]
        while nodo_actual is not None:
            if nodo_actual.getClave() == clave:
                print(f"\nValor {clave} encontrado en la direccion {direccion}")
                return True
            nodo_actual = nodo_actual.getSig()
        return False

    def promedioColisiones(self):
        suma = 0
        for i in range(len(self.__colisiones)):
            suma += self.__colisiones[i]
        return suma / self.__tamaño
    def cantidadColisiones(self):
        # pyrefly: ignore  # missing-attribute
        return self.__colisiones.sum()
    
    def colicionesPorDireccion(self, direccion):
        if 0 <= direccion < self.__tamaño:
            return self.__colisiones[direccion]
        else:
            print("\nDireccion invalida")
            return -1

if __name__ == "__main__":
    tabla = HashEnc()

    claves = []
    op = -1
    
    while op != 0:
        print("\nMenu de Opciones")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Promedio de colisiones")
        print("4. Cantidad de colisiones")
        print("5. Coliciones por direccion")
        print("0. Salir")
        try:
            op = int(input("\nIngrese una opcion: "))
            if op == 1:
                for _ in range(100):
                    claves.append(random.randint(45000000, 45999999))
                for clave in claves:
                    tabla.insertar(clave)
            elif op == 2:
                seguir_buscando = True
                while seguir_buscando:
                    try:
                        clave = int(input("\nIngrese un valor para buscar: "))
                        encontrado = tabla.buscar(clave)
                        if not encontrado:
                            respuesta = input("\nValor no encontrado, desea buscar otro valor? (s/n): ")
                            if respuesta.lower() != "s":
                                seguir_buscando = False
                        else:
                            respuesta = input("\nValor encontrado, desea buscar otro valor? (s/n): ")
                            if respuesta.lower() != "s":
                                seguir_buscando = False
                    except ValueError:
                        print("\nError, ingrese un valor valido")
            elif op == 3:
                print("\nPromedio de colisiones:")
                print(f"{tabla.promedioColisiones()}")
            elif op == 4:
                print("\nCantidad de colisiones:")
                print(f"{tabla.cantidadColisiones()}")
            elif op == 5:
                try:
                    direccion = int(input("\nIngrese una direccion para ver colisiones: "))
                    print(f"\nColisiones en la direccion {direccion}:")
                    print(f"{tabla.colicionesPorDireccion(direccion)}")
                except ValueError:
                    print("\nError, ingrese un valor valido")
            elif op == 0:
                print("\nSaliendo...")
        except:
            print("\nError al ingresar opcion")
            op = -1



    
