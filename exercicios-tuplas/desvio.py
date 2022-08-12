import math
import Maior


def desvioPadrao(tupla):
    i = 0
    soma=0
    diferenca=0
    desvio=0
    mediaDesvio=Maior.media(tupla)
    while i<len(tupla):
        diferenca = (mediaDesvio-tupla[i])**2
        soma=soma+diferenca
        i=i+1
    desvio= math.sqrt(soma/mediaDesvio)
    return desvio

minhaTup=(3,7,6,5,4)

x=desvioPadrao(minhaTup)
print(x)
