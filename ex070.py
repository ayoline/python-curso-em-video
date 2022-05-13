names = []
prices = []
continue_or_not = ''
expensives = 0

while True:
    while True:
        name = input('Digite o nome do produto: ')
        if(name == ''):
            print('Você precisa digitar algum nome!')
        else:
            names.append(name)
            break
    while True:
        price = float(input('Digite o valor do produto: R$ '))
        if(price < 0):
            print('O valor precisa ser positivo!')
        else:
            if(price > 1000):
                expensives += 1
            prices.append(price)
            break
    while True:
        continue_or_not = input('Deseja continuar?(S/N): ')
        if(continue_or_not.lower() != 's' and continue_or_not.lower() != 'n'):
            print('Digite um valor válido!')
        elif(continue_or_not.lower() == 'n'):
            print(f'O total da compra foi: R$ {sum(prices)}')
            print(f'Existem {expensives} produtos custando mais de R$ 1000,00')
            index_min = prices.index(min(prices))
            print(f'O produto {names[index_min]} de valor R$ {prices[index_min]} é o valor mais barato')
            break
        else:
            break
    
    if(continue_or_not.lower() == 'n'):
        print('FIM')
        break