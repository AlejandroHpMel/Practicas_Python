# Explicación Detallada del Programa 3
El código completo se ve así:

```print("Identificación de tipo de datos")```

```variable = input("Ingresa tu edad:")```

```print(type(variable))```

```variable = int(variable)```

```print(type(variable))```

```variable = float(variable)```

```print(type(variable))```
#### Primera Línea de Código
```print("Identificación de tipo de datos")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Identificación de tipo de datos" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Identificación de tipo de datos" en la consola, indicando al usuario el propósito del ejercicio.
#### Segunda Línea de Código
```variable = input("Ingresa tu edad:")```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "Ingresa tu edad:" es el mensaje que se muestra al usuario para solicitar su edad.

Variable variable: La entrada del usuario se guarda en la variable variable.

Propósito: Esta línea solicita al usuario que ingrese su edad y almacena esa información en la variable variable.
#### Tercera Línea de Código
```print(type(variable))```

Función print(): Muestra el tipo de dato de la variable variable en la consola.

Función type(): Devuelve el tipo de dato de la variable variable.

Propósito: Esta línea muestra el tipo de dato de la entrada del usuario, que será una cadena de texto (str), ya que la función input() siempre devuelve una cadena de texto.
#### Cuarta Línea de Código
```variable = int(variable)```

Función int(): Convierte la cadena de texto almacenada en variable a un número entero.

Variable variable: La entrada convertida se guarda nuevamente en la variable variable.

Propósito: Esta línea convierte la entrada del usuario de una cadena de texto a un número entero.
#### Quinta Línea de Código
```print(type(variable))```

Función print(): Muestra el tipo de dato de la variable variable en la consola.

Función type(): Devuelve el tipo de dato de la variable variable.

Propósito: Esta línea muestra el tipo de dato de la variable variable después de la conversión a un número entero, que será int.
#### Sexta Línea de Código
```variable = float(variable)```

Función float(): Convierte el número entero almacenado en variable a un número de punto flotante (decimal).

Variable variable: La entrada convertida se guarda nuevamente en la variable variable.

Propósito: Esta línea convierte la entrada del usuario de un número entero a un número de punto flotante.
#### Séptima Línea de Código
```print(type(variable))```

Función print(): Muestra el tipo de dato de la variable variable en la consola.

Función type(): Devuelve el tipo de dato de la variable variable.

Propósito: Esta línea muestra el tipo de dato de la variable variable después de la conversión a un número de punto flotante, que será float.
