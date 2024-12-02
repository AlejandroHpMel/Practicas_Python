# Explicación Detallada del Programa 7
El código completo se ve así:

```print("Calcula el área y el perímetro de un círculo ingresando el valor del radio por el usuario")```

```radio = float(input("Ingresa el valor del radio: "))```

```area = 3.1416 * radio ** 2```

```perimetro = 3.1416 * 2 * radio```

```print("El área del círculo es: " + str(area))```

```print("El perímetro del círculo es: " + str(perimetro))```
#### Primera Línea de Código
```print("Calcula el área y el perímetro de un círculo ingresando el valor del radio por el usuario")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Calcula el área y el perímetro de un círculo ingresando el valor del radio por el usuario" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Calcula el área y el perímetro de un círculo ingresando el valor del radio por el usuario" en la consola, indicando al usuario el propósito del ejercicio.
#### Segunda Línea de Código
```radio = float(input("Ingresa el valor del radio: "))```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "Ingresa el valor del radio: " es el mensaje que se muestra al usuario para solicitar el valor del radio.

Función float(): Convierte la entrada del usuario (que es una cadena de texto) en un número de punto flotante (decimal).

Variable radio: La entrada convertida se guarda en la variable radio.

Propósito: Esta línea solicita al usuario que ingrese el valor del radio del círculo y lo convierte a un número decimal.
#### Tercera Línea de Código
```area = 3.1416 * radio ** 2```

Operación Aritmética: 3.1416 * radio ** 2 calcula el área del círculo utilizando la fórmula del área: (\text{Área} = \pi \times \text{radio}^2).

Constante 3.1416: Aproximación del valor de (\pi).

Operador **: Este operador se utiliza para elevar el radio al cuadrado.

Variable area: El resultado del cálculo se guarda en la variable area.

Propósito: Esta línea realiza el cálculo del área del círculo utilizando el valor del radio proporcionado por el usuario.
#### Cuarta Línea de Código
```perimetro = 3.1416 * 2 * radio```

Operación Aritmética: 3.1416 * 2 * radio calcula el perímetro del círculo utilizando la fórmula del perímetro: (\text{Perímetro} = 2 \pi \times \text{radio}).

Constante 3.1416: Aproximación del valor de (\pi).

Variable perimetro: El resultado del cálculo se guarda en la variable perimetro.

Propósito: Esta línea realiza el cálculo del perímetro del círculo utilizando el valor del radio proporcionado por el usuario.
#### Quinta Línea de Código
```print("El área del círculo es: " + str(area))```

Función print(): Muestra texto en la consola.

Concatenación de Cadenas: "El área del círculo es: " + str(area) combina (concatena) la cadena de texto con el valor de area.

Función str(): Convierte el número area a una cadena de texto para que pueda ser concatenado.

Propósito: Esta línea muestra el resultado del cálculo del área en la consola, proporcionando un mensaje claro y personalizado.
#### Sexta Línea de Código
```print("El perímetro del círculo es: " + str(perimetro))```

Función print(): Muestra texto en la consola.

Concatenación de Cadenas: "El perímetro del círculo es: " + str(perimetro) combina (concatena) la cadena de texto con el valor de perimetro.

Función str(): Convierte el número perimetro a una cadena de texto para que pueda ser concatenado.

Propósito: Esta línea muestra el resultado del cálculo del perímetro en la consola, proporcionando un mensaje claro y personalizado.
