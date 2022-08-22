import random


def insere (n):
    minhaLista=[]
    i=0
    while i<n:
        num = random.randint(1,1001)
        minhaLista.append(num)
        i=i+1
    return minhaLista


       
z = insere(6)

print(z)