entrada = int(input("Digite o numero para calcular Fibonacci ?"))
contador = 0
v1 = -1
v2= 1
v3=0
soma=0
while contador<=entrada:
    v3 = v1+v2
    v1=v2
    v2=v3
    contador=contador+1

print(v3)
    

    




