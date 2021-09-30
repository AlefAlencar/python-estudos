# JOKENPÔ
# Faça o computador jogar  Jokenpô com você.
from random import choice
print('"Olá, vamos jogar Jo-ken-pô!" :D\nComputador x Jogador\nDigite o número correspondente:')
comp = choice([1, 2, 3])
jog = int(input('(1-Pedra, 2-Papel, 3-Tesoura) \n"Jo... Ken... Pô!": '))

if jog < 1 or jog > 3:
    print('"Digite o número de uma das três opções... vamos de novo"')
elif comp == jog:
    if comp == 1:
        print('Pedra x Pedra')
    elif comp == 2:
        print('Papel x Papel')
    else:
        print('Tesoura x Tesoura')
    print('"Deu empate!"')
elif comp == 1:
    if jog == 2:
        print('Pedra x Papel\n"Papel cobre a Pedra. Você venceu! -.-"')
    else:
        print('Pedra x Tesoura\n"Pedra quebra Tesoura. Eu venci!" :p')
elif comp == 2:
    if jog == 1:
        print('Papel x Pedra\n"Papel cobre a Pedra. Eu venci!" :p')
    else:
        print('Papel x Tesoura\n"Tesoura corta o Papel. Você venceu!" -.-')
elif comp == 3:
    if jog == 1:
        print('Tesoura x Pedra\n"Pedra quebra Tesoura. Você venceu!" -.-')
    else:
        print('Tesoura x Papel\n"Tesoura corta Papel. Eu venci!" :p')
