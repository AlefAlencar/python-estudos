# FUNCAO leia_int()
# como a função input(), mas faz validação para aceitar apenas um valor numérico
# n = leia_int('Digite um n')
def leia_int(n):
    while not n.isnumeric():
        n = input(f'ERRO! {n} não é um número inteiro.\nDigite um número: ')
    else:
        return print(f'CERTO. {n} é um número inteiro.')


leia_int(input('Digite um número: '))
