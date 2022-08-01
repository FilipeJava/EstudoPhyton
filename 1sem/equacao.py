import math
from winreg import DeleteValue

print("Dada a funçã ax^2 + bx + c = 0 ")
a = float(input("Digite o Termo a: "))
b = float(input("Digite o Termo b: "))
c = float(input("Digite o Termo c: "))
delta= (b**2)-4*a*c
print("O valor de dela é: ",delta)

if a==0:
    print("trata-se de uma quação do primeiro grau")
elif delta<0:
    print("não exite raiz")
elif delta>0:
    x1=(-b+(math.sqrt(delta)))/2*a
    x2=(-b-(math.sqrt(delta)))/2*a
    print("A raiz x1 = ",x1)
    print("A raiz x2 = ",x2)
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    print("X1=X2 com valor de : ",x1)

