"""
Busqueda Binaria
 Funcionamiento :
 Buscar datos de una coleccion de datos

 ventajas:
 Realiza menos comparaciones que el metodo de busqueda lineal

 Requisitos antes de realizar dicho algoritmo
 tener la lista ordenada de manera ascendente (MENOR A MAYOR)

 algoritmo:
 1.- Calcular el punto medio (Izquierda + derecha) /2
 2.- comparar el punto medio con el dato a buscar
 3.- si es igual el dato al punto medio, retornar indice
 4.- si el dato a buscar es mayor que el punto medio, izquierda es igual al valor medio +1
 5.- si el dato a buscar es menor que el punto medio , derecha es igual al valor medio -1
 6.- se seguira ejecutando siempre y cuando izquierda sea menor o igual a derecha
"""
def busqueda_binaria(dato):
    izquierda=0
    derecha=len(lista)-1
    while izquierda<=derecha:
        medio=(izquierda+derecha)//2
        if dato == lista[medio]:
            return medio
        elif dato <lista[medio]:
            derecha = medio-1
        else:
            izquierda=medio+1
    return None
def buscar(dato):
    if busqueda_binaria(dato)== None:
        return "el dato %d no se encontro"
    else:
        return "el dato %d se encontro en el indice : %d"%(dato,busqueda_binaria(dato))


lista=[5,12,15,30,50,65,70,87,88,96]

for i in range(len(lista)):
    print("[%d] => %d"%(i,lista[i]))
print(buscar(50))