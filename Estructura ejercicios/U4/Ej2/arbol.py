from nodo import Nodo

class Arbol:
    __raiz: Nodo
    def __init__(self):
        self.__raiz = None

    def vacio(self):
        return self.__raiz == None

    def insertar(self, value):
        if not self.__raiz:
            self.__raiz = Nodo(value)
        else:
            self._insertar(self.__raiz, value)
    def _insertar(self, nodo, elemento):
        if elemento < nodo.getElem():
            if nodo.getIzq() is None:
                nodo.setIzq(Nodo(elemento))
            else:
                self._insertar(nodo.getIzq(), elemento)
        elif elemento > nodo.getElem():
            if nodo.getDer() is None:
                nodo.setDer(Nodo(elemento))
            else:
                self._insertar(nodo.getDer(), elemento)
        elif elemento == nodo.getElem():
            return print("El elemento ya existe")

    def grado(self,nodo : Nodo):
        grado = 0
        if nodo.getIzq():
            grado+=1
        if nodo.getDer():
            grado+=1
        return grado

    def suprimir(self, value):
        self._suprimir(self.__raiz, value)

    def _suprimir(self, nodo, elem):
        if not nodo:
            return None
        elif elem < nodo.getElem():
            nodo.setIzq(self._suprimir(nodo.getIzq(), elem))
        elif elem > nodo.getElem():
            nodo.setDer(self._suprimir(nodo.getDer(), elem))
        else:
            if self.grado(nodo) == 0:
                return None
            if self.grado(nodo) == 1:
                return nodo.getDer() if nodo.getDer() else nodo.getIzq()
            if self.grado(nodo) == 2:
                maximo = nodo.getIzq()
                while maximo.getDer() != None:
                    maximo = maximo.getDer()
                nodo.setElem(self._suprimir(nodo.getIzq(), maximo.getElem()))
        return nodo
    def preorden(self):
        self._preorden(self.__raiz)
    
    def _preorden(self, nodo):
        if nodo:
            print(f"{nodo.getElem()}")
            self._preorden(nodo.getIzq())
            self._preorden(nodo.getDer())
    
    def hijo(self, hijo: Nodo, padre: Nodo):
        nodo_p = self.buscar(padre)
        es_hijo = False
        if nodo_p == None:
            es_hijo = False
        elif nodo_p.getIzq() != None and nodo_p.getIzq().getElem() == hijo:
            es_hijo = True
        elif nodo_p.getDer() != None and nodo_p.getDer().getElem() == hijo:
            es_hijo = True
        return es_hijo
    
    def hoja(self, valor:int):
        nodo = self.buscar(valor)
        es_hoja = False
        if not nodo:
            es_hoja = False
        elif self.grado(nodo)==0:
            es_hoja = True
        return es_hoja
    
    def padre(self, padre:int, hijo:int):
        nodo_padre = self.buscar(padre)
        es_padre = False
        if nodo_padre == None:
            es_padre = False
        elif nodo_padre.getIzq() != None and nodo_padre.getIzq().getElem() == hijo:
            es_padre = True
        elif nodo_padre.getDer() != None and nodo_padre.getDer().getElem()==hijo:
            es_padre = True
        return es_padre

    def nivel(self,valor : int):
        return self._nivel(self.__raiz,valor,0)
    def _nivel(self, nodo : Nodo, valor : int,nivel : int):
        if nodo == None:
            nivel = 0
        elif valor < nodo.getElem():
            nivel += 1
            nivel = self._nivel(nodo.getIzq(),valor,nivel)
        elif valor > nodo.getElem():
            nivel += 1
            nivel = self._nivel(nodo.getDer(),valor,nivel)
        else:
            nivel+=1
        return nivel
    def altura(self):
        return self._altura(self.__raiz,0)

    def _altura(self, nodo : Nodo, altura : int):
        if nodo:
            if altura < self.nivel(nodo.getElem()):
                altura +=1
            altura = self._altura(nodo.getIzq(),altura)
            altura = self._altura(nodo.getDer(),altura)
        return altura

    def PreOrden(self):
        self._PreOrden(self.__raiz)

    def _PreOrden(self,nodo:Nodo):
        if nodo:
            print(nodo.getElem())
            self._inOrden(nodo.getIzq())
            self._inOrden(nodo.getDer())

    def PostOrden(self):
        self._PostOrden(self.__raiz)

    def _PostOrden(self,nodo:Nodo):
        if nodo:
            self._inOrden(nodo.getIzq())
            self._inOrden(nodo.getDer())
            print(nodo.getElem())

    def raiz(self):
        return self.__raiz
    def antecesor(self,x : int,z : int):
        es_antecesor = False
        if self._buscar(self.buscar(x),z) != None:
            es_antecesor = True
        return es_antecesor
        
    def camino(self,inicio : int,fin : int):
        es_antecesor = self.antecesor(inicio, fin)
        camino = []
        if es_antecesor == True:
            nodo_actual = self.buscar(inicio)
            while nodo_actual != None and nodo_actual.getElem() != fin:
                if fin < nodo_actual.getElem():
                    camino.append(0)
                    nodo_actual = nodo_actual.getIzq()
                else:
                    camino.append(1)
                    nodo_actual = nodo_actual.getDer()
        return camino

    def padre_hermano(self, valor):
        return self._padre_hermano(valor, self.__raiz)
    def _padre_hermano(self, valor, nodo):
        if nodo is None:
            return None, None
        elif valor == nodo.getElem():
            print("\nEl valor es el mismo que la raíz")
            return None, None
        elif nodo.getIzq() and nodo.getIzq().getElem() == valor:
            padre = nodo.getElem()
            hermano = None
            if nodo.getDer():
                hermano = nodo.getDer().getElem()
            return hermano, padre

        elif nodo.getDer() and nodo.getDer().getElem() == valor:
            padre = nodo.getElem()
            hermano = None
            if nodo.getIzq():
                hermano = nodo.getIzq().getElem()
            return hermano, padre
        elif valor < nodo.getElem():
            return self._padre_hermano(valor, nodo.getIzq())
        else:
            return self._padre_hermano(valor, nodo.getDer())
            
            
if __name__ == '__main__':
    arbol = Arbol()
    op = input("\nIngrese una opcion: ")
    while op != "0":
        if op == "1":
            nodo = int(input(f"\nIngrese un nodo para insertar: "))
            arbol.insertar(nodo)
        elif op == "2":
            try:
                valor = int(input(f"\nIngrese un valor para buscar su padre y hermano: "))
                hermano, padre = arbol.padre_hermano(valor)
                if hermano:
                    print(f"\nEl hermano de {valor} es {hermano}")
                else:
                    print(f"\nEl hermano de {valor} no existe")
                if padre:
                    print(f"\nEl padre de {valor} es {padre}")
                else:
                    print(f"\nEl padre de {valor} no existe")
            except:
                print("\nValor no encontrado")
        op = input("\nIngrese una opcion: ")

"""
1
10
1
8
1
9
1
7
1
12
1
11
1
13
"""

    