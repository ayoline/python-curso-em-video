dictPlayer = {}
yes_or_not = ''
gols = []
players = []

while True:
    dictPlayer.clear()
    gols.clear()

    dictPlayer['nome'] = input('Qual o nome do jogador? ')
    numGames = int(input('Quantos partidas ' + dictPlayer['nome'] + ' jogou? '))

    for i in range(0, numGames):
        gols.append(int(input(f'Quantos gols na partida {i+1}: ')))

    dictPlayer['gols'] = gols[:]
    dictPlayer['total'] = sum(gols)

    players.append(dictPlayer.copy())

    while True:
        yes_or_not = input('\nVocê deseja continuar?(S/N)').upper()[0]
        if yes_or_not in 'SN':
            break
        else:
            print('Digite um valor valido!')
    if yes_or_not == 'N':
        break

print()
print('-=' * 48)
print(f'cod ', end='')
for i in dictPlayer.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 48)
for x, y in enumerate(players):
    print(f'{x:>3} ', end='')
    for i in y.values():
        print(f'{str(i):<15}', end='')
    print()
print('-=' * 48)

while True:
    searching = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if searching == 999:
        break
    if searching >= len(players):
        print(f'Não existe jogador com o código de busca {searching}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {players[searching]["nome"]}:')
        for i, g in enumerate(players[searching]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 48)