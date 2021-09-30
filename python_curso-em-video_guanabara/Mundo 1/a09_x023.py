# LEIA: de 0 a 9999.
# RETORNE: cada dígito separado.

num = int(input('Digite um número de 0 a 9999: ')[0:4])
print(num)
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))