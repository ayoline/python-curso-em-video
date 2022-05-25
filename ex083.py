from operator import le


expr = str(input('Digite a expressão: '))
pilha = []

for el in expr:
    if el == '(':
        pilha.append(el)
    elif el == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão NÃO é valida!')
