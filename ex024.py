cidade = input('Digite o nome de uma cidade qualquer: ')


if cidade.upper().split()[0] == 'SANTO':
    print(f'A cidade {cidade}, começa com o nome "SANTO"')
else:
    print(f'A cidade {cidade}. não começa com o nome "SANTO"')
