# Explicación Detallada del Programa 5
El código completo se ve así:

```print("Calcule el nivel de desempeño descrito con su calificación dada por el usuario, dada con la siguiente tabla")```

```calificaciones = int(input("Ingresa tu calificación para evaluar tu desempeño:"))```

```if calificaciones <= 60:```

```print("Insuficiente")```
   
```elif calificaciones >= 70 and calificaciones <= 79:```

```print("Suficiente")```
    
```elif calificaciones >= 80 and calificaciones <= 89:```

```print("Muy bien!")```
    
```elif calificaciones >= 90 and calificaciones <= 95:```

```print("Notable!")```
    
```else:```

```print("Excelente")```

```print("¡Gracias por usar mi sistema de evaluación!")```
#### Primera Línea de Código
```print("Calcule el nivel de desempeño descrito con su calificación dada por el usuario, dada con la siguiente tabla")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Calcule el nivel de desempeño descrito con su calificación dada por el usuario, dada con la siguiente tabla" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Calcule el nivel de desempeño descrito con su calificación dada por el usuario, dada con la siguiente tabla" en la consola, indicando al usuario el propósito del ejercicio.
#### Segunda Línea de Código
```calificaciones = int(input("Ingresa tu calificación para evaluar tu desempeño:"))```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "Ingresa tu calificación para evaluar tu desempeño:" es el mensaje que se muestra al usuario para solicitar su calificación.

Función int(): Convierte la entrada del usuario (que es una cadena de texto) en un número entero.

Variable calificaciones: La entrada convertida se guarda en la variable calificaciones.

Propósito: Esta línea solicita al usuario que ingrese su calificación y la convierte a un número entero.
#### Tercera Línea de Código
```if calificaciones <= 60:```

```print("Insuficiente")```

Estructura Condicional if: Evalúa si calificaciones es menor o igual a 60.

Operador <=: Compara si calificaciones es menor o igual a 60.

Función print(): Si la condición es verdadera, muestra el texto "Insuficiente" en la consola.

Propósito: Esta línea verifica si la calificación es menor o igual a 60 y muestra un mensaje correspondiente.
#### Cuarta Línea de Código
```elif calificaciones >= 70 and calificaciones <= 79:```

```print("Suficiente")```

Estructura Condicional elif: Evalúa si calificaciones es mayor o igual a 70 y menor o igual a 79.

Operadores >= y <=: Comparan si calificaciones es mayor o igual a 70 y menor o igual a 79.

Función print(): Si la condición es verdadera, muestra el texto "Suficiente" en la consola.

Propósito: Esta línea verifica si la calificación está entre 70 y 79 y muestra un mensaje correspondiente.
#### Quinta Línea de Código
```elif calificaciones >= 80 and calificaciones <= 89:```

```print("Muy bien!")```

Estructura Condicional elif: Evalúa si calificaciones es mayor o igual a 80 y menor o igual a 89.

Operadores >= y <=: Comparan si calificaciones es mayor o igual a 80 y menor o igual a 89.

Función print(): Si la condición es verdadera, muestra el texto "Muy bien!" en la consola.

Propósito: Esta línea verifica si la calificación está entre 80 y 89 y muestra un mensaje correspondiente.
#### Sexta Línea de Código
```elif calificaciones >= 90 and calificaciones <= 95:```

```print("Notable!")```

Estructura Condicional elif: Evalúa si calificaciones es mayor o igual a 90 y menor o igual a 95.

Operadores >= y <=: Comparan si calificaciones es mayor o igual a 90 y menor o igual a 95.

Función print(): Si la condición es verdadera, muestra el texto "Notable!" en la consola.

Propósito: Esta línea verifica si la calificación está entre 90 y 95 y muestra un mensaje correspondiente.
#### Séptima Línea de Código
```else:```

```print("Excelente")```

Estructura Condicional else: Se ejecuta si ninguna de las condiciones anteriores se cumplió.

Función print(): Muestra el texto "Excelente" en la consola.

Propósito: Esta línea muestra un mensaje indicando que la calificación es excelente si no se cumplen las condiciones anteriores.
#### Octava Línea de Código
```print("¡Gracias por usar mi sistema de evaluación!")```

Función print(): Muestra texto en la consola.

Cadena de Texto: "¡Gracias por usar mi sistema de evaluación!" es una cadena de caracteres.

Propósito: Esta línea muestra un mensaje de agradecimiento al usuario por usar el programa.
