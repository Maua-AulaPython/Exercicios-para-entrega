from math import *
print ("bem vindo ao programa")
print ("vc vai digitar dois pontos e transformar em coordenada polar")
Ax=float(raw_input("Qual o valor do x do ponto A:"))
Ay=float(raw_input("Qual o valor do y do ponto A:"))
Bx=float(raw_input("Qual o valor do x do ponto B:"))
By=float(raw_input("Qual o valor do y do ponto B:"))
x=Ax-Bx
y=Ay-By
ang= atan(y/x)
moduloz= sqrt((x**2)+(y**2))
print ("o modulo e")
print moduloz
print ("o angulo e")
print ang

# Nota: 0.8
# O enunciado solicitava criar uma função!
