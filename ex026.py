from posixpath import split
from typing import List

frase = input('Digite uma frase qualquer: ')
fraseSplited = list(frase)
numbersOfAppears = 0
letterExists = False
lastAppears = None

for index, x in enumerate(fraseSplited,start=0):
    if x.upper() == 'A':
        numbersOfAppears += 1
        if letterExists == False:
            print(f'A letra "A" aparece a primeira vez na posição {index} da frase')
            letterExists = True
        lastAppears = index

if lastAppears == None:
    print('A letra "A" não aparece nenhuma vez na frase')
else: 
    print(f'A letra "A" aparece na frase a ultima vez na posição {lastAppears}')

if numbersOfAppears > 0:
    print(f'A letra "A" aparece na frase {numbersOfAppears} vezes')

