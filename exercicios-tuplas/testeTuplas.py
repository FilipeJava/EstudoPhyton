estacao=("primavera","verão","outono","inverno")
print(estacao[1:3])



primos = (2,3,5,7) 

perfeitos=(6,28,492)

numeros = primos+perfeitos
print(type(numeros))
print(numeros)
print(len(numeros))

# percorrendo a tupla

sports = ("Futebol" , "Ginastica","Basquete","volei")
i=0
while i < len(sports):
    print(sports[i])
    i=i+1

for c in sports:
    print(c)