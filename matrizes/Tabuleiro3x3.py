tabuleiro =[]
i=0
while i<3:
    tabuleiro.append(['']*3)
    i=i+1

for linha in tabuleiro:
    print(linha)    

print()

tabuleiro[0][0]='X'
tabuleiro[1][1]='O'
tabuleiro[2][2]='X'

for linha in tabuleiro:
    print(linha)