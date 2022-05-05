import random

num = int(input('Tente adivinhar qual numero o computador ira sortear(entre 0 e 5):'))
randomNumber = random.randint(0,5)

if(randomNumber == num):
    print('Parabéns você ganhou!')
else:
    print(f'Voce errou, o numero sorteado foi: {randomNumber}')
