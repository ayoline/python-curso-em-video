weight = int(input('Digite o peso em kg: '))
height = float(input('Digite a altura em metros: '))

imc = weight/(height*height)
print(f'O IMC é: {imc}')

if(imc < 18.5):
    print('Abaixo do peso')
elif(imc <= 25):
    print('Peso ideal')
elif(imc <= 30):
    print('Sobrepeso')
elif(imc <=40):
    print('Obesidade')
else:
    print('Obesidade morbida')