import random
vitorias = 0

while True:
    parOuImpar = input('Escolha par ou impar(p/i): ')

    if(parOuImpar != 'p' and parOuImpar != 'i'):
        print('Opção invalida!')
    else:
        numJogador = int(input('Agora escolha um numero inteiro para jogar: '))
        numComputador = random.randint(0,5)
        print(f'Jogada do computador: {numComputador}')
        resultado = numJogador + numComputador

        if((resultado % 2) == 0):
            resultado = 'p'
        else:
            resultado = 'i'
        
        if(resultado == parOuImpar):
            print('Você ganhou!')
            vitorias += 1
        else:
            print(f'Você Perdeu, depois de {vitorias} vitórias consecutivas')
            break



