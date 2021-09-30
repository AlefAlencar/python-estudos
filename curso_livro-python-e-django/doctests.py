# modelo14.py
# Para ver como funciona, altere um dos resultados esperados na
# docstring para ver como essa forma de teste funciona

"""Módulo de exemplo de doctests.
>>> dobro(3) + triplo(4)
18
>>> dobro(5) + triplo(5)
25
"""


def dobro(numero):
    """Calcula o dobro do número e retorna o resultado.
    >>> dobro(6)
    12
    >>> dobro(7)
    14
    """
    return numero * 2


def triplo(numero):
    """Retorna o triplo de um número.
    >>> triplo(6)
    18
    >>> triplo(7)
    21
    """
    return numero * 3


# Para exibir no prompt os testes falhados
# if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
