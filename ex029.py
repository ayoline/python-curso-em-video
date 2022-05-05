velocity = int(input('Digite a velocidade do carro: '))

if(velocity > 80):
    print('Você foi multado por ultrapassar a velocidade máxima')
    print(f'Sua multa é de R$ {(velocity - 80)*7}')
else:
    print('Sua velocidade está dentro do limite')