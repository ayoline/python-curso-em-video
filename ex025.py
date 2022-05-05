name = input('Digite um nome qualquer: ')
nameSplited = name.split()
isPositive = False

for x in nameSplited:
    if x.upper() == 'SILVA':
        isPositive = True
        break

if isPositive:
    print('O nome digitado possui "SILVA" no nome')
else:    
    print('O nome digitado não possui "SILVA" no nome')