str = ''

def escreva(str):
    print('~' * (len(str) + 4))
    print(f'  {str}')
    print('~' * (len(str) + 4))

str = input('Digite a string que voce quer mostrar: ')
escreva(str)