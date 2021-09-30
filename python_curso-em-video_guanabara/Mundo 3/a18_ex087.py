# APRIMORE o exercício 086
# MOSTRE a soma de todos os pares; soma da terceira coluna; maior valor da 2a linha
matriz = []
linha = []
dimensaoMatriz = int(input('Digite a dimensão da sua matriz: '))
l = c = 1
somaPares = soma3coluna = maior2linha = 0
print('Digite o valor da posição: ')
while l <= dimensaoMatriz:  # linha
    while c <= dimensaoMatriz:  # coluna
        linha.append(int(input(f'[{l}x{c}]: ')))  # item
        c += 1
    matriz.append(linha[:])
    linha.clear()
    l += 1
    c = 1
# mostrar
print(f'MATRIZ: ')
# percorrer item a item
for ll, lin in enumerate(matriz):  # percorrer linhas
    for cc, col in enumerate(lin):  # percorrer coluna a coluna (item a item, na prática)
        print(f'{col:<3}', end=' ')
        if col % 2 == 0:
            somaPares += col
        if cc == 2:
            soma3coluna += col
        if ll == 1 and col > maior2linha:
            maior2linha = col
    print()
print(f'Soma dos pares: {somaPares}\nSoma da terceira coluna: {soma3coluna}\nMaior valor da 2ª linha: {maior2linha}')
print('FIM')
