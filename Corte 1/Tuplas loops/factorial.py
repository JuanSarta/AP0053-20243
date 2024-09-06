while True:  # Bucle infinito que se ejecutará hasta que el programa sea detenido manualmente
    value = int(input("Enter a positive integer value: ")) 
    print("Value: ", value)  
    
    a = isinstance(value, int)  # Verifica si el valor ingresado es un entero y almacena el resultado en 'a'
    
    if a == True and value > 0:  # Comprueba si 'a' es verdadero (el valor es un entero) y si el valor es mayor que 0
        fact = 1  # Inicializa la variable 'fact' que se usará para calcular el factorial
        for i in range(1, value + 1):  # Bucle 'for' que itera desde 1 hasta 'value' (incluido)
            fact = fact * i  # Multiplica 'fact' por el valor de 'i' en cada iteración
        print(f'The factorial of {value} is: ', fact)  # Imprime el factorial del número ingresado
    else:
        print("Please, enter a positive integer number")  # Si el número no es positivo o no es entero, muestra un mensaje de error
