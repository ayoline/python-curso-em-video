from cgi import print_arguments


preco = float(input('Insira o valor do produto '))
print(f'O preço do produto com 5% de desconto é: {(preco - (preco*5)/100)}')