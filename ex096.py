largura = comprimento = 0

def area(largura, comprimento):
    print(f'A área de um terreno {largura} x {comprimento} é {largura*comprimento}m²')

largura = float(input('Digite a Largura do terreno(m): '))
comprimento = float(input('Digite o comprimento do terreno(m) '))

area(largura,comprimento)