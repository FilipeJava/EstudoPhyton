n = int(input("Informe a qtd de números: "))
v = []

for i in range(n):
    num = float(input("digite num: "))
    v.append(num)
i = 0
j = n - 1
listaSoma=[]
while i <= j:
    listaSoma.append(v[i] + v[j])
    i = i + 1
    j = j - 1

print(v,listaSoma)


    
