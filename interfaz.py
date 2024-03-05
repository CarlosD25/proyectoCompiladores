from Parqueadero import *
from Carro import *
from Moto import *



reiniciarMP = True
miParqueadero = Parqueadero("Mi parquedoro", "Mz10C35", 30)


def ingresar_vehiculo():
    tipoVehiculo =input("Ingrese el tipo de vehiculo: ").lower()
    placa =input("Ingrese la placa del vehiculo: ").lower()
    horaDeEntrada =input("Ingrese la hora de ingraso del vehiculo: ").lower()
    if tipoVehiculo == "carro" or tipoVehiculo =="moto": 
        if tipoVehiculo == "carro":
            mivehciulo = Carro(tipoVehiculo, placa, horaDeEntrada,None, input("Ingrese el numero de puertas del carro: "))
        if tipoVehiculo == "moto":
            mivehciulo = Moto(tipoVehiculo, placa, horaDeEntrada,None, int(input("Ingrese el cilindraje de la moto: ")))
    miParqueadero.registrarVehiculo(mivehciulo,int(input("Ingrese el puesto del vehiculo: ")))

def eliminar_vehiculo():
    placa = input("Ingrese la placa del vehiculo: ").lower()
    horaSalida =input("Ingrese la hora de salida del vehiculo: ").lower()
    miParqueadero.eliminarVehiculo(placa, horaSalida)


while reiniciarMP:

    #1.  Registrar vehiculo
    # 
    #
    # miparquedadro.registrarVehiculo(miVehiculo) 
    menuP = f"-------------------------------------\nBienvenido Al parqueadero {miParqueadero.getNombre()}\n\n1.Registrar Vehiculo\n2.Eliminar Vehiculo\n3.Mostrar Parqueadero\n4.Salir del Programa\n-------------------------------------"
    print(menuP)
    opcionMenup = int(input("Elija una opción: "))
    if(opcionMenup == 1):
        ingresar_vehiculo()
    if(opcionMenup == 2):
        eliminar_vehiculo()
    if(opcionMenup == 3):
        print(miParqueadero.mostrarParqueadero())
    if(opcionMenup == 4):
        reiniciarMP = False