#Programa.12 
#Fecha de elaboracion: 04/11/2024
#Elaborado por: Alejandro Martinez Martinez
print("Metodo pop")
nombres = ['andrea', 'marifer', 'adan', 'lucero', 'nena']

# Eliminar el último elemento (sin pasar un índice)
elemento_eliminado = nombres.pop()
print("Elemento eliminado:", elemento_eliminado)
print("\nLista después de eliminar el último elemento:", nombres)

# Eliminar un elemento en un índice específico (por ejemplo, índice 2)
elemento_eliminado = nombres.pop(2)
print("Elemento eliminado en el índice 2:", elemento_eliminado)
print("\nLista después de eliminar el elemento en el índice 2:", nombres)