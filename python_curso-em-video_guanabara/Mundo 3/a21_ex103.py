# FUNCAO ficha(nome_jog, quant_gols_campeonato)
# LEIA nome do jogador e a quantidade de gols no campeonato
# Se um dos dados for omitido, retorne: <desconhecido>, 0
def jogador(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')


nome = str(input('Digite o nome do jogador: ')).strip()
quantGols = str(input(f'Quantos gols {nome} fez no campeonato? '))
if quantGols.isnumeric():
    quantGols = int(quantGols)
else:
    quantGols = 0
if nome == '':
    jogador(gols=quantGols)
else:
    jogador(nome, quantGols)
