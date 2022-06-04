from random import randint
import time


numGames = 0
listGames = []
game = []

print('=' * 48)
print(f'{"JOGA NA MEGA-SENA":^48}')
print('=' * 48)
print()
numGames = int(input('Digite o numero de jogos que você quer fazer: '))

print()
for i in range(0,numGames):
    for j in range(0,6):
        num = randint(1,60)

        while num in game:
            num = randint(1,60)
        
        game.append(num)

        if j == 5:
            listGames.append(game)
            print(game)
            game.clear()
            time.sleep(1)

print()