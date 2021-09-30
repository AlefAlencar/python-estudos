# UNINDO DICIONÁRIOS E LISTAS
# LEIA nome, sexo e idade de várias pessoas
# Cada pessoa é um dicionário, e todos os dicionários estão numa lista
# MOSTRE quantos_cadastrados, média_idade, uma lista das mulheres, uma lista de pessoas idade > média_idade
cadastro = list()
pessoa = dict()
resp = ' '
mediaIdade = 0
# ===ENTRADA DE DADOS===
while True:
    pessoa['Nome'] = str(input('NOME: ')).strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
    '''while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    pessoa['Sexo'] = sexo
    sexo = ' ' '''
    pessoa['Idade'] = int(input('IDADE: '))
    cadastro.append(pessoa.copy())  # CADASTRAMENTO
    while resp not in 'SN':  # "CONTINUAR?"
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '
# ===SAÍDA DE DADOS===
print(f'A) Há {len(cadastro)} pessoas cadastradas.')  # QUANT. CADASTRADOS
for p in cadastro:  # MÉDIA DE IDADE
    mediaIdade += p['Idade']
mediaIdade = mediaIdade / len(cadastro)
print(f'B) Média de idade: {mediaIdade:.1f} anos.')
print('C) Mulheres cadastradas:')  # LISTA DE MULHERES
for p in cadastro:
    if p['Sexo'] == 'F':
        print(f' - {p["Nome"]}')
print(f'D) Pessoas com idade acima da média de {mediaIdade:.1f} anos do grupo:')  # PESSOAS COM IDADE ACIMA DA MÉDIA
for p in cadastro:
    if p['Idade'] > mediaIdade:
        print(f'{p["Nome"]}, com {p["Idade"]} anos.')
print('<<<ENCERRADO>>>')
