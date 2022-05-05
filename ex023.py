num = input('Digite um numero de 0 a 9999: ')
if len(num) == 4:
    print(f'Unidade: {num[3]}, Dezena: {num[2]}, Centena: {num[1]}, Milhar: {num[0]}')
if len(num) == 3:
    print(f'Unidade: {num[2]}, Dezena: {num[1]}, Centena: {num[0]}')
if len(num) == 2:
    print(f'Unidade: {num[1]}, Dezena: {num[0]}')
if len(num) == 1:
    print(f'Unidade: {num[0]}')
    

