import time  
inicio = time.time()  # Guarda el tiempo de inicio antes de comenzar el cálculo.

for i in range(0, 31):  # Bucle que itera desde 0 hasta 30 (inclusive).
    conta = 0  # Inicializa un contador para contar los divisores de 'i'.
    for n in range(1, i+1):  # Bucle interno que va desde 1 hasta 'i', para verificar si 'n' es divisor de 'i'.
        residue = i % n  # Calcula el residuo de la división de 'i' entre 'n'.
        if residue == 0:  # Si el residuo es 0, 'n' es un divisor de 'i'.
            conta = conta + 1  # Incrementa el contador de divisores.
              
    if conta == 2:  # Si 'i' tiene exactamente 2 divisores (solo divisible por 1 y por sí mismo), es un número primo.
        print(f'{i} es un primo')  # Imprime que 'i' es un número primo.
        
fin = time.time()  # Guarda el tiempo al finalizar los cálculos.
print("t = ", (fin - inicio) * 1000)  # Calcula y muestra el tiempo total de ejecución en milisegundos.
