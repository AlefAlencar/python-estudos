a = input('Digite algo:')
print('O tipo primitivo de {} é'.format(a), type(a))
print(a, 'é númerico?', a.isnumeric())
print(a, 'é alfabético?', a.isalpha())
print(a, 'é alfanumérico?', a.isalnum())
print(a, 'está escrito em ASCII', a.isascii())
print(a, 'está em caixa alta?', a.isupper())
print(a, 'é somente espaços?', a.islower())

