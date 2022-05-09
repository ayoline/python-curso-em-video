num = int(input('Digite um numero para saber o seu fatorial: '))
i = num -1
sum = num

while (i != 0):
    sum = sum * i
    i -= 1

print(f'O fatorial de {num} é {sum}')