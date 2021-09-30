# ANÁLISE DE DADOS DO GRUPO
# LEIA: idade, sexo de x pessoas
# Pergunte se o usuário quer continuar após cada pessoa
# RETORNE: quantas pessoas +18anos; quantos homens; quantas mulheres <20anos
# Não permita entrada de dados inválidos
sexo = resp = ' '
maiores18 = homens = mulheres20 = 0
while True:
    print('-'*10, 'CADASTRE A PESSOA', '-'*10)
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    sexo = resp = ' '
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'MAIORES 18+: {maiores18} | HOMENS: {homens} | MULHERES <20anos: {mulheres20}')
