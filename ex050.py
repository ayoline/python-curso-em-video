sum = 0

for i in range(0,6):
    num = int(input('Digite um numero inteiro qualquer: '))
    if((num % 2) == 0):
        sum += num

print(f'A soma dos numeros pares é: {sum}') 