"""
Es una estructura de datos, caracterizada por ser una secuencia de elementos en
la que la operacion de inserccion (push) se realiza por un extremo y la operacion
de extraccion (pop) por el otro. Tambien se le llama estructura
FIFO (First in First Out, primero en entrar primero en salir),
debido a que el primer elemento en entrar sera tambien el primer elemento en salir.


Operaciones:
1.- Insertar
2.- Eliminar
3.- Buscar
4.- estado de la cola (vacia o con elementos)
5.- retornar el elemento frontal
6.- retornar el tamaño de la cola
7.- ETC
"""

class Cola():

    def __init__(self):
        self.cola=[]
        self.size=0

    def empty(self):
        return len(self.cola)==0

    def push(self,dato):
        self.cola= self.cola[dato]
        self.size=self.zize+1

    def pop(self):
        if self.empty():
            print("la cola esta vacia")
        else:
            self.cola=[self.cola[i] for i in range(1,self.size)]
            self.size=self.size-1


    def show(self):
        n= self.size-1
        while n>-1:
            print("[%d] => %d" %(n,self.cola[n]))
            n= n-1

    def front(self):
        if self.empty():
            print("cola vacia")
        else:
            print("primer dato %d"%self.cola[0])
   











