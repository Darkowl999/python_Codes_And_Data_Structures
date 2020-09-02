#ACA SE USA FOR CON RANGE:
#for i in range(5,20,2):
#   print(f" valor de la variable {i}")

valido=False

email= input("introduce tu email")

for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
 print("Email incorrecto")