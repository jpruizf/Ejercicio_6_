from clase_transaccion import Transaccion
import csv
class Gestor_transaccion:
    trancciones:list

    def __init__(self):
        self.trancciones = []

    def leer_archivo(self, archivo):
        with open(archivo,"r",encoding="utf-8") as file:
            lector = csv.reader(archivo,delimiter="")
            todo_transacciones = []
            for i in lector:
                cvu = i[0]
                nuevo_transaccion = i[1]
                importe = i[2]
                tipo_transaccion = i[3]
                datos_transaccion = Transaccion(cvu,nuevo_transaccion,importe,tipo_transaccion)
                todo_transacciones.append(datos_transaccion)
                self.trancciones = todo_transacciones
        return self.trancciones
    
    def ver_todas_tracciones(self):
        for i in self.trancciones:
            print(i)