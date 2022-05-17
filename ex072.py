tuple_numbers = ('zero', 'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze','quinze,','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))

    if(num < 0 or num > 20):
        print('Digite um numero entre 1 e 20!!')
    else:
        print(f'Você digitou o numero: {tuple_numbers[num]}')
        break
print('FIM')    
