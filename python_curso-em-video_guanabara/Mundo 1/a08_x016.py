# leia número real
# retorne parte inteira
from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(num, trunc(num)))

''' sem precisar importar módulos: 
print('A parte inteira  de {} é {}'.format(num, int(num)) '''