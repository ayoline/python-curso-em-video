dictPlayer = {}
gols = []

dictPlayer['nome'] = input('Qual o nome do jogador? ')
numGames = int(input('Quantos partidas ' + dictPlayer['nome'] + ' jogou? '))

for i in range(0, numGames):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))

dictPlayer['gols'] = gols
dictPlayer['total'] = sum(gols)

print()
for x, y in dictPlayer.items():
    print(f'{x}: {y}')
print()
