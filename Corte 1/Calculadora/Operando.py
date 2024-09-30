
from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division

class Operando:
    def __init__(self, menu):
        self.menu = menu
        
    def realizar_operacion(self):
            opcion = self.menu.opcion
            if opcion=="1":
                resultado = Suma().suma(self.menu.op1, self.menu.op2)
                print(f"La suma entre los numeros es {resultado}")
            elif opcion=="2":
                resultado = Resta().resta(self.menu.op1, self.menu.op2)
                print (f" La resta entre los numeros es {resultado}")  
            elif opcion=="3":
                resultado = Multiplicacion().multi(self.menu.op1, self.menu.op2)
                print (f" La multiplicacion entre los numeros es {resultado}")  
            elif opcion=="4":
                resultado = Division().division(self.menu.op1, self.menu.op2)
                print (f" La division entre los numeros es {resultado}") 
            elif opcion=="5":
                print ("Gracias por usar esta calculadora...")
                
            else:
             print (" Por favor ingresa una opcion valida")
            
                
                
            
    
       