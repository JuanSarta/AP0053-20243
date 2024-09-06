for i in range(100, 301):  # Bucle 'for' que itera sobre los números del 100 al 300 (incluido 300)
    if (i % 12) != 0:      # Comprueba si el número 'i' no es divisible por 12
        continue           # Si el número no es divisible por 12, pasa a la siguiente iteración
    print(i)               # Si el número es divisible por 12, lo imprime
