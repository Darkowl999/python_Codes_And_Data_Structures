"""
Ordenamiento por inseccion
Funcionamiento:

1- Recorremos cada elemento de la lista
2- cada elemento de la lista se ordena si a su izquierda tienen un elemento mayor que el actual
3- si es correcto el paso anterior, se hace el intercambio de valores
4- el elemento se sigue recorriendo hacia la izquierda hasta que tenga un elemento menor que él

"""

lista=[5,10,3,12,10,6]

for i in range(1,len(lista)):
    aux= lista[i]
    j=i-1
    while j>= 0 and aux<lista[j]:
        lista[j+1]=lista[j]
        lista[j]=aux
        j=1
print(lista)


