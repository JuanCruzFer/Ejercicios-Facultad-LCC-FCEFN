from GestorAlquiler import gestorAlquiler
from GestorCancha import gestorCancha

if __name__=='__main__':
    GA= gestorAlquiler()
    GA.cargar_alquileres()


    GC= gestorCancha()
    GC.cargar_canchas()
    GC.mostrar_canchas()

    op=int(input("""\nIngrese una Opcion
                    
                    1. Listar por hora y minutos
                    2. Ingresar un id de cancha
                    0. Para finalizar
                """))
    while op!= 0:
        if op== 1:
            GA.ordenarAlq()
            GA.listarAlquiler(GA,GC)
        elif op==2:
            id=input("\nIngrese id de cancha: ")
            GC.CantMin(id,GA)
        else:
            print("\nNum Incorrecto")
        op=int(input("""\nIngrese una Opcion
                    
                    1. Listar por hora y minutos
                    2. Ingresar un id de cancha
                    0. Para finalizar
                """))