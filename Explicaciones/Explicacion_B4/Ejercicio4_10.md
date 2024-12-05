# Explicación Detallada del Programa 10
El código completo se ve así:

```import math```

```# Función que determina si un número es primo```

```def es_primo(numero):```

```if numero < 2:```

```return False```

```# divisible entre 2 y raiz```

```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```return False  # Divisible, no es primo```
    
```return True  # Si no fue divisible por ningún número, es primo```

```# Solicitar al usuario que ingrese un número```

```numero_usuario = int(input("Ingrese un número entre 10 y 99: "))```

```# Comprobar si el número es primo y mostrar el resultado```

```if 10 <= numero_usuario <= 99:```

```if es_primo(numero_usuario):```

```print(f"{numero_usuario} es un número primo.")```

```else:```

```print(f"{numero_usuario} no es un número primo.")```

```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```
#### Importación del Módulo math
```import math```

Importación: Se importa el módulo math para utilizar funciones matemáticas, en este caso, math.sqrt() para calcular la raíz cuadrada.

#### Definición de la Función es_primo
```def es_primo(numero):```

```if numero < 2:```

```return False```
    
```# divisible entre 2 y raiz```

```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```return False  # Divisible, no es primo```
    
```return True  # Si no fue divisible por ningún número, es primo```

Función es_primo(numero): Esta función determina si un número es primo.

Condición Inicial: Si el número es menor que 2, no es primo.

Bucle for: Itera desde 2 hasta la raíz cuadrada del número (inclusive).

Condición if: Si el número es divisible por cualquier número en este rango, no es primo.

Retorno True: Si no es divisible por ningún número en el rango, es primo.
#### Solicitar al Usuario que Ingrese un Número
```numero_usuario = int(input("Ingrese un número entre 10 y 99: "))```

Función input(): Solicita al usuario que ingrese un número.

Conversión a Entero: int() convierte la entrada del usuario a un número entero.
#### Comprobar si el Número es Primo y Mostrar el Resultado
```if 10 <= numero_usuario <= 99:```

```if es_primo(numero_usuario):```

```print(f"{numero_usuario} es un número primo.")```

```else:```

```print(f"{numero_usuario} no es un número primo.")```

```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```

Condición if: Verifica si el número ingresado está entre 10 y 99.

Llamada a la Función es_primo(): Comprueba si el número es primo.

Salida print(): Muestra el resultado al usuario.

Condición else: Si el número no está en el rango especificado, solicita al usuario que ingrese un número válido.
