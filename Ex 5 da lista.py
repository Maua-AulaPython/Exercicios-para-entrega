from math import *

X= float(raw_input("digite o valor da coordenado do eixo X: "))#4010210.546#km
Y=float(raw_input("digite o valor da coordenado do eixo Y: "))#-4260166.288#km
Z=float(raw_input("digite o valor da coordenado do eixo Z: "))#-2533008.133 #km

E=0.00669454185
a=6378160 #km
lambida= (atan(Y/X))*(180/pi)# graus
N=1
h=0
i=0
P=sqrt((X**2)+(Y**2))
while (i<10):
    i=i+1
    tanteta=((Z/P)*(1-E*(N/(h+N)))**(-1))
    teta=atan(tanteta)
    N=(a/(sqrt(1-E*((sin(teta))**2))))
    h=(P/cos(teta))-N
"""
print teta*(180/pi)

print lambida

print h*1000
"""
print ("sua latitude e: {0} ". format(teta*(180/pi)))
print ("sua altitude : {0} ". format(h*1000))
print ("sua longitude : {0} ". format(lambida))

# Nota: 0.9
# O enunciado solicitava criar uma função!
# Dica: O método `math.degrees` converte radianos para graus
