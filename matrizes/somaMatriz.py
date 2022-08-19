def soma (a,b):
    resp = []
    lin = len(a)
    col = len(a[0])
    i=0
    while i < lin:
        resp.append([0]*col )
        i=i+1
        
    for i in range(lin):
        for j in range(col):
            resp[i][j]=a[i][j]+b[i][j]
    return resp



matriz_um=[
             [1,1,1,1],
             [1,1,1,1],
             [1,1,1,1]
]
matriz_dois=[

            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
]


z = soma(matriz_um,matriz_dois)

print(z)