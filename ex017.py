catOposto = float(input('Digite um valor para Cateto Oposto: '))
catAdjacente = float(input('Digite um valor para cateto Adjacente: '))

hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)

print(f'O comprimento da hipotenusa é: {hipotenusa}')