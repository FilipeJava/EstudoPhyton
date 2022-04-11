entrada = int(input("Digite a sequencia a ser Somada ?"))
soma=0
while entrada !=0:
    if entrada%2 == 0:
        soma=soma+entrada
        entrada =int(input("Digite o proximo da sequencia ?"))
    else:
        entrada =int(input("Digite o proximo da sequencia ?"))

print(soma)    