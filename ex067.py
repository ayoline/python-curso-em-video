while True:
    num = float(input('\nDigite um numero para saber a tabuada dele(-1 para sair): '))

    if(num < 0):
        print('===============')
        print('FIM')
        break
    
    print('===============')
    for i in range(1,11):
        print(f'{(i)} x {num} : {(num*i)}')
    print('===============')