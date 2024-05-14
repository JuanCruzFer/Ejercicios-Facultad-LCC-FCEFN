from claseCuenta import Cuenta
from GestorCuenta import gestorCuenta
from GestorTransaccion import gestorTransaccion

if __name__=='__main__':
    GC=gestorCuenta()
    #unaCuenta=Cuenta("Juan","Fernandez","44000999","2645505978",2000.0,"0000000",21)
    GC.carga_desde_CSV()
    GC.mostrarCuenta()

    GT=gestorTransaccion()
    GT.cargarT_desde_CSV()
    GT.mostrarTra()

    op=int(input("""\nIngrese una Opcion
                    1.Informar Datos Clientes (saldo actualizado)
                    2.Porcentaje Anual nuevo
                    3.Actualizar Saldo (porcentaje diario)
                    4.Informar Saldo despues de las Transacciones
                    5.Almacenar los Datos Nuevos en un archivo
                 """))
    while op!=0:
        if op==1:
            dni=input("\nIngrese Dni del Cliente: ")
            GC.mostrarDatos(dni,GT)
        elif op==2:
            nuevo_porcentaje=float(input("\nIngrese nuevo porcentaje: "))
            GC.nuevoPor(nuevo_porcentaje)
        elif op==3:
            GC.actualizarSaldoPorRendimiento(nuevo_porcentaje)
        elif op==4:
            cvu=input("\nIngrese CVU: ")
            GC.informarSaldo(cvu,GT)
        elif op==5:
            GC.almacenarDatos()
        else:
            print("Numero incorrecto\n")
        op=int(input("""\nIngrese una Opcion:
                    1.Informar Datos Clientes (saldo actualizado
                    2.Porcentaje Anual nuevo
                    3.Actualizar Saldo (porcentaje diario)
                    4.Informar Saldo despues de las Transacciones
                    5.Almacenar los Datos Nuevos en un archivo
                 """))