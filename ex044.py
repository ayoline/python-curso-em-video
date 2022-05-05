productNormalPrice = float(input('Digite o preço do produto: '))
conditionToPay = int(input(' 1 - A vista (Dinheiro)\n 2 - A vista (cartão)\n' 
' 3 - 2x no cartão\n 4 - 3x no cartão ou mais\n'))

print(f'Valor: R$ {productNormalPrice}')
if(conditionToPay == 1):
    print(f'Você receberá 10% de desconto: R$ {productNormalPrice - (productNormalPrice*10/100)}')
elif(conditionToPay == 2):
    print(f'Você receberá 5% de desconto: R$ {productNormalPrice - (productNormalPrice*5/100)}')
elif(conditionToPay == 3):
    print(f'Você pagará o preço normal: R$ {productNormalPrice}')
elif(conditionToPay == 4):
    print(f'Você pagará 20% de juros: R$ {productNormalPrice + (productNormalPrice*20/100)}')
else:
    print('Opção invalida!')