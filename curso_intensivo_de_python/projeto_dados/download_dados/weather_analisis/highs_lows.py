import csv
from datetime import datetime

import converter
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
# Obtém as temperaturas máximas
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # first_row = next(reader)
    # print(header_row)
    # print(first_row)
    # Para entender a posição do cabeçalho
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = converter.fahrenheit_to_celsius(int(row[1]))
            low = converter.fahrenheit_to_celsius(int(row[3]))
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# print(highs)
# print(lows)
# Faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(8, 5))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.5)

# Formata o gráfico
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
