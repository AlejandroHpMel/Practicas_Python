# Programa 8
# Fecha: 16/10/2024
# Elaborado por: Alejandro Martinez Martinez
print("Ejercicio que calcula el numero de minutos, horas y meses, dado el numero de dias por el usuario")
dias = int(input("Digite la cantidad de dias: "))
horas = dias * 24
min = horas * 60
meses = dias / 30
print("La cantidad de horas en esos dias es: "+str(horas))
print("La cantidad de minutos en esas horas es: "+str(min))
print("La cantidad de meses en esos dias es: "+str(meses))

