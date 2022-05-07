peso = []

for i in range(0,5):
    peso.append(int(input('Digite o peso da pessoa: ')))

max = max(peso)
min = min(peso)

print(f'O peso {max} é o maior peso da lista')
print(f'O peso {min} é o menor peso da lista')