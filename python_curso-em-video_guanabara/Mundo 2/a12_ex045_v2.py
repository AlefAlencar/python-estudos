# JOKENPÔ
# Faça o computador jogar  Jokenpô com você.
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
jogador = int(input('Opções:\n'
                    '[ 0 ] PEDRA\n'
                    '[ 1 ] PAPEL\n'
                    '[ 2 ] TESOURA\n'
                    'Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('='*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*10)
if jogador > 2:
    print('Opção INVÁLIDA. Tente novamente.')
elif computador == 0: # computador PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA')
    elif jogador == 2:
        print('DERROTA')
elif computador == 1: # computador PAPEL
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA')
elif computador == 2: # computador TESOURA
    if jogador == 0:
        print('VITÓRIA')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')