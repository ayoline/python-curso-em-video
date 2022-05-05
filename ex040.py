num1 = float(input('Digite a primeira nota:'))
num2 = float(input('Digite a segunda nota:'))
average = (num1+num2)/2
print(f'Média de: {average}')

if(average < 5):
    print('Reprovado!')
elif(average >= 5 and average <= 6.9):
    print('Recuperação!')
else:
    print('Aprovado!')