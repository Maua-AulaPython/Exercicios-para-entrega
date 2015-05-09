valor=0
b=[]
res=0
i=0
print ("digite quantos numeros vc quiser para fazer a media deles")
print ("quando desejar parar de inserir numeros, digite um numero negativo")
while valor>=0:
    i= i+1
    valor=float(raw_input("numero %i da media:" %i))
    if valor>=0:
        b.append(valor)
for g in b:
    res=res+g
resultado=res/(i-1)
print resultado

# Nota: 1,0
# comentario: *
