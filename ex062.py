num = int(input('Digite o primeiro numero da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = num + (10 * razao)
menu = -1

while(menu != 0):
    while(num != ultimo):
        print(f'{num}',end=' => ')
        num = num + razao
    menu = int(input('\nQuer continuar? quantas casa ainda quer seguir?:(0 para Sair) '))
    ultimo = ultimo + (menu * razao)
print('FIM')
