# PROGRESSÃO ARITMÉTICA v2.0
# REFAÇA o DESAFIO 051 PROGRESSÃO ARITMÉTICA
# LEIA: primeiro termo e a razão
# RETORNE: 10 primeiros termo da PA, usando estrutura while
pt = int(input('PROGRESSÃO ARITMÉTICA\nDigite o primeiro termo: ')) # primeiro termo
rz = int(input('Digite a razão: ')) #razão
en = pt  # enésimo termo

print('1º termo: {}'.format(en))
c = 1
while c != 10:
    en += rz
    c += 1
    print('{}º termo: {}'.format(c, en))
print('FIM')
