from clase_cuenta import Cuenta
import numpy as np
import csv

class Gestor_cuentas:
    todas_cuentas:list

    def __init__(self):
        self.todas_cuentas = []

    def leer_archivo(self,archivo):
        with open(archivo,"r",encoding="utf-8") as file:
            lector = csv.reader(file,delimiter="")
            lista_cuentas = []
            for i in lector:
                apellido = i[0]
                nombre = i[1]
                dni = i[2]
                telefono = i[3]
                saldo = i[4]
                cvu = i[5]
                porcentaje_rendimiento = i[6]
                datos_cuenta = Cuenta(apellido,nombre,dni,telefono,saldo,cvu,porcentaje_rendimiento)
                lista_cuentas.append(datos_cuenta)
                self.todas_cuentas = lista_cuentas
                np.array(self.todas_cuentas)
        return np.array(self.todas_cuentas)
    
    def actualizar_cuenta(self,dni):
        for i in np.array(self.todas_cuentas):
            if(dni == i[2]):
                saldo = float(input("Ingrese nuevo monto-->"))
                self.todas_cuentas[4] = saldo
                np.array(self.todas_cuentas)
        return np.array(self.todas_cuentas)
    
    def actuallizar_rendimiento(self,aux_rendimiento):
        self.todas_cuentas[6] = aux_rendimiento
        np.array(self.todas_cuentas)
        return np.array(self.todas_cuentas)
    
    def actualizar_saldo(self):
        nuevo_redimiento = self.todas_cuentas[6]
        self.todas_cuentas[4] *= nuevo_redimiento
        np.array(self.todas_cuentas)
        return np.array(self.todas_cuentas)
    
    def informe_saldo(self):
        for i in np.array(self.todas_cuentas):
            print(i)

