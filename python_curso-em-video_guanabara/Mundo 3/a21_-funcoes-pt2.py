'''# INTERACTIVE HELP
# DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    Função criada por Gustavo Guanabara do canal CursoEmVideo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)'''


'''# ARGUMENTOS OPCIONAIS
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma dá {s}.')


somar(3, 2, 5)
somar(8)
somar()'''


'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()'''


'''def funcao():
    n1 = 10  # *cria* como local, mesmo existindo n1 global
    global n2
    n2 = 20  # usa a variável global
    print(f'N1 dentro vale {n1}')
    print(f'N2 dentro vale {n2}')


n1 = 1  # *cria* como global
n2 = 2
print(f'N1 fora antes vale {n1}')
print(f'N2 fora antes vale {n2}')

funcao()
print(f'N1 fora depois vale {n1}')
print(f'N2 fora depois vale {n2}')'''


'''def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(1, 2, 3)
r2 = somar(10, 20, 30)
r3 = somar(100, 200, 300)
print(f'Os resultados foram {r1}, {r2} e {r3}')'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(p=0):
    if p % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
if par(n):
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')
