# SOMA DE PARES
# LEIA: 6 núm inteiros
# SOME apenas os PARES
s = 0
c = 0
for i in range(0, 6):
    n = int(input('Digite o {}º número inteiro: '.format(i + 1)))
    if n % 2 == 0:
        s += n
        c += 1
print('A soma de {} números pares é {}'.format(c, s))
