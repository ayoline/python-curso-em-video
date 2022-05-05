from datetime import date

birthYear = int(input('Digite o ano do nascimento da pessoa: '))
current_date = date.today()

if(current_date.year - birthYear < 18):
    print(f'Tranquilo, ainda faltam {18 - (current_date.year - birthYear)} anos para você se alistar')
elif(current_date.year - birthYear > 18):
    print(f'Atenção! Você deveria ter se alistado fazem {abs(18 - (current_date.year - birthYear))} anos')
else:
    print('Está na hora de você se alistar!')
