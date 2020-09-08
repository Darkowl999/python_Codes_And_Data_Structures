#Algoritmo de busqueda lineal
"""
Busqueda Lineal:

Funcionamiento:

1:Recorrer cada elemento de la lista:
2: Ir comparando el elemento que desea buscar con cada elemento de la lista
3: En caso de ser encontrado,retornar el indice en el que se encuentra, en caso contrario retornar
falso,None, etc:

"""

def busquedaLineal(dato):
    for x in range(len(lista)):
        if lista[x]==dato:
            return x
    return None

def buscar(dato):
    if busquedaLineal(dato)==None:
        return "el dato no se encontro "(dato)
    else:
        return "el dato se encontro" (dato,busquedaLineal(dato))
lista=[12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98] #esta es una variable global

print(buscar(2))