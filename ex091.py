from random import randint
from time import sleep


results = {}

for i in range(0,4):
    results[i+1] = randint(1,6)
    print(f'O jogador{i+1} tirou {results[i+1]}')
    sleep(1)

ranking = list()
ranking = sorted(results.items(), key=lambda item: item[1], reverse=True)

print()
print('-=' * 30)
print('-==Ranking dos Jogadores==-')

for i, v in enumerate(ranking):
    print(f'{i+1}Lugar: jogador{v[0]} tirou {v[1]}')
    sleep(1)

