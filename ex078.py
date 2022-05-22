numList = []

for i in range(0,5):
    numList.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=' * 50)
print(f'Você digitou os valores: {numList}')

print(f'O maior valor digitado foi o {max(numList)} na posição:', end=' ')
for i, j in enumerate(numList):
    if j == max(numList):
        print(f'...{i}', end=' ')

print(f'\nO menor valor digitado foi o {min(numList)} na posição:', end=' ')
for i, j in enumerate(numList):
    if j == min(numList):
        print(f'...{i}', end=' ')

print('\n', end='')
print('=' * 50)
print('FIM')
