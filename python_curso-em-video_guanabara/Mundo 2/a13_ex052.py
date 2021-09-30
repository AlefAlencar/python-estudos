# NÚMEROS PRIMOS
# LEIA: número inteiro
# RETORNE: é número primo ou não

n = int(input('Digite um número inteiro e descubra se é primo: '))
cont_div = 0    # contador de divisores

if n <= 1:
    print('')
for c in range(2, n):
    if n % c == 0:
        print(c)
        cont_div += 1
if cont_div == 0:
    print('PRIMO')
else:
    print('NÃO é primo')
