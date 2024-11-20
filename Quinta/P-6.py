#Alejandro Martinez Martinez
#Fecha de creacion: 16/11/2024
#Programa que utiliza una funcion para realizar operaciones matematicas basicas

#Funcion que realiza operaciones matematicas basicas
def operaciones(num1,num2,digitos):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    
    print(f"La suma del {num1} + {num2} es {suma}")
    print(f"La resta del {num1} - {num2} es {resta}")
    print(f"La multiplicacion del {num1} * {num2} es {multiplicacion}")
    print(f"La división del {num1} / {num2} es {division:.{digitos}f}")
    print(f"El modulo del {num1} % {num2} es {modulo}\n\n")

#Solicitar datos al usuario
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
digitos = int(input("Ingrese la cantidad de decimales a mostrar en la división y el modulo: "))

#Llamar a la funcion
operaciones(num1,num2,digitos)