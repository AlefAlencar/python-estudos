# JOGO DA ADIVINHAÇÃO
# Melhore o JOGO 'ADIVINHA' (DESAFIO 028)
# Adivinhe o número escolhido 0 a 10 pelo computador até o usuário acertar
# RETORNE: quantidade de palpites até acertar

from random import randint
comput = randint(0, 11)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual número escolhi? [0 a 10] '))
    palpites += 1
    if jogador == comput:
        acertou = True
print('{} é o meu número, ACERTOU com {} tentativas.'.format(comput, palpites))
'''
i = 0
cont = 0
while i == 0:
    palpite = int(input('[COMPUTADOR]: - "Adivinhe qual número escolhi. u.u": '))
    cont += 1
    if esc == palpite:
        i = 1
    else:
        print('Não. u.u')
print('[COMPUTADOR]: - "Acertou! Escolhi o {}. Você deu {} palpites até acertar."'.format(esc, cont))
'''