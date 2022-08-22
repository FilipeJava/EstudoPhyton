
def inverteLista(lista):
    listainvertida=[]
    contador=len(lista)-1
    while contador>=0:
        listainvertida.append(lista[contador])
        contador=contador-1
    return listainvertida




minhaLista =[]

i=0

while i<3:
    entrada = input("Digite o valor a ser inserido na lista: ")
    minhaLista.append(entrada)
    i=i+1

z =inverteLista(minhaLista)

print(z)