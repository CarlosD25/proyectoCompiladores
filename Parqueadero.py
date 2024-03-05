from Vehiculos import *
from Moto import *
from Carro import *

class Parqueadero:

    def __init__(self, nombre:str, direccion:str, capacidad:int):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__capacidad = capacidad
        self.__listaVehiculos = [None] * self.__capacidad 

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion=direccion
    
    def getCapacidad(self):
        return self.__capacidad
    
    def setCapacidad(self, capacidad):
        self.__capacidad=capacidad


    def registrarVehiculo(self,vehiculo:Vehiculo, puesto: int):
        if puesto > 0 and puesto <= self.__capacidad:
            if self.__listaVehiculos[puesto-1] == None:
                self.__listaVehiculos[puesto-1] = vehiculo
            else:
                print("El puesto está ocupado")    
        else:
            print("Elija un puesto valido")

    def eliminarVehiculo(self,placa, horaSalida:str):
        for vehiculo in self.__listaVehiculos:
            if vehiculo != None:
                if vehiculo.getPlaca() == placa:
                    vehiculo.setHoraSalida(horaSalida)
                    print(vehiculo.toString())
                    self.__listaVehiculos.remove(vehiculo)
                    

    def mostrarParqueadero(self):
        resultado= ""
        for i in range (len(self.__listaVehiculos)):
            if self.__listaVehiculos[i] == None:
                resultado+=f"Espacio {i+1} (Desocupado)\n"
            else:
                resultado+=f"Espacio {i+1} (Ocupado)\n" 
                vehiculo = self.__listaVehiculos[i]
                resultado+=f"----Espacio {vehiculo.toString()}\n"
        return resultado

    

   

#parqueadero=Parqueadero("hola","DIG16D",10)

#my_vehiculo = Moto("Moto","332hh","112:00")
#vehiculoCarro = Carro("Carro","332ha","112:00")
#parqueadero.registrarVehiculo(my_vehiculo, 1)
#parqueadero.registrarVehiculo(vehiculoCarro, 10)


#print("Parqueadero con los dos carros registrados: ")
#print(parqueadero.mostrarParqueadero())
#print("\nVehiculo eliminado:")
#parqueadero.eliminarVehiculo("332hh", "hola mundo")
#print("\nParqueadoro despues de eliminar el vehiculo")
#print(parqueadero.mostrarParqueadero())
