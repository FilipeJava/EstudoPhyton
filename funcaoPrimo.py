z=int(input("Digite o numero Para saber se é Primo ou não:"))

def primo (n):
    count =1
    prim=0
    while(count <=n):
        if(n%count==0):
            prim+=1
        count+=1 

    if(prim==2):
        return "Verdadeiro"
    else:
        return"Falso"
    

print(primo(z))        
     
    