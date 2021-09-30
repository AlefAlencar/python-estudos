import pygal

from die import Die

# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisa os resultados
sides = set(results)
frequencies = []
for side in sides:
    frequency = results.count(side)
    frequencies.append(frequency)

# Imprime os resultados
print(results)
print(sides)
print(frequencies)

# Visualiza os resultados
hist = pygal.Bar()  # inicializa o Objeto

hist._title = "Results of rolling one D6 1000 times."
hist.x_labels = [side for side in sides]  # ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_labels = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
