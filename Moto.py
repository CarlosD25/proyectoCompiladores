from Vehiculos import *

## Herencia 
class Moto(Vehiculo):
    def __init__(self, tipoVehiculo, placa, horaEntrada, horaSalida, cilindraje):
        super().__init__(tipoVehiculo, placa, horaEntrada, horaSalida)
        self.__cilindraje = cilindraje

    def get_cilindrage(self):
        return self.__cilindraje