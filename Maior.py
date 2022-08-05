
# def max (colecao):
#     i=0
#     maior=0
#     while i<len(colecao):
#         if (i==0):
#             maior=colecao[i] 

#         if(colecao[i]>maior):
#             maior=colecao[i]
#         i=i+1
#     print(maior)    


def media(tupla):
    j=0
    soma=0
    while j<len(tupla):
        soma=soma+tupla[j]
        j=j+1    
    return soma/len(tupla)


def max (colecao):
    i=0
    maior=colecao[0]
    while i<len(colecao):
       if colecao[i]>maior:
        maior=colecao[i]
       i=i+1
    return maior


numeros=(1,5,9.5,14)

y=media(numeros)
print(y)

colecaoNum=(1,214,2)       
x=max(colecaoNum)
print(x)


