"""
HACKERRANK preparação para entrevista

02. ARRAYS
"""

# 1/5 2D Array - DS
'''# a b c
#   d
# e f g
arr = []  # INPUT
for _ in range(6):
    linha = list(map(int, input().split()))
    arr.append(linha)
# OUTPUT
hg = []
for l in range(1, 5):
    for c in range(1, 5):
        soma = sum([  # soma a partir do centro de referência, conforme a ampulheta
            arr[l-1][c-1], arr[l-1][c], arr[l-1][c+1],
            arr[l][c],
            arr[l+1][c-1], arr[l+1][c], arr[l+1][c+1]
        ])
        hg.append(soma)
        print(soma)
print(max(hg))  # '''

# 3/5 Arrays: Left Rotation
'''t, r = list(map(int, input().split()))  # tamanho do array, rotacoes a esquerda
arr = input().split()

i = r % len(arr)
# fatia os primeiros termos e acrescenta-os no final
nova = arr[i:] + arr[:i]
print(nova)  # '''


# 4/5 New Year Chaos (medium) : {1ª: 10/12f, 2ª: 4/12f, 3ª: }
'''def min_bribes(q):  # diferenca entre numero com o indice da posicao atual
    # b = 0  # bribes, suborno  # 10/12failed
    # for i, x in enumerate(q):
    #     dif = x - (i+1)  # i + 1 - x
    #     if dif > 0:
    #         b += dif
    #         if dif >= 3:
    #             print('Too chaotic')
    #     print(i+1, x, '=', dif)
    # print(abs(b))
    # print('-'*10)

    # b = 0  # COMPARACAO BRUTA
    # for i, x in enumerate(q):
    #     bp = 0
    #     for ii, xx in enumerate(q[i:]):
    #         if x > xx:
    #             bp += 1
    #         if bp > 2:
    #             return print('Too Chaotic')
    #     b += bp
    #     # print('Bribes/person', bp)
    # print('>>>Total bribes', b)
    # 1. ver se P está a mais de duas posições
    # 2. ver quantas vezes P foi subornado
    bribes = 0
    q = [_-1 for _ in q]
    for i, p in enumerate(q):
        if p - i > 2:  # se >2, fim
            return print('Too Chaotic')
        for j in range(max(p-1, 0), i):  # percorre da posi_inicial p até a posi_atual i
            if q[j] > p:  # ve se eh maior que o p
                bribes += 1
    print(bribes)

for _ in range(int(input())):
    n, q = input(), list(map(int, input().split()))
    min_bribes(q)  # '''


# 5/5 Minimun Swaps 2 (medium)  {1ªsubmissao: 6/15, 6pontos; 2ª: 10/15, 20p, 3ª: 15/15}
'''def minimum_swaps(arr):
    # swaps = 0
    # # arr = [_-1 for _ in arr]
    # for i, n in enumerate(arr):  # posicao atual
    #     if i == n-1:  # ve se estah na posicao certa
    #         continue
    #     im = i  # indice do menor valor
    #     for j in range(i, len(arr)):  # procura o menor valor que vem depois do elemento atual
    #         # compara o entao menor com o seguinte. se este for menor, salva seu indice
    #         if arr[j] < arr[im]:
    #             im = j
    #     arr[i], arr[im] = arr[im], arr[i]  # SWAP
    #     swaps += 1
    # return swaps

    # swaps, size = 0, len(arr)
    # for i in range(size):
    #     if arr[i] == i+1:
    #         continue
    #     arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
    #     swaps += 1
    #     i -= 1
    # print(arr)
    # return swaps

    count = 0
    i = 0
    while i < len(arr):
        print(f'{arr[i]} != {i+1}?', end=' ')
        if arr[i] != i+1:
            while arr[i] != i+1:
                temp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = temp
                count += 1
        i += 1
    return count


for _ in range(int(input())):
    size, arra = input(), list(map(int, input().split()))
    print('\n', minimum_swaps(arra), 'swaps')  # '''


# 5/5 Array Manipulation (hard)
