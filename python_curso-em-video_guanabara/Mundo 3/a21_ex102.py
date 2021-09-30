# FUNCAO fatorial(numero, show)
# show = valor lógico opcional para mostrar ou não o cálculo inteiro. Padrão: False, só mostra resultado.
def fat(num, show=False):
    """
    A função fat() calcula o fatorial de um número.
    :param num: número a calcular.
    :param show: (opcional) mostrar ou não mostrar o cálculo. (padrão=False)
    :return: resultado
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
    return print(f'= {f}.')


numero = int(input('Informe um número para calcular o fatorial: '))
opcao = str(input('Deseja ver o cálculo? [S/N] ')).strip().upper()[0]
if opcao == 'S':
    mostrar = True
else:
    mostrar = False


fat(numero, mostrar)
