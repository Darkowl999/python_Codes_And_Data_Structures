"""
ArbolBinario(): crea una nueva instancia de un árbol binario.
obtenerHijoIzquierdo() :devuelve el árbol binario correspondiente al hijo izquierdo del nodo actual.
obtenerHijoDerecho(): devuelve el árbol binario correspondiente al hijo derecho del nodo actual.
asignarValorRaiz(valor): almacena el objeto del parámetro valor en el nodo actual.
obtenerValorRaiz(): devuelve el objeto almacenado en el nodo actual.
insertarIzquierdo(valor): crea un nuevo árbol binario y lo instala como el hijo izquierdo del nodo actual.
insertarDerecho(valor): crea un nuevo árbol binario y lo instala como el hijo derecho del nodo actual.

"""

class Arbol():
#este es un simple metodo constructor
    def __init__(self,objetoRaiz):
        self.clave=objetoRaiz
        self.hijoIzquierdo=None
        self.hijoDerecho=None

#metodo para insertar un nodo mediante el lado izquierdo o hijo izquierdo
    def insertarIzquierdo(self,nuevoNodo):
        if self.hijoIzquierdo==None:
            self.hijoIzquierdo=Arbol(nuevoNodo)
        else:
            t=Arbol(nuevoNodo)
            t.hijoIzquierdo=self.hijoIzquierdo
            self.hijoIzquierdo=t        

#metodo para insertar un nodo mediante el lado derecho o hijo derecho

    def insertarDerecho(self,nuevoNodo):
        if self.hijoDerecho==None:
            self.hijoDerecho=Arbol(nuevoNodo)
        else:
            t=Arbol(nuevoNodo)
            t.insertarIzquierdo=self.hijoDerecho
            self.hijoDerecho=t
#metodos de acceso para la estructura de datos como tal

    def obtenerHijoDerecho(self):
        return self.hijoDerecho
    
    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo
    
    def asignarValorRaiz(self,obj):
        self.clave=obj
    
    def obtenerValorRaiz(self):
        return self.clave
        
#creamos y hacemos pruebas de nuestro simplearbolBinario

r = Arbol('a')
print(r.obtenerValorRaiz())
print(r.obtenerHijoIzquierdo())
r.insertarIzquierdo('b')
print(r.obtenerHijoIzquierdo())
print(r.obtenerHijoIzquierdo().obtenerValorRaiz())
r.insertarDerecho('c')
print(r.obtenerHijoDerecho())
print(r.obtenerHijoDerecho().obtenerValorRaiz())
r.obtenerHijoDerecho().asignarValorRaiz('hola')
print(r.obtenerHijoDerecho().obtenerValorRaiz())





















