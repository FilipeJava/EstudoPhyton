
def imprime_resultado(campeao,lista):
    for pais in lista:
        if pais != campeao:
            print(campeao,pais)




paises = ["Alemanha","Argentina"," Bélgica"," Brasil"," Colômbia"," Costa Rica"," França" , "Holanda"]



# i=0
# while(i<len(paises)):
#     imprime_resultado(paises[i],paises)
#     i=i+1 

for champion in paises:
    imprime_resultado(champion,paises)