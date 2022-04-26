from ctypes import CFUNCTYPE
from re import X


x = int(input("digite o cpf:"))

cd= x%100
c3 = x//100%1000
c2 =x//100000%1000
c1= x//100000000

print(c1,".",c2,".",c3,"-",cd)