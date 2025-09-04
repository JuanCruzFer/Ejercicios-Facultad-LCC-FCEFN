

from Ejercicio_1 import PilaEncadenada

def jugada(origen, destino, pO, pD):
    if origen == destino:
        print("Movimiento inválido: origen y destino son iguales.")
        return False
    if pO.vacia():
        print("Movimiento inválido: la pila de origen está vacía.")
        return False

    disco = pO.tope()
    if pD.vacia() or disco < pD.tope():
        pD.insertar(pO.suprimir())
        return True
    else:
        print("Movimiento inválido: no se puede poner un disco grande sobre uno chico.")
        return False
    

if __name__ == '__main__':
    n = int(input("Ingrese un tamaño: "))
    pila1 = PilaEncadenada()
    pila2 = PilaEncadenada()
    pila3 = PilaEncadenada()

    for i in range(1, n + 1):  
        pila1.insertar(i)

    jugadas = 0

    while pila3.cantidad() != n: 
        print("\n--- Estado actual ---")
        print("Pila 1:", pila1.cantidad(), "elementos")
        print("Pila 2:", pila2.cantidad(), "elementos")
        print("Pila 3:", pila3.cantidad(), "elementos")
        print("---------------------")
        pila1.recorrer()
        print("---------------------")
        pila2.recorrer() 

        origen = int(input("Ingrese pila origen (1,2,3): "))
        destino = int(input("Ingrese pila destino (1,2,3): "))

        if origen not in (1,2,3) or destino not in (1,2,3):
            print("Origen/destino inválido: debe ser 1, 2 o 3.")
            continue

        if (origen, destino) in ((1,3),(3,1)):
            print("Movimiento inválido: no se puede pasar directamente de la pila 1 a la 3.")
            continue

        pilas = [pila1, pila2, pila3]
        pO, pD = pilas[origen - 1], pilas[destino - 1]

        if jugada(origen, destino, pO, pD):
            jugadas += 1
            print(f"Jugadas realizadas: {jugadas}")
        else:
            print("Movimiento inválido")

    print(f"\n¡Juego terminado en {jugadas} jugadas!")
