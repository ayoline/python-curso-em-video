from sqlalchemy import false


peopleList = []
max = min = 0

while True:
    person = []
    person.append(input('Digite o nome da pessoa: '))
    person.append(int(input('Digite o peso da pessoa: ')))

    if len(peopleList) == 0:
        max = min = person[1]
    else:
        if person[1] > max:
            max = person[1]
        if person[1] < min:
            min = person[1]

    peopleList.append(person[:])

    yes_or_not = input('Deseja continuar?(S/N): ').lower()

    if yes_or_not == 'n':
        break

print('=' * 30)
print(f'Ao todo voce cadastrou {len(peopleList)} pessoas')
print(f'O maior peso foi de {max} kg. ',end='')
for p in peopleList:
    if p[1] == max:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi de {min} kg. ', end='')
for p in peopleList:
    if p[1] == min:
        print(f'[{p[0]}] ', end='')
print()