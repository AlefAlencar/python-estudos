# VALIDAÇÃO DE DADOS
# LEIA: sexo de uma pessoa
# Só aceite 'M' ou 'F'
# Se errado, peça digite novamente
print('VALIDAÇÃO DE DADOS')
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida. Digite seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {}.'.format(sexo))
'''i = 0
sx = ''
while i == 0:
    sx = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if sx == 'M' or sx == 'F':
        i = 1
    else:
        print('Opção inválida. Digite novamente.')
if sx == 'M':
    sexo = 'Masculino'
elif sx == 'F':
    sexo = 'Femenino'
print('Seu sexo é {}. FIM'.format(sexo))'''