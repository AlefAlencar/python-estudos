#!/usr/bin/env python3
# src/modelo05.py

# ITERADORES
'''sistemas = ['linux', 'windows', 'mac os']
sistemas_iterador = iter(sistemas)

sistema = next(sistemas_iterador)
print(sistema)
# linux
sistema = next(sistemas_iterador)
print(sistema)
# windows
sistema = next(sistemas_iterador)
print(sistema)
# mac os
sistema = next(sistemas_iterador)
# Traceback (most recent call last):
# ...
# StopIteration
#################################################'''
# Iterador com interrupção da iteração ao fim (raise StopIteration)


'''class Dobra:
    def __init__(self, numeros):
        self.indice = 0
        self.numeros = numeros
        self.tamanho = len(self.numeros)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == self.tamanho:
            raise StopIteration
        proximo = self.numeros[self.indice] * 2
        self.indice += 1
        return proximo


dobra = Dobra([1, 2, 3, 4])
for numero in dobra:
    print(numero)
# 2
# 4
# 6
# 8
iterador = Dobra([3, 6, 9])
next(iterador)
# 6
next(iterador)
# 12
next(iterador)
# 18
next(iterador)
# Traceback (most recent call last):
# ...
# StopIteration
#############################################'''


# GERADORES
# implementa uma nova versão de dobra, que obtém os mesmos resultados do exemplo anterior,
# escrevendo menos linhas de código.
def dobra(numeros):
    for numero in numeros:
        yield numero * 2


# Implementa a função geradora dobra que multiplica o valor dos elementos
# por dois.
for numero in dobra([1, 2, 3, 4]):
    print(numero)
# 2
# 4
# 6
# 8
gerador = dobra([3, 6, 9])
print(next(gerador))
# 6
print(next(gerador))
# 12
print(next(gerador))
# 18
print(next(gerador))
# Traceback (most recent call last):
# ...
# StopIteration
