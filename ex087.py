matriz = [[0,0,0],[0,0,0],[0,0,0]]
evenSum = 0
lastColumnSum = 0
secondLineMax = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite o numero da posição [{i},{j}]: '))

for i in range(0,3):
    print()
    for j in range(0,3):
        num = matriz[i][j]
        if (num % 2) == 0:
            evenSum += num
        if j == 2:
            lastColumnSum += num
        if i == 1:
            if num > secondLineMax: 
                secondLineMax = num

        print(f'[ {matriz[i][j]} ]',end='')

print('\n')
print(f'A soma dos valores pares é: {evenSum}')
print(f'A soma dos valores da terceira coluna é: {lastColumnSum}')
print(f'O maior valor da segunda linha é: {secondLineMax}\n')