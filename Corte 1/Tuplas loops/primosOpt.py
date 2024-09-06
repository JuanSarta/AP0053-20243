# 9) Imprimir los números primos existentes entre 0 y 30
# Se recorre el rango de números y se identifica si son primos contando los divisores
tope_rango = 30
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):  # Verifica si hay divisores de 'n'
        if n % div == 0:
            primo = False  # Si hay un divisor, no es primo
    if primo:
        print(n)  # Si no tiene divisores, es primo
    else:
        primo = True  # Restablecer la variable para el siguiente número
    n += 1


# 10) Optimización del código anterior utilizando 'break'
# Detiene la búsqueda de divisores en cuanto encuentra el primero, mejorando el rendimiento
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break  # Si encuentra un divisor, no sigue buscando
    if primo:
        print(n)
    else:
        primo = True
    n += 1


# 11) Comparar ciclos con y sin 'break' para medir optimización
# Mide el número de ciclos ejecutados con ambos enfoques
ciclos_sin_break = 0
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):
        ciclos_sin_break += 1  # Contador de ciclos sin 'break'
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos sin break: ' + str(ciclos_sin_break))

# Contando ciclos con 'break'
ciclos_con_break = 0
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):
        ciclos_con_break += 1  # Contador de ciclos con 'break'
        if n % div == 0:
            primo = False
            break  # Detiene la búsqueda si encuentra un divisor
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos con break: ' + str(ciclos_con_break))

# Mostrar la optimización lograda
print('Se optimizó a un ' + str(ciclos_con_break / ciclos_sin_break) + '% de ciclos aplicando break')


# 12) Evaluar la optimización con un rango mayor (hasta 100)
# Similar al punto 11, pero con un rango más grande
tope_rango = 100
ciclos_sin_break = 0
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):
        ciclos_sin_break += 1
        if n % div == 0:
            primo = False
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos sin break (rango 100): ' + str(ciclos_sin_break))

# Contando ciclos con 'break' en el rango mayor
ciclos_con_break = 0
n = 0
primo = True
while n < tope_rango:
    for div in range(2, n):
        ciclos_con_break += 1
        if n % div == 0:
            primo = False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos con break (rango 100): ' + str(ciclos_con_break))

# Mostrar el porcentaje de optimización en el rango mayor
print('Se optimizó a un ' + str(ciclos_con_break / ciclos_sin_break) + '% de ciclos aplicando break')
