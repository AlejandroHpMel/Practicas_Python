# Explicación Detallada del Programa 11
El código completo se ve así:

```import math```

```def es_primo(numero):```

```if numero < 2:```

```return False```

```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```return False```  

```return True```

```while True:```

```entrada = input("Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: ").lower()``` 

```if entrada == "salir":```

```print("¡Hasta luego, gracias por usar mi programa!")```

```break```

```try:```

```numero_usuario = int(entrada)```

```if 10 <= numero_usuario <= 99:```

```if es_primo(numero_usuario):```

```print(f"{numero_usuario} es un número primo.")```

```else:```

```print(f"{numero_usuario} no es un número primo.")```

```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```

```except ValueError:```


```print("Por favor, ingrese un número válido o 'salir' para terminar.")```
#### Importación del Módulo math
```import math```

Importación: Se importa el módulo math para utilizar funciones matemáticas, en este caso, math.sqrt() para calcular la raíz cuadrada.
#### Definición de la Función es_primo
```def es_primo(numero):```

```if numero < 2:```

```return False```   

```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```return False```   

```return True ``` 

Función es_primo(numero): Esta función determina si un número es primo.

Condición Inicial: Si el número es menor que 2, no es primo.

Bucle for: Itera desde 2 hasta la raíz cuadrada del número (inclusive).

Condición if: Si el número es divisible por cualquier número en este rango, no es primo.

Retorno True: Si no es divisible por ningún número en el rango, es primo.
#### Bucle while para Múltiples Entradas del Usuario
```while True:```

```entrada = input("Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: ").lower()```

```if entrada == "salir":```

```print("¡Hasta luego, gracias por usar mi programa!")```

```break```

Bucle while True: Este bucle se ejecuta indefinidamente hasta que se encuentre una instrucción break.

Entrada del Usuario: Solicita al usuario que ingrese un número o la palabra "salir".

Condición if: Si el usuario ingresa "salir", el programa imprime un mensaje de despedida y termina el bucle con break.
#### Intentar Convertir la Entrada a un Número
```try:```

```numero_usuario = int(entrada)```

```if 10 <= numero_usuario <= 99:```

```if es_primo(numero_usuario):```

```print(f"{numero_usuario} es un número primo.")```

```else:```

```print(f"{numero_usuario} no es un número primo.")```

```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```

Bloque try: Intenta convertir la entrada del usuario a un número entero.

Condición if: Verifica si el número está entre 10 y 99.

Llamada a la Función es_primo(): Comprueba si el número es primo.

Salida print(): Muestra el resultado al usuario.

Condición else: Si el número no está en el rango especificado, solicita al usuario que ingrese un número válido.
#### Manejo de Errores
```except ValueError:```

```print("Por favor, ingrese un número válido o 'salir' para terminar.")```

Bloque except: Captura el error si la entrada no puede ser convertida a un número entero.

Salida print(): Muestra un mensaje de error al usuario.
