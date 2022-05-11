stop = False
num = []
resp = ''

while(stop != True):
    numTemp = int(input('Digite um numero qualquer: '))
    num.append(numTemp)
    resp = ''

    while(resp != 'n' and resp != 's'):
        resp = input('Deseja continuar? (s/n): ')
        if(resp == 'n'):
            stop = True
        elif(resp == 's'):
           stop = False
        else:
            print('Parâmetro invalido!')

print(f'A média entre os numeros é: {sum(num)/len(num)}')
print(f'O menor numero é {min(num)}')
print(f'O maior numero é {max(num)}')
