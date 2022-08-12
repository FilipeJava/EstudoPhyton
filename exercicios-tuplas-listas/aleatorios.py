import random

def randonNumber(numero):
    contador =0
    listaRandon=[]
    while contador<numero:
        numeroAleatorio=random.randint(1,1001)
        listaRandon.append(numeroAleatorio)
        contador=contador+1
    return listaRandon


x=randonNumber(5)

print(x)
