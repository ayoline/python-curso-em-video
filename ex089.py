studentsList = []

while True:
    tempList = []
    tempList.append(input('Digite o nome do aluno: ')) 
    tempList.append(float(input('Digite a primeira nota: ')))
    tempList.append(float(input('Digite a segunda nota: ')))
    tempList.append((tempList[1] + tempList[2])/2)

    studentsList.append(tempList)

    yes_or_not = input('\nDeseja continuar?(S/N) ').lower()
    if yes_or_not == 'n':
        break

print()
print('=' * 48)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 48)
for i, a in enumerate(studentsList):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    # print(f'{i}   {studentsList[i][0]}         {studentsList[i][3]}')

while True:
    numStudent = int(input(f'\nDeseja ver as nota de qual aluno?(999=sair) '))

    if numStudent == 999:
        break
    elif numStudent > len(studentsList) -1:
        print('Digite uma posição valida!')
    else:
        print(f'Notas de {studentsList[numStudent][0]} são {studentsList[numStudent][1:3]}')



