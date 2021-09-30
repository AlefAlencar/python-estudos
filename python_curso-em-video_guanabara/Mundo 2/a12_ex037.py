# CONVERSOR DE BASES NUMÉRICAS
# LEIA: número inteiro, pergunte a base de conversão:
# 1 = binário, 2 = octal, 3 = hexadecimal
# RETORNE: resultado.

num = int(input('Digite um número inteiro: '))
base = int(input('Escolha uma base de conversão (1=bin, 2=octal, 3=hex): '))

if base == 1:
    print(bin(num)[2::])
elif base == 2:
    print(oct(num)[2::])
elif base == 3:
    print(hex(num)[2::])
else:
    print('Escolha uma das três opções.')
