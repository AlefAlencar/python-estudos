# LEIA: nome completo.
# RETORNE: primeiro nome;
# último nome.

nome = str(input('Digite nome completo: '))
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))
