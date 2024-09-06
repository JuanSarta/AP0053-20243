#Creación y manipulación básica de listas

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print(my_lista)  # Imprime la lista completa
print(type(my_lista))  # Imprime el tipo de dato (list)
print(my_lista[2])  # Imprime el tercer elemento de la lista

# Operaciones básicas sobre listas
print("my_lista size: ", len(my_lista))  # Imprime la longitud de la lista
print(my_lista[0:2])  # Imprime los primeros dos elementos (rango 0-2)
print(my_lista[:2])  # Otra forma de imprimir los primeros dos elementos
#---------------------------------------------------------------------------------------------
#Modificación de listas (Agregar, insertar y extender)

my_lista.append('Blanco')  # Agrega un nuevo elemento al final
print(my_lista)

my_lista.insert(3, 'Negro')  # Inserta un nuevo elemento en la posición 3
print(my_lista)

my_lista.extend(['Marron', 'Gris'])  # Extiende la lista concatenando otra lista
print(my_lista)
#---------------------------------------------------------------------------------------------

#Búsqueda y eliminación de elementos en listas

print(my_lista.index('Azul'))  # Encuentra el índice de un elemento

# Eliminación de elementos
# my_lista.remove('Magenta')  
my_lista.remove('Marron')  # Elimina el primer 'Marron' encontrado
print(my_lista)

my_lista.insert(8, 'Marron')  # Inserta 'Marron' nuevamente en la posición 8
print(my_lista)

print(my_lista.pop())  # Elimina y devuelve el último elemento
size = len(my_lista)
print("size = ", size)
#---------------------------------------------------------------------------------------------
#Multiplicación de listas y ordenamiento

my_lista_3 = my_lista * 3  # Multiplica la lista por 3 (repite su contenido)
print("my_lista_3: ", my_lista_3)

# Ordenar la lista
print("Sort:")
my_listaSort = my_lista.sort()  # Ordena la lista de manera alfabética
print(my_listaSort)  # Imprime None porque sort() no retorna nada, pero modifica la lista
#---------------------------------------------------------------------------------------------
#Ordenamiento de listas numéricas

my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()  # Ordena la lista numérica de menor a mayor
print(my_NumList)

# Ordenando de mayor a menor
my_NumList.sort(reverse=True)  # Ordena la lista numérica de mayor a menor
print("De mayor a menor: ", my_NumList)
#---------------------------------------------------------------------------------------------
#Introducción a tuplas

# Las tuplas son inmutables, es decir, no se pueden modificar una vez creadas
print("###########################")
print("############TUPLAS#########")

# Convertir una lista a tupla
my_tupla = tuple(my_lista)
print("my_tuple: ", my_tupla)

print(my_tupla[0])  # Acceder a elementos por índice
print(my_tupla[2])
#---------------------------------------------------------------------------------------------
#Operaciones con tuplas

# Verificar si un elemento está contenido en la tupla
print('Rojo' in my_tupla)  # Devuelve True si 'Rojo' está en la tupla
print(my_tupla.count('Rojo'))  # Cuenta cuántas veces aparece 'Rojo'

# Tupla con un solo elemento
my_tupla_unitaria = ('Blanco',)
print(my_tupla_unitaria)
#---------------------------------------------------------------------------------------------
#Empaquetado y desempaquetado de tuplas

# Empaquetado de tupla
my_tupla = 'Gaspar', 5, 8, 1999  # Empaquetar valores en una tupla sin paréntesis
print(my_tupla)

# Desempaquetado de tupla
nombre, dia, mes, año = my_tupla  # Desempaquetar los valores en variables
print(nombre)
print(dia)
print(mes)
print(año)

# Mostrar los valores desempaquetados
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)
#---------------------------------------------------------------------------------------------

# Convertir una tupla a lista
my_lista2 = list(my_tupla)  # Convierte la tupla en una lista
print(my_lista2)
