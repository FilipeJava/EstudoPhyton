coisas = [""]*10
contador=0

while contador<len(coisas):
    x = input("Digite o valor para preencher na Lista" )
    coisas[contador]=x
    contador=contador+1   


 
listaRevertida=[]
i=len(coisas)-1
while i>=0:
    listaRevertida.append(coisas[i])
    i=i-1

print(listaRevertida)


