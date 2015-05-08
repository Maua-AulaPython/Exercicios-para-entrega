from math import sqrt
print ("bem vindo ao programa")
Ax=float(raw_input("Qual o valor do x do ponto A:"))
Ay=float(raw_input("Qual o valor do y do ponto A:"))
Bx=float(raw_input("Qual o valor do x do ponto B:"))
By=float(raw_input("Qual o valor do y do ponto B:"))
x=Ax-Bx
y=Ay-By
d= sqrt((x**2)+(y**2))
print ("a distancia entre os pontos e")
print d
