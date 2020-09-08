"""
Nodo:

En programacion, concretramente en estructuras de datos, un nodo es uno de los elementos
de una lista enlazada, de un arbol o de un grafo, cada nodo sera una estructura o registro
que dispondrá de varios campos, y al menos uno de esos campos sera un puntero o referencia a otro nodo
de forma que, conocido un nodo, a partir de una referencia. sera posible en teoria tener acceso a otros
nodos de la estructura
"""
class Nodo():

    def __init__(self,dato,siguiente=None):
        self.dato=dato
        self.siguiente=siguiente

    def __str__(self):
        return str(self.dato)

def recorrer(nodo):
    while nodo!=None:
        print(nodo.dato)
        nodo=nodo.siguiente

nodo4=Nodo(12)
nodo3=Nodo(45,nodo4)
nodo2=Nodo(67,nodo3)
nodo1=Nodo(89,nodo2)

recorrer(nodo1)
