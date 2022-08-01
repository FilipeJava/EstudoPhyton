def perfect(n):
    contador=1
    soma=0
    while(contador<=n):
        if(n%contador==0):
            soma=soma+contador
        if(n==soma):
            return n
        contador=contador+1    


