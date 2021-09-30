# LEIA 3 números
# RETORNE qual é o maior e qual é o menor
import math

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite só mais um outro: '))

n = [n1, n2, n3]
n.sort()
print('O menor número é o {}, e o maior é o {}'.format(n[0], n[-1]))
