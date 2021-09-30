# CADASTRO DE JOGADOR DE FUTEBOL
# LEIA nome_jogador, núm_partidas, quantidade_gols/partida
# GUARDE tudo em um dicionário, incluindo total_gols
# jogador{nome, gols/partida, total_gols}
jogador = {'Nome': str(input('Nome: ')).strip()}
numP = int(input('Números de partidas jogadas: '))
golsPartida = list()
c = totalGols = 0
for c in range(0, numP):
    golsPartida.append(int(input(f'Número de gols na {c+1}º partida: ')))
jogador['Gols por partida'] = golsPartida[:]
print('='*30)
'''for i in jogador['Gols por partida']:
    totalGols += i'''
jogador['Total de gols'] = sum(golsPartida)
# MOSTRAR
print(f'{jogador}\n{"="*30}')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols por partida"])} partidas:')
for i, g in enumerate(jogador['Gols por partida']):
    print(f'Partida {i+1} ==> {g} gols.')
print(f'Um total de {jogador["Total de gols"]} gols.')
print('='*30)
