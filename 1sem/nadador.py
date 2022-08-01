idade=int(input("Digite a sua idade : "))


if idade>30:
    print("Sua categoria é Senior")
elif 16<=idade<=30:
    print("sua categoria é adulto") 
elif 11<=idade<=15:
    print("sua categoria é adolescente")
elif 8<=idade<=10:
    print("sua categoria é juvenil")
else:
    print("sua categoria é infantil")           