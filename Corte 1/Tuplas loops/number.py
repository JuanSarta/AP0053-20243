import random  # Importa la librería 'random' para generar números aleatorios.
from matplotlib import pyplot as plt  # Importa la función 'pyplot' de 'matplotlib' para crear gráficos.

# Add your code below:
numbers_a = range(1, 13)  # Crea una secuencia de números del 1 al 12.
numbers_b = [random.randint(1, 1000) for i in range(12)]  # Genera una lista de 12 números aleatorios entre 1 y 1000.
plt.plot(numbers_a, numbers_b)  # Crea un gráfico de líneas usando 'numbers_a' como eje x y 'numbers_b' como eje y.
plt.show()  # Muestra el gráfico en pantalla.
