# ALISTAMENTO MILITAR
# LEIA: ano de nascimento
# RETORNE: Ainda vai, está na hora, ou passou do tempo; Tempo para o alistamento.
from datetime import date

print('Olá, recruta! Bem-vindo ao Alistamento Militar.')
anonasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite o seu sexo:\n[M] Masculino\n[F] Feminino\n')).upper()
minimo = 18
anohoje = date.today().year

if not sexo == 'M':
    print('Apenas homens devem fazer o alistamento militar obrigatório.')
elif anonasc == anohoje - minimo:
    print('Já está na hora de se alistar, soldado! :D #ChamadoDoDever')
elif anonasc < anohoje - minimo:
    print('Está tentando fugir de seu dever, soldado? >:| '
          '\nJá devia ter se alistado a {} anos, em {}! #Atrasado'.format(anohoje - minimo - anonasc, minimo + anonasc))
else:
    print('Sua hora vai chegar, recruta! Você poderá se alistar em {}. Ainda falta {} anos. #Prepare-se'.format(anonasc + minimo, anonasc + minimo - anohoje))
