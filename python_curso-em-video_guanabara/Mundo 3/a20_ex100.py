# DUAS FUNÇOES: sorteia() e somaPar()
# sorteia() sorteará 5 números int
# somaPar() mostrará a soma de todos os pares da sorteia()
import time
from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(lista)


def soma_par(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f'SOMANDO PARES DA LISTA {lista}, TOTAL = {total}')


# PRINCIPAL
numeros = list()  # lista vazia
sorteia(numeros)  # aqui ele preenche a lista. Pronto.
soma_par(numeros)  # aqui ele só vai pegar essa lista
