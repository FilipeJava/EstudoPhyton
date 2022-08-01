def primo (n):
    count =1
    prim=0
    while(count <=n):
        if(n%count==0):
            prim+=1
        count+=1 

    if(prim==2):
        return True
    else:
        return False

entrada=int(input("Digite a Sequencia que gostaria de numeros Primos? "))

contador=2

while (contador<=entrada):
    if(primo(contador)==True):
        print(contador)        
    contador=contador+1


    

   