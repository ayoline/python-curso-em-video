housePrice = float(input('Digite o valor da casa: '))
salaryBuyer = float(input('Digite qual é o salário do comprador: '))
yearsToPay = int(input('Digite em quantas anos será paga a casa: '))

maxPerMonth = (salaryBuyer*30)/100
valorPerMonth = housePrice/(yearsToPay*12)

if(valorPerMonth > maxPerMonth):
    print('Voce não pode comprar a casa pois compromete mais de 30% do salario')   
else:
    print(f'O emprestimo será liberado e voce terá que pagar R$ {round(valorPerMonth,2) },' 
    f'durante {(yearsToPay*12)} meses!')