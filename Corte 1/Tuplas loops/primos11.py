import time  # Importa la librería 'time' para medir el tiempo de ejecución.

inicio = time.time()  # Guarda el tiempo de inicio para medir la duración del proceso.

for i in range(1, 31):  # Itera sobre los números desde 1 hasta 30.
    conta = 0  # Inicializa un contador para contar los divisores de 'i'.
    for n in range(1, i + 1):  # Itera desde 1 hasta 'i' para encontrar sus divisores.
        residue = i % n  # Calcula el residuo de dividir 'i' entre 'n'.
        if residue == 0:  # Si el residuo es 0, significa que 'n' es un divisor de 'i'.
            conta = conta + 1  # Incrementa el contador si encuentra un divisor.
    if conta == 2:  # Si el número tiene exactamente 2 divisores (es decir, es primo).
        print(f'{i} es un primo')  # Imprime que el número 'i' es primo.
        print("\n")  # Imprime una línea en blanco para separar los números primos.

fin = time.time()  # Captura el tiempo después de completar el bucle.

print("t = ", (fin - inicio) * 1000)  # Calcula y muestra el tiempo total de ejecución en milisegundos.
