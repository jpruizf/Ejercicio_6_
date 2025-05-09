class Cuenta:
    __Apellido:str
    __Nombre:str
    __DNI:int
    __telefono:int
    __saldo:float
    __cvu:int
    __porcentaje_rendimiento:float

    def __init__(self,apellido,nombre,dni,telefono,saldo,cvu,porcentaje_rendimiento):
        self.__Apellido = apellido
        self.__Nombre = nombre
        self.__DNI = dni
        self.__telefono = telefono
        self.__saldo = saldo
        self.__cvu = cvu
        self.__porcentaje_rendimiento = porcentaje_rendimiento
    
    def get_cliente(self):
        return f"Titular de la cuenta:{self.__Nombre}/{self.__Apellido}"
    
    def get_dni(self):
        return self.__DNI
    
    def get_telefono(self):
        return self.__telefono
    
    def get_saldo(self):
        return self.__saldo
    
    def get_cvu(self):
        return self.__cvu
    
    def get_porcentaje_rendimiento(self):
        return self.__porcentaje_rendimiento
    
    def __str__(self):
        return f"{self.get_cliente()}/{self.get_dni()}/{self.get_telefono()}/{self.get_saldo()}/{self.get_cvu}/{self.get_porcentaje_rendimiento()}"