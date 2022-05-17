tupla = ()
lista = []
numeros_pares = []
numero9 = numero3 = 0
ja_entrou = False

for i in range(0,4):
    lista.append(int(input('Digite um numero qualquer: ')))
    tupla = tuple(lista)

for i in range(0, len(tupla)):
    if tupla[i] == 9:
        numero9 += 1
    if tupla[i] == 3:
        if ja_entrou == False:
            numero3 = i
            ja_entrou = True
    if (tupla[i] % 2) == 0:
        numeros_pares.append(tupla[i])

print(f'O numero 9 aparece {numero9} vezes')
print(f'O valor 3 aparece a primeira vez na posição: {numero3}')
print(f'Os valores {numeros_pares} são pares')