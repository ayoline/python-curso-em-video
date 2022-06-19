from random import randint


lista_num = []


def sorteia():
    print('Sorteio de 5 valores: ', end='')
    for i in range(0,5):
        lista_num.append(randint(0,10))
        print(f'{lista_num[i]} ', end='')
    print('FIM!')

def somaPar(lista):
    sorteia()
    soma_par = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            soma_par += lista[i]
    print(f'Somando os valores pares de {lista}, temos {soma_par}')
    print()

somaPar(lista_num)
