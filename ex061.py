num = int(input('Digite o primeiro numero da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = num + (10 - 1) * razao

while(num != ultimo):
      print(f'{num}',end=' => ')
      num = num + razao
print('FIM')
