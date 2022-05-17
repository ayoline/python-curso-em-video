tabela_brasileiro = ('Corinthians','Atlético-MG','São Paulo','Botafogo','Santos','Coritiba','Avaí',
'América-MG','Palmeiras','Bragantino','Internacional','Fluminense','Goiás','Cuiabá','Athletico-PR',
'Flamengo','Juventude','Ceará','Atlético-GO','Fortaleza')

print(f'As primeiras 5 posições do campeonato brasileiro são: {tabela_brasileiro[:5]}\n')
print(f'Os ultimos 4 colocados do campeonato são: {tabela_brasileiro[-4:]}\n')
print(f'A lista em ordem alfabética: {sorted(tabela_brasileiro) }\n')

for i in range(0, len(tabela_brasileiro)):
    if(tabela_brasileiro[i] == 'Botafogo'):
        print(f'O Botafogo está na posição {i + 1} do campeonato\n')
        break