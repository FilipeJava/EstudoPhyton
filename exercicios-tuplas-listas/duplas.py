def imprime(conjunto, pos):
    j = pos + 1
    while j < len(conjunto):
        print(conjunto[pos], conjunto[j])
        j = j + 1


col = ("Andre", "Bruno", "Cido", "Davi")

tam=len(col)-1
contador=0

while contador<tam:
    imprime(col,contador)
    contador=contador+1


