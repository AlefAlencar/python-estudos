# Inteiro aleatório de 0 a 5
# LEIA: Usuário deve tentar adivinhar qual foi o num
# RETORNE: se ele venceu ou perdeu
from random import randint
from time import sleep
num = randint(0, 5)
esc = int(input('Adivinhe qual foi o número sorteado de 0 a 5? '))

print('Processando...')
sleep(3)
print('O número sorteado foi {}.'.format(num))
if num == esc:
    print('Você acertou!')
else:
    print('Você errou...')
