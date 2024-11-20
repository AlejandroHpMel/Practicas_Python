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

# Solicitar el número de repeticiones
repeticiones = int(input("¿Cuántas veces desea realizar las operaciones?: "))

# Ciclo para repetir el código
for i in range(repeticiones):
    print(f"\n--- Repetición {i + 1} ---")
    # Multiplicar poe 2 cada que haga una iteracion
    num1 = num1 * 2
    num2 = num2 * 2
    
    # Llamar a la función
    operaciones(num1, num2, digitos)
# Ciclo para repetir el código hasta que el usuario escriba "salir"
while True:
    print("\n--- Nueva operación ---")
    # Solicitar datos al usuario
    opcion = input("Escriba 'salir' para terminar o presione Enter para continuar: ").strip()
    
    if opcion.lower() == "salir":
        print("Programa finalizado.")
        break  # Salir del ciclo si el usuario escribe "salir"