year = int(input('Digite um ano acima de 1582: '))

if(year%4 == 0 and year%100 == 0 and year%400 == 0):
    print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')