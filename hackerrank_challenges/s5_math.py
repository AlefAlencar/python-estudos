"""
DESAFIOS HACKERRANK

05. Math ("Matemática")

Identificação do desafio:
##### tipo, dificuldade: nome_desafio
    Descrição da solução em comentários.
    Remova as aspas triplas para poder executar o código do desafio específico. Recoloque-as para não executar.
"""

# 1/7 Polar coordinates (easy)
'''# Converter um número complexo Z para coordenadas polares.
# INPUT: 1. número complexo Z
# OUTPUT: 2.1 valor de R
# 2.2 valor de O
from cmath import polar
r, o = polar(complex(input()))  # INPUT: lê o número complexo,
# converte para coordenadas polares, e atribui os valores
# OUTPUT
print(f'{r:.3f}')
print(f'{o:.3f}')  # '''

# 2/7 Mod Divmod (easy)
'''a, b = (int(input()) for _ in range(2))  # INPUT dois valores
r = (a // b, a % b)  # calcula o divisao inteira, modulo
# OUTPUT
print(r[0])
print(r[1])
print(r)  # '''

# 3/7 Power - Mod Power (easy)
'''# 1. lê A, B, M
# OUTPUT:
# 2.1. pow(a,b)
# 2.2. pow(a,b,m)
a, b, m = (int(input()) for _ in range(3))  # 1
print(pow(a, b))  # 2.1
print(pow(a, b, m))  # 2.2  # '''

# 4/7 Integers Come In All Sizes (easy)
'''# INPUT: 1. 4 valores A, B, C, D
# OUTPUT: a^b + c^d
a, b, c, d = (int(input()) for _ in range(4))
print(pow(a, b) + pow(c, d))  # '''

# 5/7 Find Angle MBC (medium) ************** NÃO-RESOLVIDO
'''# Descobrir o ângulo T (theta) do triângulo MBC
# M é o ponto médio da hipotenusa de um triângulo-retângulo ABC
# INPUT:
# 1. comprimento do lado AB (integer)
# 2. comprimento do lado BC (integer)
# OUTPUT: ângulo MBC em graus. Arredondar para cima a partir da metade (xx.5º)
import math
# sen=opo/hip, cos=adj/hip, tan=opo/adj. Todos em relação ao ângulo desejado
ab, bc = (int(input()) for _ in range(2))  # A B
ac = math.hypot(ab, bc)  # H

# angulo â = a^2 + b^2 -2abCosC

print('tan', math.degrees(math.atan2(ab, bc)))  # '''

# 6/7 Triangle Quest (medium)
# OUTPUT: n=3
# 1
# 22
# 333
for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print() #


# 7/7 Triangle Quest II (medium)

