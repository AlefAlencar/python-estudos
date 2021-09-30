# CÁLCULO DE FATORIAL
# LEIA: número
# RETORNE: fatorial
from math import factorial

print('FATORIAL')
num = int(input('Digite um número: '))
print('{}! é {}'.format(num, factorial(num)))


'''result = num
num -= 1
print('{}! é:'.format(result))
print(result, 'x', num)

while num != 1:
    result = (result * num)
    num -= 1
    print(result, 'x', num)
print('=', result)'''
