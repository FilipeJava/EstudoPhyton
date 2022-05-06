
entrada = int(input("Qual o tamanho da sequencia ?"))
a1 = int(input("Digite a sequencia ?"))
contador=1

if(entrada==1):
   print(contador)
else:    
    while(entrada>1):
        a2 = int(input("Digite a sequencia ?"))
        if(a1==a2):
                entrada=entrada-1
                a1=a2
        else:
                contador=contador+1
                entrada=entrada-1
                a1=a2    

print(contador)
