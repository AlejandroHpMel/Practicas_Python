# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False  # Los números menores a 2 no son primos
    for i in range(2, int(numero ** 0.5) + 1):  # Verificar divisores hasta la raíz cuadrada del número
        if numero % i == 0:
            return False
    return True

# Solicitar al usuario un número entre 10 y 99
while True:
    try:
        numero = int(input("Ingrese un número entre 10 y 99: "))
        
        if 10 <= numero <= 99:
            # Verificar si el número es primo
            if es_primo(numero):
                print(f"El número {numero} es primo.")
            else:
                print(f"El número {numero} no es primo.")
            break  # Salir del ciclo si el número es válido
        else:
            print("El número debe estar entre 10 y 99. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
while True:
    print("\n--- Nueva operación ---")
    # Solicitar datos al usuario
    opcion = input("Escriba 'salir' para terminar o presione Enter para continuar: ").strip()
    
    if opcion.lower() == "salir":
        print("Programa finalizado.")
        break  # Salir del ciclo si el usuario escribe "salir"