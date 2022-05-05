fullName = input('Digite o um nome completo qualquer: ')
fullName = fullName.split()

print(f'O primeiro nome da pessoa é: {fullName[0]}')
print(f'O ultimo nome da pessoa é: {fullName[len(fullName) -1]}')