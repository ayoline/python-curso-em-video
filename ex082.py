my_list = []
listEven = []
listOdd = []

while True:
    tempNumber = int(input('Digite um número qualquer: '))
    my_list.append(tempNumber)

    if tempNumber % 2 == 0:
        listEven.append(tempNumber)
    else:
        listOdd.append(tempNumber)
        
    yes_or_not = input('Deseja sair?(S/N): ').lower()

    if yes_or_not == 's':    
        print(f'A lista completa é {my_list}')
        print(f'O numeros pares são {listEven}')
        print(f'Os numeros impares são {listOdd}')
        break
    
    elif yes_or_not != 'n':
        while yes_or_not != 'n':
            print('Digite uma opção válida!')
            yes_or_not = input('Deseja sair?(S/N): ').lower()

print('-=' * 30)
print('FIM')
