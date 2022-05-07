nome = []
idade = []
sexo = []
mulheresComMenosDe20 = 0
homemMaisVelho = 0


for i in range(0,6):
    nome.append(input('Digite o nome da pessoa: '))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(input('Qual o sexo("m" ou "f"): '))

print(f'A média de idade das pessoas é: {sum(idade)/len(idade)}')

for i in range(0,6):
    if(idade[i] < 20 and sexo[i] == 'f'):
        mulheresComMenosDe20 += 1
    if(sexo[i] == 'm' and idade[i] > homemMaisVelho):
        homemMaisVelho = idade[i]

index = idade.index(homemMaisVelho)
print(f'O homem mais velho é: {nome[index]}')

print(f'Existem {mulheresComMenosDe20} mulheres com menos de 20 anos')