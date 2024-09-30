from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division
from Operando import Operando 

class Menu:
    def __init__(self):
        self.opcion = None
        self.op1 = 0
        self.op2 = 0

    def mostrar_menu(self):
        while True:
            print("Bienvenido a mi calculadora :D")
            print("1) Suma")
            print("2) Resta")
            print("3) Multiplicacion")
            print("4) Division")
            print("5) Salir")
            self.opcion = input("¿Qué operación desea realizar? ")
            if self.opcion in ["1", "2", "3", "4"]:
                 while True:
                    try:
                        self.op1 = float(input("Ingrese el primer número: "))
                        self.op2 = float(input("Ingrese el segundo número: "))
                        break  # Si se ingresan correctamente los números, salir del bucle
                    except ValueError:
                        print("Error: Debe ingresar números válidos. Inténtelo de nuevo.")           
            operando = Operando(self)  # Crear una instancia de Operando y pasarle el menú actual
            operando.realizar_operacion()  # Llamar al método para realizar la operación
            if   self.opcion == "5":
                print("Saliendo del programa")
                break     
           
             