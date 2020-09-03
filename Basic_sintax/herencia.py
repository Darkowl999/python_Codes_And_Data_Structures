#HERENCIA EN PYTHON

class Vehiculos():
#constructor de oficio
    def __init__(self,marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frenar=False
#Comportamientos o metodos de tipo vehiculo

    def arrancar(self):
        self.enmarcha=True

    def acelera(self):
        self.acelera=True

    def frenar(self):
        self.frenar=True

    def estado(self):
        print("Marca :",self.marca, "\n Modelo :", self.modelo,"\nEn marcha :",self.enmarcha
              ,"\n Acelerando :", self.acelera,"\n Frenando :",self.frenar)

#Herencia en python

class Furgoneta(Vehiculos):#esta clase hereda de la clase vehiculos
    #metodos propios de la clase
    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"


class Moto(Vehiculos):#esta clase hereda de la clase vehiculos
#PROPIOS METODOS DE LA CLASE

#PROPIEDADES
    hcaballito=""

    def caballito(self):# este es un metodo propio de la clase
      self.hcaballito="Voy haciendo el caballito"
#Sobreescribir el metodo estado
    def estado(self):#Acá se sobreescribio el metodo caballito
        print("Marca :",self.marca, "\n Modelo :", self.modelo,"\nEn marcha :",self.enmarcha
              ,"\n Acelerando :", self.acelera,"\n Frenando :",self.frenar,"\n",self.hcaballito)


miMoto=Moto("honda","cbr")
miMoto.caballito()
miMoto.estado()
print("_________________________________________________________")
print("aca esta la furgoneta")
mifurgoneta=Furgoneta("FORD","250")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))






















