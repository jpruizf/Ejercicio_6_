from gestor_cuenta import Gestor_cuentas
from gestor_transaccion import Gestor_transaccion
def menu():
    gestor_t = Gestor_transaccion()
    gestor_c = Gestor_cuentas()
    print("1.Ver datos de un cliente, ingresando un DNI")
    print("2.Ingresar un nuevo porecentaje anual de rendimiento")
    print("3.Actualizar el saldo actual")
    print("4.Ver saldo inicial, movimientos de todas las transacciones y saldo actualizado")
    print("0.Finalizar")
    opcion = input("Seleccione una de las opciones dadas-->")
    while opcion != '0':
        if opcion == '1':
            if Gestor_cuentas.leer_archivo("cuentasBilletera.csv"):
                print("lectura exitosa!")
            if Gestor_transaccion.leer_archivo("“transaccionesBilletera.csv"):
                print("lectura exitosa!")
            aux_dni = input("DNI-->")
            gestor_c.actualizar_cuenta(aux_dni)
        if opcion == '2':
            aux_porcentaje = input("Porcentaje anual nuevo-->")
            gestor_c.actuallizar_rendimiento(aux_porcentaje)
        if opcion == '3':
            if gestor_c.actualizar_saldo():
                print("Saldo actualizado!")
        if opcion == '4':
            gestor_c.informe_saldo()
            gestor_t.ver_todas_tracciones()
if __name__ == '__main__':
    menu()