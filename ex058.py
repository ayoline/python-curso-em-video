import random

num = -1
randomNumber = 0
tryes = 0

while num < 0 or num > 10 or num != randomNumber:
    num = int(input('Tente adivinhar o numero sorteado de 0 a 10 '))
    randomNumber = random.randint(0,10)
    if(num == randomNumber):
        tryes += 1
        print(f'Parabens, vc acertou em {tryes} tentativas')
    elif(num < 0 or num > 10):
        print('Voce digitou um numero invalido, tenta novamente')
    else:
        tryes += 1
        print('Voce errou, tente novamente')

