# Programa 1_7 calcula el area y el perimetro de un circulo ingresando el valor del radio por el usuario.
# Fecha: 2024/10/15

radio = float(input("Ingresa el valor del radio: "))
area = 3.1416 * radio ** 2
perimetro = 3.1416 * 2 * radio
print("El area del circulo es: "+str(area))

print("El perimetro del circulo es: "+str(perimetro))