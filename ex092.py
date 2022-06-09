dicEmployee = {}

dicEmployee['nome'] = input('Digite o nome: ')
dicEmployee['nascimento'] = input('Digite o ano de nascimento:')
dicEmployee['ctps'] = int(input('Digite o número da CTPS:(0 não tem) '))

if dicEmployee['ctps'] == 0:
    dicEmployee['ctps'] = 'Não possui'
else:
    dicEmployee['contratação'] = int(input('Qual o ano de contratação: '))
    dicEmployee['salário'] = float(input('Qual o salário?: '))
    dicEmployee['aposentadoria'] = dicEmployee['contratação'] + 35

print()
for x, y in dicEmployee.items():
    print(f'{x}: {y}')
print()
