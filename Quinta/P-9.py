# Solicitar al usuario un número entre 10 y 99
numero = input("Ingrese un número entre 10 y 99: ")

# Validar que el número ingresado sea un entero
if numero.isdigit():  # Verifica si el valor ingresado es un número positivo
    numero = int(numero)
    
    if 10 <= numero <= 99:  # Verifica si está dentro del rango
        # Determinar si el número es primo
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        
        # Mostrar resultado
        if es_primo:
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
    else:
        print("El número debe estar entre 10 y 99.")
else:
    print("Por favor, ingrese un número válido.")