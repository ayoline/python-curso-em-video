import random

alunos = ['fulano', 'ciclano', 'beltrano', 'mengano']
randomList = random.sample(range(0,4),4)

print(f'A ordem de alunos que iram apresentar o trabalho é:')

for x in randomList:
    print(alunos[randomList[x]])