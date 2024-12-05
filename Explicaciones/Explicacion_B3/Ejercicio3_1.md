# Explicación Detallada del Programa 1
El código completo se ve así:

```print("Elife")```

```nombre = input("Ingresa el tipo de mascota que tienes:  ")```

```if "perro" in nombre:```

``` print("Es un perro")```
   
```elif "gato" in nombre:```
   
```print("Es un gato")```
    
```else:```

   ``` print("Mascota desconocida")```
#### Primera Línea de Código
```print("Elife")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Elife" es una cadena de caracteres. Las cadenas de texto en Python se encierran entre comillas dobles (") o simples (').

Propósito: Esta línea muestra el texto "Elife" en la consola. Parece que hay un error tipográfico y debería ser "Elif" para indicar el uso de la estructura condicional elif.
#### Segunda Línea de Código
```nombre = input("Ingresa el tipo de mascota que tienes:  ")```

Función input(): Esta función se utiliza para recibir entrada del usuario. Muestra un mensaje en la consola y espera a que el usuario escriba algo y presione Enter.

Cadena de Texto: "Ingresa el tipo de mascota que tienes: " es el mensaje que se muestra al usuario para solicitar el tipo de mascota.

Variable nombre: La entrada del usuario se guarda en la variable nombre.

Propósito: Esta línea solicita al usuario que ingrese el tipo de mascota que tiene y almacena esa información en la variable nombre.
#### Tercera Línea de Código
```if "perro" in nombre:```
    
```print("Es un perro")```

Estructura Condicional if: Evalúa si la cadena "perro" está contenida en la variable nombre.

Operador in: Verifica si una subcadena está presente dentro de otra cadena.

Función print(): Si la condición es verdadera, muestra el texto "Es un perro" en la consola.

Propósito: Esta línea verifica si el usuario ingresó "perro" como parte del tipo de mascota y, si es así, muestra un mensaje indicando que es un perro.
#### Cuarta Línea de Código
```elif "gato" in nombre:```
    
```print("Es un gato")```
    
Estructura Condicional elif: Evalúa si la cadena "gato" está contenida en la variable nombre, si la condición anterior no se cumplió.
Operador in: Verifica si una subcadena está presente dentro de otra cadena.

Función print(): Si la condición es verdadera, muestra el texto "Es un gato" en la consola.

Propósito: Esta línea verifica si el usuario ingresó "gato" como parte del tipo de mascota y, si es así, muestra un mensaje indicando que es un gato.
#### Quinta Línea de Código
```else:```

```print("Mascota desconocida")```
Estructura Condicional else: Se ejecuta si ninguna de las condiciones anteriores se cumplió.

Función print(): Muestra el texto "Mascota desconocida" en la consola.

Propósito: Esta línea muestra un mensaje indicando que la mascota es desconocida si el usuario no ingresó "perro" ni "gato".
