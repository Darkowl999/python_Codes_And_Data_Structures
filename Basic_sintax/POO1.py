#PROGRAMACION ORIENTADA A OBJETOS EN PYTHON
#EN POO UN OBJETO TIENE:
# -UN ESTADO. -PROPIEDADES -COMPORTAMIENTO

class Coche():
    #CONSTRUCTOR POR DEFECTO CON UN ESTADO INICIAL
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enMarcha=False

#comportamiento de la clase (Metodos)
#self hace referencia al propio objeto perteneciente de la clase es como un this en java
    def arrancar(self,arrancamos): #este es un comportamiento de la clase
        self.enMarcha=arrancamos
        if self.enMarcha:
            chequeo=self.__chequeoInterno()
        if self.enMarcha:
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"


    def estado(self): #este es otro comportamiento de la clase
        print("El coche tiene  ",self.ruedas, "ruedas.  Un ancho de ", self.anchoChasis,"y un largo de ",self.largoChasis)

    def __chequeoInterno(self): #ESTE METODO ESTÁ ENCAPSULADO
        print("Realizando un chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False

#aca se crea el primer objeto=> se instancio una clase
miCoche= Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("------------------------------------------------------------------------------------------------")

print("------------------------  A CONTINUACION CREAMOS EL SEGUNDO OBJETO -------------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()






#EVALUAR EL CODIGO EN CASO DE DUDA

#UN CONSTRUCTOR ES UN METODO ESPECIAL QUE LE DA UN ESTADO INICIAL A LOS OBJETOS#


