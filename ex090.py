dictionary = {}

dictionary['name'] = input('Digite o nome: ')
dictionary['average'] = float(input('Digite a média '))

if dictionary['average'] >= 7:
    dictionary['status'] = 'Aprovado'
else:
    dictionary['status'] =  'Reprovado'

print(f'\nO nome é igual a: {dictionary["name"]}')
print(f'A média é igual a: {dictionary["average"]}')
print(f'A situação é igual a: {dictionary["status"]}\n')