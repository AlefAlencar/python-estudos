a = 3
b = 5
nome = 'Alef'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'petroebranco':'\033[7;30m'}
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))