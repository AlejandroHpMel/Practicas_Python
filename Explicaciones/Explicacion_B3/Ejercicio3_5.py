#Programa.5 
#Fecha de elaboracion: 30/10/2024
#Elaborado por: Alejandro Martinez Martinez
print("Calcule el nivel de desempeño descrito con su calificacion dada pir el usuario, dada con la siguiente tabla")
calificaciones = int(input("Ingresa tu calificación para evaluar tu desempeño:"))


if calificaciones <= 60:
          print("Insufuciente")

elif calificaciones >= 70 and calificaciones <=79:
        print("Suficiente")

elif calificaciones >= 80 and calificaciones <= 89:
        print("Muy bien!")

elif calificaciones >= 90 and calificaciones <= 95:
        print("Notable!")

else:
     print("Excelente")


print("!Gracias por usar mi sistema de evaluación¡")                
