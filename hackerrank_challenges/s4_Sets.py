"""
DESAFIOS HACKERRANK

04. Sets ("Conjuntos")
"""
# 1/12 Introduction To Sets (Sets, easy)
'''# * Corrigido após revisão. A forma anterior não garantia 3 casas decimais.
# Contudo, o código anterior mesmo assim passou em todos os testes do site após a submissão.
import math

def average(array): 
    # your code goes here
    a = set(array)
    s = math.fsum(a)
    return float(f'{s / len(a):.3f}') # Média de valores distintos (máximo 3 casas decimais).

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)  # '''

# 2/12 No Idea! (Sets, medium)
'''# "The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array. Might contain duplicate elements.
# The third and fourth lines contain m integers, A and B, respectively. No repeated elements."
_ = input()  # n m
arr = input().split()  # n integers array
(a, b) = (set(input().split()) for r in range(2))  # A, B

print(sum((x in a) - (x in b) for x in arr))  # Output, total felicidade
# for x in arr -> sum( (x in a) - (x in b) )  Se x estiver em A ou em B, então 1 (True)  # '''

# 3/12 Symmetric Difference (Sets, easy)
'''def diff(x, y):
    x = set(x)
    y = set(y)
    z = x.difference(y)  # está em x mas não em y
    z.update(y.difference(x))  # adiciona(está em y mas não em x)
    z = sorted(z)  # ordena
    for i in z:    # imprime
        print(i)


a, b = int(input()), list(map(int, input().split()))
c, d = int(input()), list(map(int, input().split()))
diff(b, d)  # '''

# 4/12 add() (Sets, easy)
'''n = int(input())  # Número de carimbos
cs = (input() for _ in range(n))  # lê nome dos países n vezes.
print(len(set(cs)))  # imprime o tamanho do conjunto do objeto gerador cs. '''

# 5/12 Set.discard(), .remove(), .pop() (Sets, easy)
'''# Lê n=len(s), s, m=commands, m commands
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))  # '''

# 6/12 Set.union() operation A|B (Sets, easy)
''' _, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))
print(len(a.union(b)))  # '''

# 7/12 Set.intersection() operation A&B (Sets, easy)
'''_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

print(len(a.intersection(b)))  # '''

# 8/12 Set.difference() operation A-B (Sets, easy)
'''_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

print(len(a - b))  # '''

# 9/12 Set.symmetric_difference() operation A^B (Sets, easy)
'''_, a = input(), set(map(int, input().split()))
_, b = input(), set(map(int, input().split()))

print(a ^ b)  # diferenca simetrica, A.symmetric_difference(B) '''

# 10/12 Set Mutations (Sets, easy)
'''# .update()  |=
# .intersection_update()  &=
# .difference_update()  -=
# .symmetric_difference_update()  ^=
# ## Input ##
# 1. número de elementos do conjunto a
# 2. conjunto a
# 3. número de operações/conjuntos m
# 4.1. operação e tamanho do conjunto m
# 4.2. conjunto m
_, a = input(), set(map(int, input().split()))  # 1, 2
for _ in range(int(input())):  # 3
    operacao = input().split()[0]
    b = set(map(int, input().split()))  # 4.1
    eval(f'a.{operacao}(b)')  # 4.2
    print(sum(a))  # '''

# 11/12 Check Subset (Sets, easy)
'''# Verificar se A é subconjunto de B, imprima True ou False.
# Inputs
# 1. T número de casos de testes
# 1.1 len(A)
# 1.2 Conjunto A
# 1.3 len(B)
# 1.4 Conjunto B
# Output: # 2. True ou False
for _ in range(int(input())):  # 1
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))

    print(a.issubset(b))  # '''

# 12/12 Check Strict Superset (Sets, easy)
'''# Verificar se o conjunto A é superconjunto de n conjunto
# INPUT
# 1. Conjunto A
# 2. N, número de outros conjuntos
# 2.1 Outro conjunto n
# OUTPUT 3. Imprima True se A é superconjunto de todos os outros conjuntos. Senão, False.
a = set(map(int, input().split()))  # 1
output = True
for _ in range(int(input())):  # 2
    b = set(map(int, input().split()))  # 2.1
    output = output and a.issuperset(b)  # 3

print(output)  # '''
