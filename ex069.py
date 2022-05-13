nome = []
idade = []
sexo = []
pessoasMaiores = 0
qtdHomens = 0
mulheresComMenosDe20 = 0

while True:
    nome.append(input('Digite o nome da pessoa: '))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(input('Qual o sexo("m" ou "f"): '))

    if(idade[-1] > 17):
        pessoasMaiores += 1

    if(sexo[-1] == 'm'):
        qtdHomens += 1
    
    if(sexo[-1] == 'f' and idade[-1] < 20):
        mulheresComMenosDe20 += 1

    sair = input('Deseja continuar?(s/n): ')

    if(sair == 'n'):
        break



print(f'Foram cadastrados {pessoasMaiores} pessoas maiores de 18 anos')
print(f'Foram cadastrados {qtdHomens} homens')
print(f'Foram cadastradas {mulheresComMenosDe20} mulheres com menos de 20 anos')