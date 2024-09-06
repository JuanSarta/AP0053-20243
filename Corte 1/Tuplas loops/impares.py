
# for i in range(1, 21):  # Itera sobre los números del 1 al 20 (inclusive)
#     residual = i % 2  # Calcula el residuo de la división de 'i' entre 2
#     if residual == 0:  # Si el residuo es 0, el número es par
#         print(f'{i} is even')  
#     else:
#         #print(f'{i} is odd')  
#         print(str(i) + ' is odd')  

# Segundo bloque comentado:
# for i in range(0, 6):  # Itera sobre los números del 0 al 5
#     result = i ** 3  # Eleva 'i' al cubo
#     print(result)  

# Tercer bloque:
times = input("Enter a number of times: ")  # Solicita al usuario ingresar un número
times = float(times)  # Convierte el valor ingresado en un número flotante
times = int(times)  # Convierte el número flotante en un número entero
print(type(times))  # Imprime el tipo de dato de 'times'
print(times)  # Imprime el valor de 'times'

if times == 0:  # Verifica si el valor de 'times' es 0
    print("Don't do anything")  
else:
    for i in range(1, times + 1):  # Si 'times' es mayor que 0, itera de 1 a 'times'
        print("i = ", i)  # Imprime el valor actual de 'i' en cada iteración
