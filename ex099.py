from time import sleep


def maior(*arg):
    maior = 0
    print('-=' * 30)
    print('Analisndo os valores passados...')
    for i in range(0, len(arg)):
        print(f'{arg[i]} ', end='')
        sleep(0.3)
        if arg[i] > maior:
            maior = arg[i]
    print(f'Foram informados {len(arg)} valores ao todo.')
    print(f'O maior numero informado foi o {maior}')

maior(1,4,7,10,34,5,9)
maior(40,56,2)
maior()
