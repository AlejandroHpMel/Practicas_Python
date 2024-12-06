# Explicación Detallada del Programa 6
El código completo se ve así:

```def operaciones(num1, num2, digitos):```

```suma = num1 + num2```

```resta = num1 - num2```

```multiplicación = num1 * num2```

```division = float(num1 / num2)```

```modulo = num1 % num2```

```print(f'la suma de {num1} + {num2} es: {suma}')```

```print(f'la resta de {num1} - {num2} es: {resta}')```

```print(f'la multiplicación de {num1} * {num2} es: {multiplicación}')```

```print(f'la division de {num1} / {num2} es: {division:.{digitos}f}')```

```print(f'el modulo de {num1} % {num2} es: {modulo}\n\n')```

```# Solicitar datos al usuario```

```num2 = int(input('Ingrese el segundo número: '))```

```num1 = int(input('Ingrese el primer número: '))```

```digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y modulo:\n'))```

```operaciones(num1, num2, digitos)```

```operaciones(140, 8, 5)```
#### Definición de la Función operaciones
```def operaciones(num1, num2, digitos):```

```suma = num1 + num2```

```resta = num1 - num2```

```multiplicación = num1 * num2```

```division = float(num1 / num2)```

```modulo = num1 % num2```

```print(f'la suma de {num1} + {num2} es: {suma}')```

```print(f'la resta de {num1} - {num2} es: {resta}')```

```print(f'la multiplicación de {num1} * {num2} es: {multiplicación}')```

```print(f'la division de {num1} / {num2} es: {division:.{digitos}f}')```

```print(f'el modulo de {num1} % {num2} es: {modulo}\n\n')```

Función operaciones(num1, num2, digitos): Esta función toma tres argumentos: num1, num2 y digitos.

Operaciones Aritméticas:

suma: Suma de num1 y num2.

resta: Resta de num1 y num2.

multiplicación: Multiplicación de num1 y num2.

division: División de num1 entre num2, convertida a float.

modulo: Módulo de num1 y num2.

Impresión de Resultados:

Usa print() para mostrar los resultados de las operaciones.

La división se formatea para mostrar un número específico de decimales usando .{digitos}f.
#### Solicitar Datos al Usuario
```num2 = int(input('Ingrese el segundo número: '))```

```num1 = int(input('Ingrese el primer número: '))```

```digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y modulo:\n'))```

Entrada del Usuario:

num2: Solicita el segundo número.

num1: Solicita el primer número.

digitos: Solicita la cantidad de decimales a mostrar en la división.

#### Llamadas a la Función operaciones
```operaciones(num1, num2, digitos)```

```operaciones(140, 8, 5)```

Primera Llamada: Llama a la función operaciones con los valores ingresados por el usuario.

Segunda Llamada: Llama a la función operaciones con los valores 140, 8 y 5.
