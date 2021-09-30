# LISTA COMPOSTA E ANÁLISE DE DADOS
# LEIA nome e peso de várias pessoas e cadastre numa lista.
# MOSTRE: quantos cadastrados; lista dos +pesados; lista dos +leves.
dados = list()
pessoas = list()
maisPesados = list()
maisLeves = list()
maiorPeso = menorPeso = 0
resp = ' '
while True:
    # entrada DADOS
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso (Kg): ')))
    # maior e menor pesos
    pessoas.append(dados[:])
    if maiorPeso == menorPeso == 0:
        maiorPeso = menorPeso = dados[1]
    elif dados[1] > maiorPeso:
        maiorPeso = dados[1]
    elif dados[1] < menorPeso:
        menorPeso = dados[1]
    dados.clear()
    # entrada CONTINUAR?
    while resp not in 'SN':
        resp = str(input('#Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '
# nomes dos mais pesados e leves
for i in pessoas:
    if i[1] == maiorPeso:
        maisPesados.append(i[0])
    if i[1] == menorPeso:
        maisLeves.append(i[0])
# SAÍDA
#print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.\n'
      f'Mais pesado(s): {maiorPeso}Kg, {maisPesados}\n'
      f'Mais leve(s): {menorPeso}Kg, {maisLeves}')
