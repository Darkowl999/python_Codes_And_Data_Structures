#POLIMORFISMO EJEMPLO BASICO

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("me desplazo utilizando seis ruedas")


def desplazamientoVehiculo(vehiculo):#aca se aplica el polimorfismo
    vehiculo.desplazamiento() 

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)