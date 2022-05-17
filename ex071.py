fifty = twenty = ten = one = value = 0

while True:
    while True:
        value = int(input(('Digite um valor a ser sacado: R$')))
        if(value < 1):
            print('Digite um valor positivo!!')
        else:
            break
    
    if(value >= 50):
        fifty = value // 50
        print(f'Total de {fifty} notas de R$50')
        value = value % 50
    if(value >= 20):
        twenty = value // 20
        print(f'Total de {twenty} notas de R$20')
        value = value % 20
    if(value >= 10):
        ten = value // 10
        print(f'Total de {ten} notas de R$10')
        value = value % 10
    if(value >= 1):
        one = value // 1
        print(f'Total de {one} notas de R$1')
    break

print('FIM')
    