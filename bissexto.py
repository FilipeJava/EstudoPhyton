dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

if 1<=dia<=31 and 1<=mes<=12:
    if dia==29:
        if mes==2:
            if ano%4==0 and ano%100!=0 or ano%400==0:
                print(dia, mes, ano)    
            else:            
                print("dia invalido para esse ano")    
    else:
        print(dia, mes, ano)

else:
    print("invalido")    
    