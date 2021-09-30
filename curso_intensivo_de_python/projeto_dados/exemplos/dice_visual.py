import pygal

from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analisa os resultados
values = set(results)
frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
for value in values:
    frequency = results.count(value)
    frequencies.append(frequency)

# Imprime os resultados
print(f'results: {results}')
print(f'values: {values}')
print(f'frequencies: {frequencies}')

# Visualiza os resultados
hist = pygal.Bar()  # inicializa o Objeto

hist._title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [value for value in values]  # ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_labels = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
