#condicionales para python
#condicional if en python 
#programa para introducir la nota por teclado
print("programa de evaluacion de notas de alumnos")
print("introduce tu calificacion por favor")

nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(int(nota_alumno)))

