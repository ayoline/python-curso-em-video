from datetime import datetime

birthday = []

for i in range(0,3):
    my_string = str(input('Informe a data de nascimento(dd-mm-yyyy): '))
    birthday.append(datetime.strptime(my_string, "%d-%m-%Y"))

for i in range(0,len(birthday)):
    if((2022 - birthday[i].year) > 18):
        print(f'{birthday[i]} é maior de idade')
    else:
        print(f'{birthday[i]} é menor de idade')
