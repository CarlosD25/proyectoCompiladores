class Vehiculo: 
   
    def __init__(self, tipoVehiculo:str, placa:str, horaEntrada, horaSalida:str="Sin Hora de Salida"):
        self.__tipoVehiculo = tipoVehiculo
        self.__placa = placa
        self.__horaEntrada = horaEntrada
        self.__horaSalida = horaSalida

    def getTipoVehiculo(self):
        return self.__tipoVehiculo
    
    def setTipoVehiculo(self,tipoVehiculo:str):
        self.__tipoVehiculo= tipoVehiculo
    
    def getPlaca(self):
        return self.__placa

    def setPlaca(self, placa:str):
        self.__placa=placa
    
    def getHoraEntrada(self):
        return self.__horaEntrada
    
    def setHoraEntrada(self, horaEntrada:str):
        self.__horaEntrada=horaEntrada

    def getHoraSalida(self):
        return self.__horaSalida
    
    def setHoraSalida(self,horaSalida:str):
        self.__horaSalida= horaSalida
    
    def toString(self):
        return f"{self.__tipoVehiculo} {self.__placa} {self.__horaEntrada} {self.__horaSalida}"

