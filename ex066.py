num = []

while True:
    numTemp = int(input('Digite um numero qualquer(999 para sair): '))
    if(numTemp == 999):
        break
    num.append(numTemp)    

print(f'A soma dos {len(num)} valores é: {sum(num)}')