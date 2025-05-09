class Transaccion:
    __cvu:int
    __numero_transaccion:int
    __importe:float
    __tipo_traccion:str

    def __init__(self,cvu,numero_tansaccion,importe,tipo_traccion):
        self.__cvu = cvu
        self.__numero_transaccion = numero_tansaccion
        self.__importe = importe
        self.__tipo_traccion = tipo_traccion

    def get_cvu(self):
        return self.__cvu
    
    def get_numero_traccion(self):
        return self.__numero_transaccion
    
    def get_importe(self):
        return self.__importe
    
    def get_tipo_traccion(self):
        return self.__tipo_traccion
    
    def __str__(self):
        return f"{self.get_cvu()}/{self.get_numero_traccion()}/{self.get_importe()}/{self.get_tipo_traccion()}"