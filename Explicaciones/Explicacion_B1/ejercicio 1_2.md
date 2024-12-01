Explicación Detallada del Código
Este código en Python solicita al usuario su nombre y luego imprime un mensaje personalizado. Vamos a analizar cada línea para entender cómo funciona.

Primera Línea de Código
print("Ejercicio 1.2 Solicitar nombre e imprimir mensaje personalizado")
Función print(): Esta función se utiliza para mostrar texto en la consola.
Cadena de Texto: "Ejercicio 1.2 Solicitar nombre e imprimir mensaje personalizado" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').
Propósito: Esta línea muestra el texto "Ejercicio 1.2 Solicitar nombre e imprimir mensaje personalizado" en la consola, indicando al usuario el propósito del ejercicio.
Segunda Línea de Código
nombre = input("¿Cómo te llamas? ")
Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.
Cadena de Texto: "¿Cómo te llamas? " es el mensaje que se muestra al usuario para solicitar su nombre.
Variable nombre: La entrada del usuario se guarda en la variable nombre. Una variable es un espacio en la memoria donde se puede almacenar información para usarla más adelante.
Propósito: Esta línea solicita al usuario que ingrese su nombre y almacena esa información en la variable nombre.
Tercera Línea de Código
print("Hola, " + nombre)
Función print(): Nuevamente, se utiliza para mostrar texto en la consola.
Concatenación de Cadenas: "Hola, " + nombre combina (concatena) la cadena "Hola, " con el contenido de la variable nombre. La concatenación une dos cadenas de texto en una sola.
Propósito: Esta línea muestra un saludo personalizado en la consola, utilizando el nombre que el usuario ingresó. Por ejemplo, si el usuario ingresó "Alejandro", la consola mostrará "Hola, Alejandro".
Resumen
El código completo se ve así:

print("Ejercicio 1.2 Solicitar nombre e imprimir mensaje personalizado")
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)
Primera Línea: Muestra el título del ejercicio.
Segunda Línea: Solicita al usuario que ingrese su nombre.
Tercera Línea: Imprime un saludo personalizado utilizando el nombre del usuario.
