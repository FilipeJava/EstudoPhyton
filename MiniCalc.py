num1 =float(input("Digite o primeiro numero"))
operador = input("digite um dos 5 operadores *,/,+,-,%")
num2 =float(input("Digite o segundo numero"))

if operador=="*":
    resultado = num1*num2
else:
    if operador=="/":
        if num2!=0:
           resultado=num1/num2
        else:
            print("Impossivel divisão por zero")
    else:
        if operador=="+":
            resultado=num1+num2 
        else:
            if operador=="-":
                resultado=num1-num2
            else:
                resultado=num1%num2

print("Resposta : {}".format(resultado))                
                
                                          