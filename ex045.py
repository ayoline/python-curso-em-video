import random


numPlayer1 = int(input('Vamos jogar Jokenpo!, Digite:\n1 - Papel\n2 - Pedra\n3 - Tesoura\n'))
numPlayer2 = random.randint(1,3)
print(numPlayer2)

if(numPlayer1 == 1 and numPlayer2 == 1):
    print('Empate!')
elif(numPlayer1 == 1 and numPlayer2 == 2):
    print('Você ganhou!')
elif(numPlayer1 == 1 and numPlayer2 == 3):
    print('Você perdeu!')
elif(numPlayer1 == 2 and numPlayer2 == 1):
    print('voce perdeu!')
elif(numPlayer1 == 2 and numPlayer2 == 2):
    print('Empatou!')
elif(numPlayer1 == 2 and numPlayer2 == 3):
    print('Você ganhou!')
elif(numPlayer1 == 3 and numPlayer2 == 1):
    print('voce ganhou!')
elif(numPlayer1 == 3 and numPlayer2 == 2):
    print('voce perdeu!')
elif(numPlayer1 == 3 and numPlayer2 == 3):
    print('Empatou!')

