# SOMA ÍMPARES MÚLTIPLOS DE TRÊS
# calcule a SOMA de números ÍMPARES MÚLTIPLOS DE 3 de 1 até 500
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print('{} é ÍMPAR e MÚLTIPLO DE 3'.format(c))
        c += 1
        s += i
print('FIM')
print('A soma de todos os {} números ímpares múltiplos de três é: {}'.format(c, s))
