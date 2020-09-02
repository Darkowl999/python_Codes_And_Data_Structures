#PROGRAMACION ORIENTADA A OBJETOS EN PYTHON
#EN POO UN OBJETO TIENE:
# -UN ESTADO. -PROPIEDADES -COMPORTAMIENTO

class Coche():
    #estas son las propiedades
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False
#comportamiento de la clase (Metodos)
#self hace referencia al propio objeto perteneciente de la clase es como un this en java
    def arrancar(self,arrancamos): #este es un comportamiento de la clase
        self.enMarcha=arrancamos
        if self.enMarcha:
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"


    def estado(self): #este es otro comportamiento de la clase
        print("El coche tiene  ",self.ruedas, "ruedas.  Un ancho de ", self.anchoChasis,"y un largo de ",self.largoChasis)

#aca se crea el primer objeto=> se instancio una clase
miCoche= Coche()

print("el largo del coche es ",miCoche.largoChasis)
print("el coche tiene",miCoche.ruedas," ruedas")
print(miCoche.arrancar(True))

miCoche.estado()

print("------------------------------------------------------------------------------------------------")

print("------------------------  A CONTINUACION CREAMOS EL SEGUNDO OBJETO -------------------------")

miCoche2=Coche()
print("el largo del coche es ",miCoche2.largoChasis)
print("el coche tiene",miCoche2.ruedas," ruedas")
print(miCoche2.arrancar(False))
miCoche2.estado()
#EVALUAR EL CODIGO EN CASO DE DUDA







