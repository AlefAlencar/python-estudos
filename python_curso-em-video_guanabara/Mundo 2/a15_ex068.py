# JOGO DE PAR OU ÍMPAR
# Jogue com o computador
# INTERROMPA quando jogador perder
# RETORNE total de vitórias consecutivas do jogador
from random import randint
valorComp = valorUser = soma = c = 0
while True:
    valorComp = randint(1, 6)
    opcaoUser = ' '
    while True:
        valorUser = int(input('Digite um valor [0 a 5]: '))
        if -1 < valorUser < 6:
            break
    while opcaoUser not in 'PI':
        opcaoUser = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    soma = valorComp + valorUser
    print(f'{valorComp} + {valorUser} = {soma}', end='')
    if soma % 2 == 0:
        print(' deu PAR.', end='')
        if opcaoUser == 'P':
            print(' VENCEU')
            c += 1
        else:
            print(' PERDEU')
            break
    else:
        print(' deu ÍMPAR.', end='')
        if opcaoUser == 'P':
            print(' PERDEU')
            break
        else:
            print(' VENCEU')
            c += 1
print(f'Você venceu {c} vezes.')
