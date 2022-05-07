num1 = int(input('Digite o primeiro numero da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = num1 + (10 - 1) * razao

for i in range(num1, ultimo + razao, razao):
    print(f'{i}',end=' => ')
print('FIM')