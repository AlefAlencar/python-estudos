# FUNÇÃO maior() receba vários parâmetros (núm inteiros)
# ANALISAR todos os valores e dizer qual deles é o maior
from time import sleep
from random import randint


def maior(varios):
    print('ANALISANDO OS VALORES OBTIDOS...')
    sleep(1)
    ma = 0
    for n in varios:
        if n > ma:
            ma = n
    print(f'O MAIOR VALOR FOI O ===> {ma}\n{"-"*30}')


def gerador():
    print('GERANDO VALORES...')
    sleep(1)
    lista = []
    for n in range(0, 5):
        lista.append(randint(0, 100))
    print(lista)
    return lista


# PRINCIPAL
q = int(input('QUANTAS VEZES? '))
while q > 0:
    sleep(2)
    maior(gerador())
    q -= 1
print('<<<<<ENCERRADO>>>>>')
