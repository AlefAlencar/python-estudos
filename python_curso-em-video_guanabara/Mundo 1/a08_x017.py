# leia catetos
# retorne hipotenusa
from math import hypot
opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(hypot(opo, adj)))
''' com sqrt
print('O comprimento da hipotenusa é {:.2f}'.format(sqrt(opo**2 + adj**2)))'''