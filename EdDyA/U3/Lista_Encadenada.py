import re
from turtle import teleport
# pyrefly: ignore  # missing-import
from nodo_lista_en import Nodo
class ListaEncadenada:
    __cabeza : Nodo
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:int, tel: int):
        nuevo = Nodo(elem, tel)
        if self.__cant:
            anterior = None
            actual = self.__cabeza
            while actual != None and actual.getElem() < elem:
                anterior = actual
                actual = actual.getSig()
            if anterior:
                nuevo.setSig(anterior.getSig())
                anterior.setSig(nuevo)
            else:
                nuevo.setSig(self.__cabeza)
                self.__cabeza = nuevo
        else:
            self.__cabeza = nuevo
        self.__cant += 1
    def suprimir(self, posicion:int):
        if 1 <= posicion <= self.__cant:
            if not self.vacia():
                posicion -= 1
                indice = 0
                anterior = None
                actual = self.__cabeza
                while indice != posicion:
                    anterior = actual
                    actual = anterior.getSig()
                    indice += 1
                if anterior:
                    anterior.setSig(actual.getSig())
                else:
                    self.__cabeza = actual.getSig()
                self.__cant-=1
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(f"{aux.getElem()} : {aux.getTel()}")
            aux = aux.getSig()
    def buscar(self, nombre):
        aux = self.__cabeza
        while aux is not None and aux.getElem() != nombre:
            aux = aux.getSig()

        if aux is not None:
            print(f"El teléfono de {nombre} es {aux.getTel()}")
            return True
        else:
            print(f"{nombre} no existe en la agenda")
            return False
    def agregarContacto(self, contacto, tel):
        actual = self.__cabeza
        while actual is not None:
            if actual.getElem() == contacto:
                print("Contacto ya agendado\n")
                return
            actual = actual.getSig()
        self.insertar(contacto, tel)
        print(f"{actual}")
        print("\nContacto agregado:", contacto, "Numero de Telefono: ", tel)

    def borrar_contacto(self):
        nombre = input("Ingrese El nombre del contacto a eliminar: ")
        if self.buscar(nombre):
            if not self.vacia():
                anterior = None
                actual = self.__cabeza
                while actual != None and actual.getElem() != nombre:
                    anterior = actual
                    actual = anterior.getSig()
                if anterior:
                    # pyrefly: ignore  # missing-attribute
                    anterior.setSig(actual.getSig())
                else:
                    # pyrefly: ignore  # missing-attribute
                    self.__cabeza = actual.getSig()
                self.__cant-=1
                print("El contacto fue eliminado de la agenda")
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")


LE = ListaEncadenada()
op = int(input("\nIngrese una opcion:\n1- Agendar Contacto\n2- Eliminar Contacto\n3- Buscar Contacto\n4- Ver los Contactos\n0- Salir\n"))
while op != 0:
    if op == 1:
        LE.agregarContacto(input("Ingrese Nombre del Contacto: "),input("\nIngrese el Telefono: "))
    elif op == 2:
        LE.borrar_contacto()
    elif op == 3:
        LE.buscar(input("\nIngrese el contacto a buscar: "))
    elif op == 4:
        print("\nAgenda de Contactos")
        LE.recorrer()
    else:
        print("\nOpción inválida.")
    op = int(input("\nIngrese una opcion:\n1- Agendar Contacto\n2- Eliminar Contacto\n3- Buscar Contacto\n4- Ver los Contactos\n0- Salir\n"))


"""
1
juan
12445467856
1
diego
3243454564
1
lucas
123123434534
"""
