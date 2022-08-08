minhaTupla=("Filipe","Laranja", "oi","paralelepipedo")

# 1- len(indice[0]) atribuir a uma variavel maior//strMaior recebe indice[0] 
# 2-percorrer a tupla
# 3-a partir de cada indice usar len()para descobrir o tamanho de cada String
# 4-questionar se maior > minhaTupla[indice] 
#   

def maxString(colecao):
    maior = len(minhaTupla[0])
    strMaior=minhaTupla[0]
    i =0
    while i< len(colecao):
        if len(colecao[i])>maior:
            maior=len(colecao[i])
            strMaior=colecao[i]
        i=i+1    

    return(strMaior)



    
x=maxString(minhaTupla)
print(x)