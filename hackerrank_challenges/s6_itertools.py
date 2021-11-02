"""
DESAFIOS HACKERRANK

06. itertools
"""
# Exemplos
import itertools
'''# PRODUTO CARTESIANO é a multiplicação entre pares ordenados
# envolvendo conjuntos distintos.
print(list(itertools.product([1, 2, 3], repeat=2)))
print(list(itertools.product([1, 2, 3], repeat=3)))
A = [[1, 2, 3], ['a', 'b', 'c']]
print(list(itertools.product(*A)))
B = [[1, 2, 3], ['a', 'b', 'c'], ['¹', '²', '³']]
print(list(itertools.product(*B)))
# PERMUTAÇÃO é uma técnica de contagem utilizada para determinar
# quantas maneiras existem para ordenar os elementos de um conjunto finito.
print(list(itertools.permutations([1, 2, 3])))
print(list(itertools.permutations([1, 2, 3], 2)))
# COMBINAÇÃO são todos os subconjuntos que podemos formar com uma
# quantidade de elementos de um conjunto maior
print('combinações\n',
      list(itertools.combinations('123', 2)))
A = [1, 1, 3, 3, 3]
print(list(itertools.combinations(A, 4)))
# Combinacoes incluindo o próprio elemento
print('combincations_with_replacement:\n',
      list(itertools.combinations_with_replacement([1, 2, 3], 2)))
print(list(itertools.combinations_with_replacement('aaeee', 2)))
# GROUPBY fabrica um iterador que retorna consecutivas chaves e grupos de um iterável.
chaves = []
grupos = []
data = 'abbcccbba'
for chances, g in itertools.groupby(data):
    chaves.append(chances)
    gg = list(g)
    grupos.append(gg)
    print(chances, gg)
print(chaves, '\n', grupos)
# '''

# 1/7 product() (easy)
'''A, B = (list(map(int, input().split())) for _ in range(2))  # INPUT A, B
AB = list(itertools.product(A, B))  # produto AxB
# OUTPUT
for t in AB:
    print(t, end=' ')  # '''

# 2/7 permutation() (easy)
'''s, chances = input().split()  # INPUT em 1 linha, string S e integer K
p = sorted(list(itertools.permutations(s, int(chances))))  # permutacao
print(s, chances)
print(''.join(''.join(t) for t in p))
for t in p:
    print(''.join(t))  # '''

# 3/7 combinations() (easy)
# Fazer todas as combinações ATÉ o tamanho K, ou seja, de 1 a K
'''s, chances = input().upper().split()  # INPUT em 1 linha, string S e integer K
for x in range(1, int(chances)+1):  # aumentar o tamanho da combinacao
    c = sorted(list(itertools.combinations(sorted(s), x)))  # combina conforme X
    for t in c:  # OUTPUT
        print(''.join(t))  # cada combinacao (tupla) concatenada '''

# 4/7 combinations_with_replacement() (easy)
'''s, chances = input().upper().split()  # INPUT
cr = sorted(list(itertools.combinations_with_replacement(sorted(s), int(chances))))
for t in cr:  # OUTPUT
    print(''.join(t))  # '''

# 5/7 Compress the String! (medium)
'''s = input()  # INPUT string S
chaves, grupos = [], []
for chances, g in itertools.groupby(s):
    chaves.append(int(chances))
    grupos.append(len(list(g)))
zipado = list(zip(grupos, chaves))
#print(chaves, grupos, '\n', zipado)
for tupla in zipado:  # OUTPUT formatado conforme a amostra
    print(tupla, end=' ')  # '''

# 6/7 Iterables and Iterators (medium)
'''# INPUT em 3 linhas: n, N, chances
# n quantidade de elementos da lista N
# N lista de letras
# chances quantidade de índices para selecionar (vezes)
# OUTPUT: a probabilidade de selecionar a letra 'a'
n_letras = int(input())
letras = input().split()
n_escolhas = int(input())
# resultados = []
# contem_a = 0
# for resultado in itertools.combinations(letras, n_escolhas):
#    if 'a' in resultado:
#        contem_a += 1
#    resultados.append(resultado)
# print(f'{letras.count("a")}, {contem_a}/{len(resultados)}, {contem_a / len(resultados)}')
# >simplificado
resultados = list(itertools.combinations(letras, n_escolhas))
cont = len(list(1 for result in resultados if 'a' in result))
print(resultados, len(resultados))
print(f'{(cont / len(resultados)):.3f}')  # '''


# 7/7 Maximize It! (hard)
'''# precisava fazer o produto cartesiano antes
# INPUT
k, m = (map(int, input().split()))
lt = [list(map(int, input().split())) for _ in range(k)]
# PROCESS
# 1. gerar produto cartesiano
# 2. para cada combinacao, calcular o modulo da soma dos quadrados dos elementos
# OUTPUT
print(
    max(
        [(sum(_**2 for _ in _) % m) for _ in list(itertools.product(*lt))]
    )
)
# lt_comb = list(itertools.product(*lt))
# res = [sum([_**2 for _ in _]) % m for _ in lt_comb]
# maior = max(res)
# 
# print(k, m, lt)
# print(lt_comb)
# print(res)
# print(maior)  # '''
