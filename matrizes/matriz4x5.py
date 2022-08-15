
def populaMatriz(matriz):
    num = 1
    k=0
    while k<4:
        j=0 #percorre a coluna
        while j<5:
            matriz[k][j]=num
            num = num +1
            j=j+1
        k=k+1    

def dimensao(matriz):
    lin= len(matriz)
    col=len(matriz[0])
    return (lin,col)


matriz=[]
i=0

while i<4:
    matriz.append([0]*5)
    i=i+1

for linha in matriz:
    print(linha)


print() 

populaMatriz(matriz)

for linha in matriz:
    print(linha)





      