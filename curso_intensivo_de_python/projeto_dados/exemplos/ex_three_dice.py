from die import Die

import pygal

# Cria um D6 e um D10
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Número de lançamentos
roll = 40000
# Faz alguns lançamentos e armazena os resultado em uma lista
results = []
for roll_num in range(roll):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analisa os resultados
values = set(results)
frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
for value in values:
    frequency = results.count(value)
    frequencies.append(frequency)

# Imprime os resultados
'''print(results)
print(values)
print(frequencies)'''

# Visualiza os resultados
hist = pygal.Bar()

hist.title = f"Results of rolling trhee D6 {roll} times."
hist.x_labels = [value for value in values]
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('exercise_three_dice_visual.svg')
