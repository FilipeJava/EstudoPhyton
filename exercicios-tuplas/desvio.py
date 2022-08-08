import math
def media(tupla):
    j=0
    soma=0
    while j<len(tupla):
        soma=soma+tupla[j]
        j=j+1    
    return soma/len(tupla)


def desvioPadrao(tupla):
    i = 0
    soma=0
    diferenca=0
    desvio=0
    mediaDesvio=media(tupla)
    while i<len(tupla):
        diferenca = (mediaDesvio-tupla[i])**2
        soma=soma+diferenca
        i=i+1
    desvio= math.sqrt(soma/mediaDesvio)
    return desvio

minhaTup=(3,7,6,5,4)

x=desvioPadrao(minhaTup)
print(x)
