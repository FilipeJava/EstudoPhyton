diasUteis = float(input("Digite o numero de dias Uteis do mes referente: "))
horasTrabalhadas =float(input("Digite o total de horas trabalhadas: "))
valorHora = float(input("Digite o valor do salário por Hora: "))

horasRegulares = diasUteis*8
salarioRegular = horasRegulares*valorHora

if horasTrabalhadas>=horasRegulares:
    horaExtra = horasTrabalhadas-horasRegulares
    salarioExtra = horaExtra*valorHora
    print("O valor de hora extra para o funcionário é de R$ ",salarioExtra)
    print("O salario final a receber é de : R$ ",salarioRegular+horaExtra)
else:
    print("Voce trabalhou ",horasTrabalhadas," horas seu salario proporcional é de ",horasTrabalhadas*valorHora)



