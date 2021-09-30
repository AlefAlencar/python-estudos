# CAMPEONATO BRASILEIRO
# CRIE TUPLA com os 20 primeiros colocados do Campeonato Brasileiro de Futebol em ordem de colocação
# MOSTRE:
# A) 5 primeiros colocados
# B) 4 últimos
# C) Lista toda em ordem alfabética
# D) Posição do time Chapecoense
serieA = ('Fortaleza', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Bahia',
          'Fluminense', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Corinthians',
          'Ceará', 'Santos', 'Cuiabá', 'Sport', 'São Paulo', 'Juventude',
          'Internacional', 'Grêmio', 'América-MG', 'Chapecoense')
print(f'Brasileirão: {serieA}')
time = ' '
c = 0
print(f'== TOP 5 ==\n{serieA[0:5]}')
print(f'== Z4 ==\n{serieA[-4:]}')
print('ORDEM ALFABÉTICA:', sorted(serieA))
while True:
    time = str(input('>>>>> Posição de qual time? ')).strip().capitalize()
    if time in serieA:
        break
print(f'O {time} está na {serieA.index(time)+1}ª posição.')
print('FIM')
