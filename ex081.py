my_list = []

while True:
    my_list.append(int(input('Digite um número qualquer: ')))
    yes_or_not = input('Deseja sair?(S/N): ').lower()

    if yes_or_not == 's':
        my_list.sort(reverse=True)
        
        print(f'Voce digitou {len(my_list)} números!')
        print(f'A lista em ordem Decrescente é: {my_list}')

        if (my_list.count(5) > 0):
            print('O número 5 aparece na lista!')
        else:
            print('O número 5 não aparece na lista')
        break
    elif yes_or_not != 'n':
        while yes_or_not != 'n':
            print('Digite uma opção válida!')
            yes_or_not = input('Deseja sair?(S/N): ').lower()
print('-=' * 30)
print('FIM')
