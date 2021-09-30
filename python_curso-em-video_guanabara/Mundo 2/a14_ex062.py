# SUPER PROGRESSÃO ARITMÉTICA v3.0
# MELHORE o DESAFIO 061
# LEIA: primeiro termo e a razão
# RETORNE: 10 primeiros termo da PA, usando estrutura while
# PERGUNTE quantos termos mais o usuário quer ver
# ENCERRAR quando for '0'
pt = int(input('PROGRESSÃO ARITMÉTICA\nDigite o primeiro termo: ')) # primeiro termo
rz = int(input('Digite a razão: ')) #razão
en = pt  # enésimo termo
x = 1

print('1º termo: {}'.format(en))
c = 1
while c != 10:
    en += rz
    c += 1
    print('{}º termo: {}'.format(c, en))
while x != 0:
    x = int(input('Mais quantos termos deseja ver? '))
    i = c + x
    while c != i:
        en += rz
        c += 1
        print('{}º termo: {}'.format(c, en))
print('{} termos mostrado. FIM'.format(c))
