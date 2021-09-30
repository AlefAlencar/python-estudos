# JOGO DE DADOS
# CRIE um programa onde 4 jogares joguem dados
# GUARDE os resultados num dicionário
# ORDENE o dicionário, o vencedor tirou o maior número
from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
print(jogos)
for k, v in jogos.items():
    sleep(1)
    print(f'O {k} tirou {v}.')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('====RANKING DOS JOGADORES====')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
