from GestorCabaña import gestorCabaña
from GestorReserva import gestorReserva

def menu():
      op = int(input("""Ingrese opcion:
                        1_cargar
                        2_cargar
                        3_
                        4_
                        0_Para finalizar\n"""))
      return op


if __name__=='__main__':
    GC = gestorCabaña() #asigno la clase
    GC.cargarCabaña()
    GC.mostrarCabaña() 

    GR = gestorReserva() #asigno la clase
    GR.cargarReserva()
    GR.mostrarReserva()
    
    
    opcion = menu()
    while opcion!=0:
        if opcion == 1:
            canti= int(input("\nIngrese cant huespedes: "))
            GC.mostrarNumC(canti,GR)
        elif opcion == 2:
            fecha=input("\nIngrese fecha: ")
            GR.listarReservas(fecha,GC)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        else: 
            print("Numero ingresado no corresponde\n")
        opcion = menu()

    