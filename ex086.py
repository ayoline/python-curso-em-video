matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite o numero da posição [{i},{j}]: '))

for i in range(0,3):
    print()
    for j in range(0,3):
        print(f'[ {matriz[i][j]} ]',end='')

print()