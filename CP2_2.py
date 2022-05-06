
n = float(input("Digite a quantidade de produtos: " ))
valorAtual = float(input("Digite o valor Atual do Produto : " ))
valorRejustado= float(input("Digite o valor Reajustado do Produto : " ))

maiorPercentual =(valorRejustado-valorAtual)/valorAtual
maiorPreco=valorRejustado-valorAtual



while(n>1):
    valorAtual = float(input("Digite o valor Atual do Produto 1: "))
    valorRejustado= float(input("Digite o valor Reajustado do Produto 1: "))
    maiorP= valorRejustado-valorAtual
    maiorPer =((valorRejustado-valorAtual)/valorAtual)
	
    if(maiorPercentual<maiorPer):
	    maiorPercentual=maiorPer
	    
    if(maiorPreco<maiorP):
        maiorPreco=maiorP
    n=n-1
	
		
	
print("O maior em preco R$" ,maiorPreco)
print(f'O maior em Percentual:{maiorPercentual:.2%}')
		
		
		
			
			

