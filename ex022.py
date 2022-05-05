name = input('Digite o seu nome: ')

print(f'nome em maiusculo: {name.upper()}')
print(f'nome em minusculo: {name.lower()}')
print(f'Quantidade de letras: {len(name.replace(" ", ""))}')
print(f'Quantidade de letras no primeiro nome: {len(name.split()[0])}')
