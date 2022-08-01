
cpf= 368707108
backup_cpf = cpf
soma = 0
mult = 2


while mult<=10:
    resto = cpf %10
    cpf = cpf//10
    
    soma = soma +resto *mult 
    mult = mult + 1

resto = soma%11
if resto<2:
    dc =0
else:
    dc = 11-resto        

    print(dc)