# MEGA-SENA
# ajude o jogador da MegaSena a criar palpites
# PERGUNTE quantos jogos serão gerados
# SORTEIE 6 números de 1 a 60, sem repetições, para cada jogo. Cadastre numa lista composta
from random import randint
from time import sleep
jogos = []
jogo = []
num = 0
print('$$$ MEGA-$ENA $$$')
q = int(input('Quantos jogos sorteados deseja? '))
print(f'Sorteando {q} jogos...')
while q > 0:
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    q -= 1
    jogos.append(jogo[:])
    jogo.clear()

for n, j in enumerate(jogos):
    sleep(1)
    print(f'JOGO #{n+1} = {j}')
sleep(1)
print('=== BOA $ORTE! ===')
