# LEIA: nome da pessoa.
# RETORNE: tem 'Silva' ou não.

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
