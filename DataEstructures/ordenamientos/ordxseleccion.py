"""
Ordenamiento por seleccion:
 Es una algoritmo que consiste en ordenar los elementos de manera ascendente o descendente

 Funcionamiento:
 -Buscar el dato mas pequeño de la lista
 -Intercambiarlo por el actual
 -Seguir buscando el dato mas pequeño de la lista
 -Intercambiarlo por el actual
 -es se repetira sucesivamente
"""
lista=[4,2,6,8,5,7,0]

for indice in range(len(lista)):
    minimo=indice
    for x in range(indice,len(lista)):
        if lista[x]<lista[minimo]:
            minimo=x
    aux=lista[indice]
    lista[indice]=lista[minimo]
    lista[minimo]=aux
    print(lista)
#REVISAR ESTE ALGORITMO DE MANERA CORRECTA