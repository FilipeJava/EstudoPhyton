

def interseccao(listaA,listaB):
    lista_resposta=[]
    for x in listaA:
        if x in listaB:
            lista_resposta.append(x)
    return lista_resposta