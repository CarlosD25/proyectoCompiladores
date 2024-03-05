from Vehiculos import *

## Herencia
class Carro(Vehiculo):
    def __init__(self,tipoVehiculo, placa, horaEntrada, horaSalida, puertas):
        super().__init__(tipoVehiculo, placa, horaEntrada, horaSalida)
        self.__puertas = puertas

    def get_puertas (self):
        return self.__puertas

