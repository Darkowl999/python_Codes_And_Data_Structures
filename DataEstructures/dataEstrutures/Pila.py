"""
Pila:

Una pila es una lista ordenada o estructura de datos en la que el modo de acceso a sus elementos es de tipo
'LIFO' (Last In First Out, Ultimo en entrar es el primero en salir) que permite almacenar datos.

Para el manejo de los datos se cuenta con dos operaciones basicas: apilar(push) que coloca un objeto
en la pila, y su opearacion inversa, retirar o desapilar(pop), que retira el ultimo elemento apilado

OPERACIONES:
- Crear: se crea la pila vacio. (constructor)
- Tamaño: regresa el numero de elementos de la pila (size)
- Apilar: se añade un elemento a la pila (push)
- Desapilar: se elimina el elemento frontal de la pila (pop)
- Cima: devuelve el elemento que esta en la cima de la pila (top o peek)
- Vacia: devuelve cierto (true) si la pila está sin elementos o falso en caso que contenga uno (empty)

Las pilas pueden ser de tamaño estatico y dinamico, se pueden implementar listas, arreglos, colecciones
de datos o listas enlazadas.

"""

class Pila():
#constructor por defecto
    def __init__(self,size):
        self.lista=[]
        self.tope=0
        self.size=size


    def empty(self):
        if self.tope==0:
            return True
        else:
            return False

    def push(self,dato):
        if self.tope<self.size:
            self.lista=self.lista+[dato]
            self.tope=self.tope+1
        else:
            print("la pila está llena")

    def pop(self,dato):
        if self.empty():
            print("la pila esta vacia")
        else:
            self.tope=self.tope-1
            self.lista== [self.lista[x] for x in range(self.tope)]

    def show(self):
        i=self.tope-1
        while i>-1:
            print("[%d] => %d"%(i,self.lista[i]))
            i=i-1

    def size(self):
        return self.tope

    def top(self):
        return self.list[-1]



pila= Pila(5)
pila.push(2)
pila.push(24)
pila.show()
pila.pop(2)

















