# APRIMORANDO OS DICIONÁRIOS
# APRIMORE o desafio 093
# para vários jogadores
# e consulta detalhada do aproveitamento de cada jogador
jogador = dict()
jogadores = []
numP = gols = totalGols = c = 0
golsPartida = list()
# CADASTRAMENTO
print(f'{"#"*5}{"ESTATÍSTICAS DOS JOGADORES":^30}{"#"*5}\n{"="*10}{"CADASTRAMENTO":^20}{"="*10}')
while True:
    print(f'{"+" * 10}{"NOVO JOGADOR":^20}{"+" * 10}')
    jogador['Nome'] = str(input('NOME: ')).strip()
    numP = int(input('Nº de PARTIDAS: '))
    for c in range(0, numP):
        gols = int(input(f'=> GOLS NA {c+1}ª PARTIDA: '))
        golsPartida.append(gols)  # totalGols += gols
    jogador['Gols por partida'] = golsPartida[:]  # anexar em jogador
    # jogador['Total de gols'] = sum(golsPartida)  # totalGols
    jogadores.append(jogador.copy())  # salvar jogador em jogadores
    # RESET / c = 0
    jogador.clear()
    golsPartida.clear()  # totalGols = 0
    resp = ' '
    while resp not in 'SN':  # ?novo jogador?
        resp = str(input('ADICIONAR NOVO JOGADOR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
# EXIBIR TABELA
print(f'{"-"*40}\n{"ID":<5}{"JOGADOR":<20}{"PARTIDAS":>10}{"GOLS":>5}')
for k, v in enumerate(jogadores):
    print(f'{k:<5}{v["Nome"]:<20}{len(v["Gols por partida"]):>10}{sum(v["Gols por partida"]):>5}')
# CONSULTA DADOS_JOGADOR
print(f'{"="*10}{"CONSULTA DETALHADA":^20}{"="*10}')
while True:
    id = int(input('Digite o ID: '))
    if id < len(jogadores):
        print(f'DETALHES DE {jogadores[id]["Nome"]}:\nTotal de gols: {sum(jogadores[id]["Gols por partida"])}')  # {jogadores[id]["Total de gols"]}')
        for p, g in enumerate(jogadores[id]['Gols por partida']):
            print(f'¬ {p+1}ª partida = {g} gols.')
    else:
        print('ID não consta na lista.')
    print('-'*40)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('NOVA CONSULTA? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"<"*10}{"ENCERRADO":^20}{">"*10}')
