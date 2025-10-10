from Eje5 import ColaEnc
import random

def subir(n, cola):
    while n > 0:
        op = random.randint(1,2)
        if op == 2 and n >= 2:
            cola.insertar(2)
            n -= 2
        else:   
            cola.insertar(1)
            n -= 1
    while not cola.vacia():
        print(cola.suprimir())
    
if __name__ == "__main__":
    cola = ColaEnc()
    n = int(input("Ingrese un número de escalones: "))
    print("\n--- Mostrando Secuencia ---")
    subir(n, cola)

