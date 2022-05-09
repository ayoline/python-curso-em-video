import math


numbers = []
menu = -1

numbers.append(float(input('Digite um numero: ')))
numbers.append(float(input('Digite um novo numero: ')))

while(menu != 5):
    print('Escolha uma das opções:')
    print('[1] Somar\n[2] Multiplicar\n[3] Maior número\n[4] Novos números\n[5] Sair')
    menu = int(input(''))

    if(menu == 1):
        print(f'A soma dos numeros digitados é: {sum(numbers)}')
    if(menu == 2):
        print(f'A multiplicação dos numeros digitados é: {math.prod(numbers)}')
    if(menu == 3):
        print(f'O maior numero da lista é: {max(numbers)}')
    if(menu == 4):
        numbers.append(float(input('Digite mais um numero: ')))
