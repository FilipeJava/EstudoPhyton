from xml.dom.minidom import Notation


qtdAlunos = int(input("Digite o numeros de alunos:"))


i=0
soma=0
listaNotas=[]
while i<qtdAlunos:
    nota = float(input("Digite a nota do Alunos"))
    listaNotas.append(nota)
    soma=soma+nota
    i=i+1

media = soma/qtdAlunos

abaixo_media=0
acima_media=0
for nota in listaNotas:
    if nota>=media:
        acima_media=acima_media+1
    else:
        abaixo_media=abaixo_media+1    

print("A média da Sala foi {}".format(media))
print("Quantidade de Alunos Acima da Média:",acima_media) 
print("Quantidade de Alunos Abaixo da Média:",abaixo_media)



print(numeros)