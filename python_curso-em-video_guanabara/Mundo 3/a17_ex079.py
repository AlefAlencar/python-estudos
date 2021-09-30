# LEIA: vários números int e cadastre na lista
# Cadastre apenas valores inexistentes na lista
# MOSTRE os valores únicos em ordem crescente
valores = list()
while True:
    while True:
        valor = int(input('Digite um número: '))
        if valor not in valores:
            valores.append(valor)
            break
        else:
            print(f'Valor {valor} já existe na lista.')
    resp = str(input('Continuar? [S/N]_')).strip().upper()[0]
    if resp == 'N':
        break
print(f'VALORES DIGITADOS EM ORDEM CRESCENTE: {sorted(valores)}')

print('FIM')
