#Programa.4  programa que calcula los impuestos y dar un valor
#Fecha de elaboracion: 20210/10/22
#Elaborado por: Alejandro Martinez Martinez

def calcular_impuesto(valor, tasa_impuesto):
  impuesto = valor * (tasa_impuesto / 100)
  return impuesto

valor = float (input("Introduce el valor:"))
tasa_impuesto = float(input("introduce la tasa de impuesto en %:"))

print(f"El impuesto sobre {valor} con una tasa del {tasa_impuesto}% es: {calcular_impuesto(valor, tasa_impuesto):.2f}""\nGracias por usar nuestro sistema!")