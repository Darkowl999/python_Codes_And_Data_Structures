"""
Lista Enlazada:

Las listas enlazadas son estructuras de datos semejantes a los arrays(arreglos o listas en python)
salvo que el acceso a un elemento no se hace mediante un indice sino mediante un puntero

Lista Enlazada Simple:

La lista enlazada basica es la lista enlazada simple la cual tiene un enlace por nodo, este
enlace acepta al siguiente nodo en la lista o al valor null o None si es el ultimo nodo

"""
#clase nodo
class Nodo:

    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

#clase lista simple
class ListaSimpleEnlazada():
    def __init__(self):
        self.primero=None#esta vendria ser la cabecera
        self.ultimo=None

    def estadoLista(self):
        return self.primero==None

    def agregarUltimo(self):
        if self.estadoLista()==True:
            self.primero









