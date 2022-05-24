ListNumbers = []

for i in range(0,5):
    numTemp = int(input('Digite um valor qualquer: '))
    if i == 0 or numTemp > ListNumbers[-1]:
        ListNumbers.append(numTemp)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(ListNumbers):
            if numTemp <= ListNumbers[pos]:
                ListNumbers.insert(pos,numTemp)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {ListNumbers}')
    