# COMPARANDO NÚMEROS
# LEIA: dois números inteiros.
# Compare-os.
# RETORNE: O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.
print('COMPARANDO NÚMEROS')
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 == n2:
    print('O primeiro valor ({}) é IGUAL ao segundo ({})'.format(n1, n2))
elif n1 > n2:
    print('O PRIMEIRO valor ({}) é MAIOR que o segundo ({}).'.format(n1, n2))
else:
    print('O SEGUNDO valor ({}) é maior que o primeiro ({})'.format(n2, n1))
