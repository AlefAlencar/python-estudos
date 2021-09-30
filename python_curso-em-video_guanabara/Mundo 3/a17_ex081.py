# LEIA vários números, guarde na lista
# MOSTRE quantos digitados, a lista em decrescente, e se o 5 está ou não na lista
valores = list()
resp = ' '
q = 0
while True:
    valores.append(int(input('Digite valor: ')))
    q += 1

    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '

print(f'Invertido: {sorted(valores, reverse=True)}. Digitados {len(valores)} elementos')

if 5 in valores:
    print('O 5 está na lista.')
else:
    print('Não, o 5 não está na lista.')

print('FIM')
