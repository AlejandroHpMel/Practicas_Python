# Explicación Detallada del Programa 8
El código completo se ve así:

```def operaciones(num1, num2, digitos):```

```suma = num1 + num2```

```resta = num1 - num2```

```multiplicacion = num1 * num2```

```division = float(num1 / num2)```

```modulo = num1 % num2```

```print(f'La suma de {num1} + {num2} es: {suma}')```

```print(f'La resta de {num1} - {num2} es: {resta}')```

```print(f'La multiplicación de {num1} * {num2} es: {multiplicacion}')```

```print(f'La división de {num1} / {num2} es: {division:.{digitos}f}')```

```print(f'El módulo de {num1} % {num2} es: {modulo}\n\n')```

```# Ciclo while, repetir el programa hasta que el usuario ingrese "salir"```

```while True:```

```num2 = int(input('Ingrese el segundo número: '))```

```num1 = int(input('Ingrese el primer número: '))```

```digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))```

```iteraciones = int(input('Ingrese el número de iteraciones: '))```

```for i in range(iteraciones):```

```operaciones(num1, num2, digitos)```

```# Duplicar los valores de num1 y num2 para la siguiente iteración```

```num1 *= 2```

```num2 *= 2```

```respuesta = input("¿Desea realizar otra operación? (Escriba 'salir' para terminar o enter para continuar): ").lower()```

```if respuesta == "salir":```

```print("¡Hasta luego!")```

```break  # Salir del ciclo```
#### Definición de la Función operaciones
```def operaciones(num1, num2, digitos):```

```suma = num1 + num2```

```resta = num1 - num2```

```multiplicacion = num1 * num2```

```division = float(num1 / num2)```

```modulo = num1 % num2```

```print(f'La suma de {num1} + {num2} es: {suma}')```

```print(f'La resta de {num1} - {num2} es: {resta}')```

```print(f'La multiplicación de {num1} * {num2} es: {multiplicacion}')```

```print(f'La división de {num1} / {num2} es: {division:.{digitos}f}')```

```print(f'El módulo de {num1} % {num2} es: {modulo}\n\n')```

Función operaciones(num1, num2, digitos): Esta función toma tres argumentos: num1, num2 y digitos.

Operaciones Aritméticas:

suma: Suma de num1 y num2.

resta: Resta de num1 y num2.

multiplicacion: Multiplicación de num1 y num2.

division: División de num1 entre num2, convertida a float.

modulo: Módulo de num1 y num2.

Impresión de Resultados:

Usa print() para mostrar los resultados de las operaciones.

La división se formatea para mostrar un número específico de decimales usando .{digitos}f.
#### Ciclo while para Repetir el Programa
```while True:```

```num2 = int(input('Ingrese el segundo número: '))```

```num1 = int(input('Ingrese el primer número: '))```

```digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))```

```iteraciones = int(input('Ingrese el número de iteraciones: '))```

```for i in range(iteraciones):```

```operaciones(num1, num2, digitos)```

```# Duplicar los valores de num1 y num2 para la siguiente iteración```

```num1 *= 2```

```num2 *= 2```

```respuesta = input("¿Desea realizar otra operación? (Escriba 'salir' para terminar o enter para continuar): ").lower()```

```if respuesta == "salir":```

```print("¡Hasta luego!")```

```break  # Salir del ciclo```
Ciclo while True: Este bucle se ejecuta indefinidamente hasta que se encuentre una instrucción break.

Entrada del Usuario:

num2: Solicita el segundo número.

num1: Solicita el primer número.

digitos: Solicita la cantidad de decimales a mostrar en la división.

iteraciones: Solicita el número de iteraciones para realizar las operaciones.

Bucle for: Itera el número de veces especificado por iteraciones.

Llamada a operaciones(num1, num2, digitos): Realiza las operaciones aritméticas y muestra los resultados.

Duplicar Valores: Duplica los valores de num1 y num2 en cada iteración.

Condición if: Si el usuario ingresa "salir", el programa imprime un mensaje de despedida y termina el bucle con break.
