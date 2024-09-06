a = 1  
value = input('Ingrese un valor')  # Solicita al usuario que ingrese un valor.
value = int(value)  # Convierte el valor ingresado a un entero.

while a == 1:  
    for i in range(1, value + 1):  # Itera desde 1 hasta el valor ingresado por el usuario.
        conta = 0 
        for n in range(1, i + 1):  # Itera desde 1 hasta 'i' para encontrar los divisores de 'i'.
            residue = i % n 
            if residue == 0:  # Si el residuo es 0, significa que 'n' es divisor de 'i'.
                conta = conta + 1  # Incrementa el contador de divisores.
            
            # Las siguientes líneas son comentarios que puedes descomentar para depuración:
            # print("i = ", i) 
            # print("n = ", n)  
            # print("residue = ", residue)  # Imprime el residuo de 'i' % 'n'.
            # print("conta = ", conta)  # Imprime el número de divisores actuales de 'i'.

    if conta == 2:  # Si 'i' tiene exactamente 2 divisores, es un número primo.
        print(f'{i} es un primo')  # Imprime que 'i' es un número primo.
        print("\n")  # Imprime un salto de línea para mayor claridad.
    else:  # Si 'i' no tiene exactamente 2 divisores, no es primo.
        print(f'{i} NOOO es un primo')  # Imprime que 'i' no es primo.
        print("\n")  # Imprime un salto de línea.

    print('Do you want to continue?. Press 1 to do that')  # Pregunta si el usuario quiere continuar.
    a = input()  
    a = int(a)  

    if a != 1:  # Si el valor de 'a' no es 1, rompe el bucle y termina el programa.
        break  # Sale del bucle 'while'.

    value = input('Ingrese un valor')  # Si el usuario decide continuar, pide otro valor.
    value = int(value)  # Convierte el nuevo valor ingresado a entero.
