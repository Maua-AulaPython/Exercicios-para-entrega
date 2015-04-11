valor=0
b=[]
res=0
i=0
max=0
print ("digite quantos numeros vc quiser para fazer a media deles")
print ("quando desejar parar de inserir numeros, digite um numero negativo")
while valor>=0:
    i= i+1
    while True:
        try:
            valor=float(raw_input("numero %i da media:" %i))
            break
        except:
            print("vc digitou errado, tenta de novo")    
    if valor>=0:
        b.append(valor)
for g in b:
    res=res+g
resultado=res/(i-1)
print ("sua média é")
print resultado
for i in range (len(b)):
    if (max<b[i]):
        max=b[i]
print ("a maior nota é")
print (max)



print ("obrigado")
