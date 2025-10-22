import random

class Trabajo:
    def __init__(self, tiempo):
        self.__tiempo = tiempo
        self.__cant = 100
        self.__sig = None

    def getTiempo(self):
        return self.__tiempo
        return self.__sig
    def setTiempo(self, tiempo):
        self.__tiempo = tiempo
    
    def getCant(self):
        return self.__cant
    
    def setCant(self, cant):
        self.__cant = cant

    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig = sig

class ColaImpresion:
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0
        self._tiempoEspera = 0
        self.__trabajosProcesados = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, tiempo):
        nuevoTrabajo = Trabajo(tiempo)
        if self.__ul is None: #Cola vacia
            # pyrefly: ignore  # bad-assignment
            self.__pr = nuevoTrabajo
        else:
            self.__ul.setSig(nuevoTrabajo)
        # pyrefly: ignore  # bad-assignment
        self.__ul = nuevoTrabajo
        self.__cant += 1
    
    def suprimir(self):
        if self.vacia():
            return None
        else:
            aux = self.__pr
            # pyrefly: ignore  # missing-attribute
            self.__pr = self.__pr.getSig()
            self.__cant -= 1
            if self.__pr is None:
                self.__ul = None
            return aux
    
    def recorrer(self):
        aux = self.__pr
        while aux != None:
            print(aux.getTiempo())
            aux = aux.getSig()
        
    def procesar(self, duracion):
        tiempoActual = 0
        while tiempoActual < duracion:
            if self.vacia():
                break
            else:
                actual = self.suprimir()
                # pyrefly: ignore  # missing-attribute
                tiempoTrabajo = actual.getTiempo()
                if tiempoTrabajo > 5:
                    self.insertar(tiempoTrabajo - 5)
                    self._tiempoEspera += 5
                else:
                    tiempoActual += tiempoTrabajo
                    self._tiempoEspera += tiempoActual
                    self.__trabajosProcesados += 1

    def tiempoPromedio(self):
        if self.__trabajosProcesados == 0:
            return 0
        return self._tiempoEspera / self.__trabajosProcesados  

    def mostrar(self):
        aux = self.__pr
        while aux != None:
            print(f"Trabajo con {aux.getTiempo()} minutos restantes")
            aux = aux.getSig()
        
    def pendientes(self):
        return self.__cant

if __name__ == "__main__":
    cola = ColaImpresion()

    for _ in range(random.randint(1, 10)):
        cola.insertar(random.randint(1, 10))
    
    print("Estado inicial de la cola de impresión:")
    cola.mostrar()

    print("\nProcesando trabajos...")
    duracion_simulacion = 60  # Simulamos 60 minutos de tiempo total de la impresora
    cola.procesar(duracion_simulacion)

    print("\nEstado final de la cola de impresión:")
    cola.mostrar()

    # Resultados
    print(f"\nCantidad de trabajos que quedaron sin atender: {cola.pendientes()}")
    print(f"Promedio de espera de los trabajos impresos: {cola.tiempoPromedio()} minutos")
    


    
