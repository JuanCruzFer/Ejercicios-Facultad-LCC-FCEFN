from Ejercicio_1 import PilaEncadenada
import random

def subir(n, pila):
    while n > 0:
        esc= random.randint(1,2)
        if esc == 2:
            pila.insertar(2)
            n-=2
        else:
            pila.insertar(1)
            n-=1
    while not pila.vacia():
        print(pila.suprimir())

if __name__ == "__main__":
    pila = PilaEncadenada()
    subir(7, pila)