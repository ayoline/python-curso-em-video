from datetime import date

birthYear = int(input('Digite o ano do nascimento da pessoa: '))
current_date = date.today()
print(f'Possui {current_date.year - birthYear} anos')

if(current_date.year - birthYear <= 9):
    print('MIRIM')
elif(current_date.year - birthYear <= 14):
    print('INFANTIL')
elif(current_date.year - birthYear <= 19):
    print('JUNIOR')
elif(current_date.year - birthYear <= 20):
    print('SENIOR')
else:
    print('MASTER')
