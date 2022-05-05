number1 = int(input('Digite o primeiro numero: '))
number2 = int(input('Digite o segundo numero: '))
number3 = int(input('Digite o terceiro numero: '))

def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    print("O maior dos 3 numeros é: ", largest_num)

def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    print("O menor dos 3 numeros é : ", smallest_num)
largest(number1, number2, number3)
smallest(number1, number2, number3)