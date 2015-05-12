from math import sqrt

lista=[(12,0),(11,0),(10,0),(0,1),(20,0)] # lista de pontos


def tamanho (b,s):
    x=(b[0])+(s[0])
    y=(b[1])+(s[1])
    d= sqrt((x**2)+(y**2))
    return d


novadistancia=0
for i in range (len(lista)):
    for j in range(len(lista)):
        if (i==j):
            pass
        else:
            d=tamanho((lista[i]),(lista[j]))
            if (novadistancia<=d):
                novadistancia=d
print ("a lista de pontos ja foi criada pelo programador")
print ("portanto o valor da maior distancia entre dois pontos dela sempre sera o mesmo")
print ("sendo ele:")
print d

# Nota: 0.8
# O enunciado solicitava criar uma função!
