# Explicación Detallada del Programa 2
El código completo se ve así:

```print("Comparación de números enteros")```

```num1 = int(input("Ingresa el primer número:"))```

```num2 = int(input("Ingresa el segundo número:"))```

```if (num1 > num2):```

```print(str(num1) + "\nEs mayor que " + str(num2))```

```elif num1 == num2:```

```print(str(num1) + "\nEs igual que " + str(num2))```

```else:```
   
```print(str(num1) + "\nEs menor que " + str(num2))```

```print("¡Gracias por usar mi programa!")```
#### Primera Línea de Código
```print("Comparación de números enteros")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Comparación de números enteros" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Comparación de números enteros" en la consola, indicando al usuario el propósito del ejercicio.
#### Segunda Línea de Código
```num1 = int(input("Ingresa el primer número:"))```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "Ingresa el primer número:" es el mensaje que se muestra al usuario para solicitar el primer número.

Función int(): Convierte la entrada del usuario (que es una cadena de texto) en un número entero.

Variable num1: La entrada convertida se guarda en la variable num1.

Propósito: Esta línea solicita al usuario que ingrese el primer número y lo convierte a un número entero.
#### Tercera Línea de Código
```num2 = int(input("Ingresa el segundo número:"))```

Función input(): Solicita al usuario que ingrese el segundo número.

Cadena de Texto: "Ingresa el segundo número:" es el mensaje que se muestra al usuario.

Función int(): Convierte la entrada del usuario en un número entero.

Variable num2: La entrada convertida se guarda en la variable num2.

Propósito: Esta línea solicita al usuario que ingrese el segundo número y lo convierte a un número entero.
#### Cuarta Línea de Código
```if (num1 > num2):```
```print(str(num1) + "\nEs mayor que " + str(num2))```

Estructura Condicional if: Evalúa si num1 es mayor que num2.

Operador >: Compara si num1 es mayor que num2.

Función print(): Si la condición es verdadera, muestra el texto "num1\nEs mayor que num2" en la consola.

Función str(): Convierte los números num1 y num2 a cadenas de texto para que puedan ser concatenados.

Propósito: Esta línea verifica si num1 es mayor que num2 y muestra un mensaje correspondiente.
#### Quinta Línea de Código
```elif num1 == num2:```

```print(str(num1) + "\nEs igual que " + str(num2))```

Estructura Condicional elif: Evalúa si num1 es igual a num2, si la condición anterior no se cumplió.

Operador ==: Compara si num1 es igual a num2.

Función print(): Si la condición es verdadera, muestra el texto "num1\nEs igual que num2" en la consola.

Función str(): Convierte los números num1 y num2 a cadenas de texto para que puedan ser concatenados.

Propósito: Esta línea verifica si num1 es igual a num2 y muestra un mensaje correspondiente.
#### Sexta Línea de Código
```else:```

```print(str(num1) + "\nEs menor que " + str(num2))```

Estructura Condicional else: Se ejecuta si ninguna de las condiciones anteriores se cumplió.

Función print(): Muestra el texto "num1\nEs menor que num2" en la consola.

Función str(): Convierte los números num1 y num2 a cadenas de texto para que puedan ser concatenados.

Propósito: Esta línea muestra un mensaje indicando que num1 es menor que num2 si no se cumplen las condiciones anteriores.
#### Séptima Línea de Código
```print("¡Gracias por usar mi programa!")```

Función print(): Muestra texto en la consola.

Cadena de Texto: "¡Gracias por usar mi programa!" es una cadena de caracteres.

Propósito: Esta línea muestra un mensaje de agradecimiento al usuario por usar el programa.
