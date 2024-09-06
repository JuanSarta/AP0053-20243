a = input("Enter a number: ")  # Solicita al usuario un número y lo almacena como una cadena (string)
a = int(a)  # Convierte la cadena ingresada en un número entero
b = input("Enter b number: ")  # Solicita al usuario un segundo número y lo almacena como una cadena
b = float(b)  # Convierte la cadena ingresada en un número de punto flotante (float)

c = a + b  

if a == b: 
    print("equal")
else:
    print("Different") 

print("Type of a is: ", type(a))  
print("Type of b is: ", type(b))  
print("c = ", c)  

if type(a) == type(b):  # Comprueba si 'a' y 'b' son del mismo tipo de dato
    print("a and b are of the same type")  
else:
    print("a and b are of different type")  
