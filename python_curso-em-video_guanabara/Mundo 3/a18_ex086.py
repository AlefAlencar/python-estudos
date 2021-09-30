# MATRIZ
# CRIE uma matriz 3x3
# PREENCHA a matriz com os valores lidos pelo teclado
# MOSTRE a matriz na formatação correta
matriz = []
linha = []
dimensaoMatriz = int(input('Digite a dimensão da sua matriz: '))
l = c = 1
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
for ll in matriz:
    for cc in ll:
        print(f'{cc:^5}', end=' ')
    print()

print('FIM')
