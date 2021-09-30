# ESTATÍSTICAS EM PRODUTOS
# LEIA: nome, preço de x produtos
# Pergunte se usuário quer continuar
# RETORNE: Total gasto; Quantos produtos >$1000; Nome produto <$
totalGasto = prodMaisDe1000 = precoMenor = 0
resp = nomeProdMaisBarato = ''

while True:
    nome = str(input('PRODUTO: '))
    preco = float(input('PREÇO: R$'))
    if preco > 1000:
        prodMaisDe1000 += 1
    if precoMenor == 0 or precoMenor > preco:
        precoMenor = preco
        nomeProdMaisBarato = nome
    totalGasto += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('CONTINUAR [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'TOTAL GASTO: R${totalGasto}\nQUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE R$1000: {prodMaisDe1000}\nPRODUTO MAIS BARATO: {nomeProdMaisBarato}')
