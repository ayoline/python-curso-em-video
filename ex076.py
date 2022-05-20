from sqlalchemy import table


tableItens = ('Pão',1,'Caneta',3,'Agua',2,'Caderno',10)

print('=' * 48)
print(f'{"LISTAGEM DE PREÇOS":^48}')
print('=' * 48)

for i in range(0,len(tableItens)):
    if i % 2 == 0:
        print(f'{tableItens[i]:.<39}', end='')
    else:
        print(f'R${tableItens[i]:>7.2f}')

print('=' * 48)