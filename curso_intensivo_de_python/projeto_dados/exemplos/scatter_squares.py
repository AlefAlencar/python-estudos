import matplotlib.pyplot as plt

x_values = list(range(1, 10001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap='Blues', edgecolors='none', s=20)
# Define o título, nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 11000, 0, 110000000])

plt.show()
