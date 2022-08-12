

def insereOrdenado(x,lista):
    i=0
    while i < len(lista) and lista[i]<x:
        i=i+1
    lista.insert(i,x)
    






minhaLista = [1,6,10,20,24,25,30,45]
insereOrdenado(13,minhaLista)
print(minhaLista)