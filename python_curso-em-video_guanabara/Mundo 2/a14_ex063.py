# SEQUÊNCIA DE FIBONACCI V1.0
# LEIA: n número inteiro
# RETORNE: n primeiros elementos da sequência de Fibonacci
# F: {0, 1, n = n-1 + n-2}
n1 = 0
n2 = 1
n3 = 1
x = int(input('Quantos números da sequência de FIBONACCI v1.0 deseja ver? '))
print('{}->{}'.format(n1, n2), end='')
c = 2
while c != x:
    n3 = n1 + n2
    c += 1
    print('->{}'.format(n3), end='')
    n1 = n2
    n2 = n3

print('\nFIM')
