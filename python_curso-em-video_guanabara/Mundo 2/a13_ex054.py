# GRUPO DA MAIORIDADE
# LEIA: ano de nascimento de 7 pessoas
# RETORNE: x que não atingiram a maioridade
from datetime import date
x = 7
for c in range(1, 8):
    d = int(input('Digite a data de nascimento da {}ª pessoa: '.format(c)))
    i = date.today().year - d
    if i >= 21:
        x -= 1
print('{} pessoas não atingiram a maioridade.'.format(x))
