entrada = int(input("Qual o tamanho da sequencia ?"))
a1 = int(input("Digite a sequencia ?"))
contador=0

if(entrada ==1):
    while(entrada>1):
        a2 = int(input("Digite a sequencia ?"))
        if(a1==a2):
            contador = contador
        else:
            contador = contador+1      
    entrada=entrada-1
contador=1
print(contador)


