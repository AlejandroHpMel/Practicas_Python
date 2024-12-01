# Explicación Detallada del Código Programa 6
#### El código completo se ve así:

```print("Ejercicio 6: Calcular el área de un triángulo")```

```base = float(input("¿Cuánto mide la base? "))```

```altura = float(input("¿Cuánto mide la altura? "))```

```area = base * altura / 2```

```print("El área de este triángulo es: " + str(area))```

#### Primera Línea de Código
```print("Ejercicio 6: Calcular el área de un triángulo")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Ejercicio 6: Calcular el área de un triángulo" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Ejercicio 6: Calcular el área de un triángulo" en la consola, indicando al usuario el propósito del ejercicio.
#### Segunda Línea de Código
```base = float(input("¿Cuánto mide la base? "))```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "¿Cuánto mide la base? " es el mensaje que se muestra al usuario para solicitar la medida de la base.

Función float(): Convierte la entrada del usuario (que es una cadena de texto) en un número de punto flotante (decimal).

Variable base: La entrada convertida se guarda en la variable base.

Propósito: Esta línea solicita al usuario que ingrese la medida de la base del triángulo y la convierte a un número decimal.
#### Tercera Línea de Código
```altura = float(input("¿Cuánto mide la altura? "))```

Función input(): Solicita al usuario que ingrese la medida de la altura.

Cadena de Texto: "¿Cuánto mide la altura? " es el mensaje que se muestra al usuario.

Función float(): Convierte la entrada del usuario en un número de punto flotante.

Variable altura: La entrada convertida se guarda en la variable altura.

Propósito: Esta línea solicita al usuario que ingrese la medida de la altura del triángulo y la convierte a un número decimal.
#### Cuarta Línea de Código
```area = base * altura / 2```

Operación Aritmética: base * altura / 2 calcula el área del triángulo utilizando la fórmula del área de un triángulo: (\text{Área} = \frac{1}{2} \times \text{base} \times \text{altura}).

Variable area: El resultado del cálculo se guarda en la variable area.

Propósito: Esta línea realiza el cálculo del área del triángulo utilizando las medidas de la base y la altura proporcionadas por el usuario.

#### Quinta Línea de Código
```print("El área de este triángulo es: " + str(area))```

Función print(): Muestra texto en la consola.

Concatenación de Cadenas: "El área de este triángulo es: " + str(area) combina (concatena) la cadena de texto con el valor de area.

Función str(): Convierte el número area a una cadena de texto para que pueda ser concatenado.

Propósito: Esta línea muestra el resultado del cálculo del área en la consola, proporcionando un mensaje claro y personalizado.
