num = int(input('Digite um numero inteiro qualquer: '))
primo = True

for i in range(2,num):
    if((num % i) == 0):
        primo = False

if(primo):
    print(f'O numero {num} é primo!')
else:
    print(f'O numero {num} não é primo!')
