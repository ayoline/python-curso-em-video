salario = float(input('Digite o seu salário em R$: '))

if(salario > 1250):
    salario = (salario * 10)/100
    print(f'O seu aumento salarial foi de 10%: R${salario}')
else:
    salario = (salario * 15)/100
    print(f'O seu aumento salarial foi de 15%: R${salario}')
    