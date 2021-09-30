# LEIA vários números e coloque numa lista
# Separe os pares dos  ímpares em duas outras listas
# MOSTRE as três listas
valores = list()
pares = list()
impares = list()
resp = ' '
while True:
    valores.append(int(input('Digite número: ')))
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'VALORES: {valores}\nPARES: {pares}\nIMPARES: {impares}')

print('FIM')
