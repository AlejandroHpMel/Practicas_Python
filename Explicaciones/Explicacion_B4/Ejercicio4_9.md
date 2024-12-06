# Explicación Detallada del Programa 9
Código Completo

```import math```

```numero = int(input("Ingrese un número entre 10 y 99: "))```

```if 10 <= numero <= 99:```

```es_primo = True  # Variable que determina si es primo```
    
```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```es_primo = False  # Si es divisible, no es primo```

```break```

    
```# Resultado```

```if es_primo:```

```print(f"{numero} es un número primo.")```

```else:```

```print(f"{numero} no es un número primo.")```

```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```
#### Importación del Módulo math
```import math```

Importación: Se importa el módulo math para utilizar funciones matemáticas, en este caso, math.sqrt() para calcular la raíz cuadrada.
#### Solicitud de Entrada al Usuario
```numero = int(input("Ingrese un número entre 10 y 99: "))```

Función input(): Solicita al usuario que ingrese un número.

Conversión a Entero: int() convierte la entrada del usuario a un número entero.
#### Verificación del Rango del Número
```if 10 <= numero <= 99:```

```es_primo = True  # Variable que determina si es primo```

Condición if: Verifica si el número ingresado está dentro del rango permitido (10 a 99).

Variable es_primo: Se inicializa como True, asumiendo que el número es primo hasta que se demuestre lo contrario.
#### Verificación de Primalidad
```for i in range(2, int(math.sqrt(numero)) + 1):```

```if numero % i == 0:```

```es_primo = False  # Si es divisible, no es primo```

```break```

Bucle for: Itera desde 2 hasta la raíz cuadrada del número (inclusive).

Condición if: Si el número es divisible por cualquier número en este rango, es_primo se establece como False y se rompe el bucle.
#### Impresión del Resultado
```if es_primo:```

```print(f"{numero} es un número primo.")```

```else:```

```print(f"{numero} no es un número primo.")```
        
Condición if: Si es_primo es True, se imprime que el número es primo.

Condición else: Si es_primo es False, se imprime que el número no es primo.
#### Mensaje de Error para Números Fuera del Rango
```else:```

```print("Por favor, ingrese un número entre 10 y 99.")```

Condición else: Si el número ingresado no está dentro del rango permitido, se imprime un mensaje de error.
