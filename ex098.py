from time import sleep


contagem = []

def contador(inicio, fim, passo):
    ini = inicio; fi = fim; pas = passo
    
    print('-=' * 20)
    print(f'Contagem de {ini} até {fi} de {pas} em {pas}')

    if ini > fi:
        for i in range(ini, fi - 1, -pas):
            print(f'{i}', end=' ')
            sleep(0.3)
        print('FIM!')
    else:
        for i in range(ini, fi +1, pas):
            print(f'{i}', end=' ')
            sleep(0.3)
        print('FIM!')

contador(1,10,1)
contador(10,0,2)

print('Agora personalize a contagem!')
contagem.append(int(input('Digite o início: ')))
contagem.append(int(input('Digite o Fim: ')))
contagem.append(int(input('Digite o passo: ')))

contador(contagem[0],contagem[1],contagem[2])
