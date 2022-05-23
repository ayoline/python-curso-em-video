list_num = []
yes_or_not = ''

while True:
    num_temp = int(input('Digite um numero qualquer: '))

    if (list_num.count(num_temp) > 0):
        print('O número não será adicionado, pois já existe!\n')
    else:
        list_num.append(num_temp)
        print('O numero foi adicionado com sucesso!\n')

    while True:
        yes_or_not = input('Você desaja continuar?(S/N): ').lower()
        if yes_or_not == 's':
            break
        elif yes_or_not == 'n':
            list_num.sort()
            print(f'Voce digitou os valores: {list_num}')
            break
        else:
            print('Digite um valor valido!')
    
    if(yes_or_not == 'n'):
        break