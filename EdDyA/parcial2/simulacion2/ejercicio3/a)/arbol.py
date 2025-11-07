#pyrefly: ignore # missing import
from nodo import Nodo
class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def vacia(self):
        return self.__raiz == None

    def insertar(self, nodo, valor):
        if self.vacia() == True:
            self.__raiz = Nodo(valor)
        elif nodo.getElem() == valor:
            print("\nValor ya ingresado")
        elif valor < nodo.getElem():
            if nodo.getIzq():
                self.insertar(nodo.getIzq(), valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self.insertar(nodo.getDer(), valor)
            else:
                nodo.setDer(Nodo(valor)) 
    def hoja(self, nodo):
        if nodo:
            if nodo.getIzq() is None and nodo.getDer() is None:
                print(f"{nodo.getElem()}")
            self.hoja(nodo.getIzq())
            self.hoja(nodo.getDer())
    def terminales (self, nodo, n):
        nodo = self.buscar(nodo, n)
        if nodo is None:
            print("Nodo no encontrado")
        else:
            print(f"\nDescendientes terminales de {n}: ", end="")
            self.hoja(nodo)
            
    def buscar(self, nodo, valor):
        if not nodo:
            encontrado = None
        elif nodo.getElem() == valor:
            encontrado = nodo
        elif valor < nodo.getElem():
            encontrado = self.buscar(nodo.getIzq(), valor)
        else:
            encontrado = self.buscar(nodo.getDer(), valor)
        return encontrado
    def gradoNodo(self, nodo, valor):
        nodo = self.buscar(nodo, valor)
        if nodo is None:
            print("Nodo no encontrado")
        else:
            print(f"Grado del nodo {valor}: {nodo.grado()}")
    def descendientes(self, nodo, valor, cont):
        nodo = self.buscar(nodo, valor)
        if nodo:
            if nodo.getIzq() and nodo.getDer():
                cont += 2
            else:
                if nodo.getIzq() or nodo.getDer():
                    cont += 1
            cont = self.descendientes(nodo.getIzq(), valor, cont)
            cont = self.descendientes(nodo.getDer(), valor, cont)
        return cont
if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 3)
    arbol.insertar(arbol.getRaiz(), 7)
    arbol.insertar(arbol.getRaiz(), 2)
    arbol.insertar(arbol.getRaiz(), 4)
    arbol.insertar(arbol.getRaiz(), 6)
    arbol.insertar(arbol.getRaiz(), 8)

    n = int(input("Ingrese nodo: "))
    arbol.terminales(arbol.getRaiz(), n)
    arbol.hoja(arbol.getRaiz())

    m = int(input("Ingrese nodo: "))
    arbol.gradoNodo(arbol.getRaiz(), m)

    s = int(input("Ingrese nodo: "))
    print(f"Cantidad de descendientes de {s}: {arbol.descendientes(arbol.getRaiz(), s, 0)}")


    