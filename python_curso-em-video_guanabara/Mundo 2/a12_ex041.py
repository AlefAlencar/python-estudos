# CLASSIFICANDO NADADORES
# LEIA: ano de nascimento.
# RETORNE: Categoria.
# <=9 = Mirim, <=14: infantil, <=19 = Junior, <=25 = Sênior, >25 = Master.
import datetime

print('Olá, nadador!')
anonasc = int(input('Digite seu ano de nascimento: '))
anohoje = datetime.datetime.today().year
idade = anohoje - anonasc
print('A sua classificação é: ')
if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil.')
elif idade <= 19:
    print('Junior.')
elif idade <= 25:
    print('Senior.')
elif idade > 25:
    print('Master.')
