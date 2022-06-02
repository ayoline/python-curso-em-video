numberList = [[],[]]

for i in range(0,7):
    temp = int(input('Digite um número inteiro qualquer: '))

    if temp % 2 == 0:
        numberList[0].append(temp)
    else:
        numberList[1].append(temp)

numberList[0].sort()
numberList[1].sort()

print(f'Os valores pares digitados foram: {numberList[0]}')
print(f'Os valores impares digitados foram: {numberList[1]}')