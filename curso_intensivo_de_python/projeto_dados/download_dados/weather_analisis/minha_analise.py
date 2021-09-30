import csv
from datetime import datetime

import converter
from matplotlib import pyplot as plt
arquivo = 'sitka_weather_2014.csv'

with open(arquivo) as f:  # ABRIR ARQUIVO
    leitor = csv.reader(f)  # LÊ O OBJETO E SALVA NUMA VARIÁVEL
    cabecalho = next(leitor)  # LÊ O CABEÇALHO (1ª LINHA)

    # print(cabecalho)
    # for n, h in enumerate(cabecalho):
    #    print(f'{n}: {h}')
    # SALVA APENAS OS DADOS DESEJADOS
    datas, temps_max, temps_min, umids_max, umids_med, umids_min, chuvas = [], [], [], [], [], [], []
    for linha in leitor:  # LÊ CADA LINHA, PEGA CADA DADO DESEJADO
        data_atual = datetime.strptime(linha[0], '%Y-%m-%d')
        temp_max = converter.fahrenheit_to_celsius(float(linha[1]))
        temp_min = converter.fahrenheit_to_celsius(float(linha[3]))
        umid_max = linha[7]
        umid_med = linha[8]
        umid_min = linha[9]
        chuva = converter.inch_to_milimeters(float(linha[19]))

        # ADICIONA NAS RESPECT LISTAS
        datas.append(data_atual)
        temps_max.append(temp_max)
        temps_min.append(temp_min)
        umids_max.append(umid_max)
        umids_med.append(umid_med)
        umids_min.append(umid_min)
        chuvas.append(chuva)  # ADICIONA NA LISTA
# print(f"{'DATA':<20}{'MAX':>5}{'MIN':>5}{'CHUVA':>5}")
for n, data in enumerate(datas):
    # print(f'{data}:{temps_max[n]:>5.1f}{temps_min[n]:>5.1f}{chuvas[n]:>5.0f}mm')
    print(f'{data}: {umids_max[n]} . {umids_med[n]} . {umids_min[n]}')

fig = plt.figure(dpi=128, figsize=(16, 9))
plt.plot(datas, temps_max, c='red')  # DEFINIÇÃO DA PLOTAGEM
plt.plot(datas, temps_min, c='purple')
# plt.plot(datas, umids_max, c='red')
# plt.plot(datas, umids_med, c='purple')
# plt.plot(datas, umids_min, c='aqua')
plt.bar(datas, chuvas, color='blue')
plt.fill_between(datas, temps_max, temps_min, facecolor='purple', alpha=0.25)  # FORMATAÇÃO
# plt.fill_between(datas, chuvas, facecolor='blue', alpha=0.5)
plt.title('Sitka, AK: CHUVAS - 2014', fontsize=24)
plt.xlabel('DATA', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('CHUVA (mm), TEMPERATURAS (máx-mín °C)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()  # PLOTAGEM DO GRÁFICO
