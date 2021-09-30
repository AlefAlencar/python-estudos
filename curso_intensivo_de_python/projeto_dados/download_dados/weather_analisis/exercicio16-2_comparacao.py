from matplotlib import pyplot as p
from converter import Arquivo

arquivo1 = 'sitka_weather_2014.csv'
arquivo2 = 'death_valley_2014.csv'

# ARQUIVO 1
bd1 = Arquivo(arquivo1)
bd1.carregar_dados()
bd1.imprimir_cabecalho()
bd1.imprimir_dados()

# ARQUIVO 2
bd2 = Arquivo(arquivo2)
bd2.carregar_dados()
# bd2.imprimir_cabecalho()
# bd2.imprimir_dados()

# CÁLCULOS E CÓPIA DOS DADOS DOS OBJETOS
amplitude_temp1, amplitude_temp2, dif_temp_maxs, dif_temp_mins = [], [], [], []

# cópias
datas1 = bd1.datas[:]
temp_max1 = bd1.temps_max[:]
temp_min1 = bd1.temps_min[:]

datas2 = bd2.datas[:]
temp_max2 = bd2.temps_max[:]
temp_min2 = bd2.temps_min[:]

# amplitude da temperatura
for i, temp in enumerate(temp_max1):
    amplitude_temp1.append(temp - temp_min1[i])
for i, temp in enumerate(temp_max2):
    amplitude_temp2.append(temp - temp_min2[i])

# comparação entre os locais (death valley, CA - sitka, AK)
for i, temp in enumerate(temp_max2):
    try:
        dif_temp_maxs.append(temp - temp_max1[i])
    except IndexError:
        pass
for i, temp in enumerate(temp_min2):
    try:
        dif_temp_mins.append(temp - temp_min1[i])
    except IndexError:
        pass

# PLOTAGEM DO GRÁFICO
fig = p.figure(dpi=128, figsize=(10, 7))
# temperaturas
'''p.plot(datas1, temp_max1, c='red')
p.plot(datas1, temp_min1, c='blue')
p.plot(datas2, temp_max2, c='green')
p.plot(datas2, temp_min2, c='yellow')'''
# amplitudes
p.plot(amplitude_temp1, c='aqua')
p.plot(amplitude_temp2, c='yellow')
# diferença das máximas e mínimas entre as duas regiões
'''p.plot(dif_temp_maxs, c='red')
p.plot(dif_temp_mins, c='blue')'''

# fig.autofmt_xdate()
p.show()
