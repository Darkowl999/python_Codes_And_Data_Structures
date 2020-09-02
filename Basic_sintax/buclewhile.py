#Bucle while  
#while condicion
#cuerpo del bucle

#i=1
#while i<=10:
#print("ejecucion"+str(i))
#print("termino la ejecucion")
edad=int(input("Introduce la edad por favor :  "))
while edad<0:
    print("Has ingreado una edad negativa: vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor"))

print("gracias por colaborar puedes pasar")
print("Edad del aspirante"+str(edad))