# CRIE PROGRAMA que gere 5 números aleatórios e coloque numa TUPLA
# MOSTRE: lista de números gerados, e o menor e o maior valor
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(numeros)
for n in numeros:
    print(f'{n}')
print(f'O maior foi {max(numeros)}\nO menor foi {min(numeros)}')

'''c = maior = menor = 0
lista = []
while c != 6:
    lista.append(randint(1, 100))
    if maior == 0:
        maior = menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
    c += 1
tupla = tuple(lista)
print(f'TUPLA: {tupla}\nMAIOR: {maior}\nMENOR: {menor}')
print('FIM')'''
