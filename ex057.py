sexo = ''

while sexo != 'f' and sexo !='m':
    sexo = str(input('Digite o sexo de uma pessoa(ex: M/F) ')).lower()
    if(sexo != 'f' and sexo !='m'):
        print('Valor invalido, tente novamente!')