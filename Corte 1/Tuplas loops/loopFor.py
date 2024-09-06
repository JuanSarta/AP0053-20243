import time # Importamos la librería time, que nos permite manejar funciones relacionadas con el tiempo.

cadena = 'Python'

for letra in cadena: # Usamos un bucle for para recorrer cada letra de la variable 'cadena'.
    # Verificamos si la letra actual es 't'.
    if letra == 't':
        # Si la letra es 't', usamos continue para saltar a la siguiente iteración sin ejecutar el código restante.
        continue
    # Si la letra no es 't', la imprimimos en la consola.
    print(letra)
    # Hacemos una pausa de 1 segundo antes de continuar con la siguiente letra.
    time.sleep(1)
   
