stop = 0
num = []

while(stop != 999):
    numTemp = int(input('Digite um numero qualquer(999 para sair): '))
    if(numTemp == 999):
        stop = numTemp
    else:
        num.append(numTemp)    

print(f'A quantidade de números digitados foi: {len(num)}')
print(f'A soma entre ele é: {sum(num)}')