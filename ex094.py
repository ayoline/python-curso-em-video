all_person = []
yes_or_not = ''
sum_ages = 0
average_age = 0
person = {}

while True:
    person.clear()
    person['Nome'] = str(input('Digite o nome da pessoa: '))
    
    while True:
        person['Sexo'] = str(input('Digite o sexo:(M/F) ')).upper()[0]
        if person['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F!')
    person['Idade'] = int(input('Digite a idade: '))
    sum_ages += person['Idade']
    all_person.append(person.copy())

    while True:
        yes_or_not = input('\nVocê deseja continuar?(S/N)').upper()[0]
        if yes_or_not in 'SN':
            break
        else:
            print('Digite um valor valido!')
    if yes_or_not == 'N':
        break

print(f'O grupo tem {len(all_person)} pessoas')
average_age = sum_ages / len(all_person)
print(f'A média de idade das pessoas é {average_age} anos')
print('As mulheres cadastradas foram: ', end='')
for m in all_person:
    if m['Sexo'] in 'F':
        print(f'{m["Nome"]} ', end='')

print()
print('Lista de pessoas que estão acima da média de idade: ')
for p in all_person:
    if p['Idade'] >= average_age:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('FIM')