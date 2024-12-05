# Explicación Detallada del Programa 9
El código completo se ve así:

```print("Igualdad en listas")```

```puntos = [10, 30, 20]```

```puntos_2 = [10, 30, 20]```

```ordenados = [10, 20, 30]```

```puntos_textos = ["10", "20", "30"]```

```print(puntos == puntos_2)  # True```

```print(puntos == ordenados)  # False```

```print(puntos == "puntos_textos")  # False```

```print("\n")```

```print(puntos != puntos_2)  # False```

```print(puntos != ordenados)  # True```

```print(puntos != puntos_textos)  # True```
#### Primera Línea de Código
```print("Igualdad en listas")```

Función print(): Esta función se utiliza para mostrar texto en la consola.

Cadena de Texto: "Igualdad en listas" es una cadena de caracteres que se muestra en la consola.

```Definición de Listas```

```puntos = [10, 30, 20]```

```puntos_2 = [10, 30, 20]```

```ordenados = [10, 20, 30]```

```puntos_textos = ["10", "20", "30"]```

Listas: Se definen cuatro listas con diferentes elementos.

puntos y puntos_2 contienen los mismos elementos en el mismo orden.

ordenados contiene los mismos elementos que puntos pero en un orden diferente.

puntos_textos contiene los mismos números que puntos pero como cadenas de texto.
#### Comparaciones de Igualdad
```print(puntos == puntos_2)  # True```

```print(puntos == ordenados)  # False```

```print(puntos == "puntos_textos")  # False```

```Comparación ==:```

puntos == puntos_2 devuelve True porque ambas listas tienen los mismos elementos en el mismo orden.

puntos == ordenados devuelve False porque, aunque tienen los mismos elementos, el orden es diferente.

puntos == "puntos_textos" devuelve False porque puntos es una lista de enteros y "puntos_textos" es una cadena de texto, no una lista.

```Salto de Línea```

```print("\n")```

Función print(): Muestra un salto de línea en la consola.
#### Comparaciones de Desigualdad
```print(puntos != puntos_2)  # False```

```print(puntos != ordenados)  # True```

```print(puntos != puntos_textos)  # True```

```Comparación !=:```

puntos != puntos_2 devuelve False porque ambas listas son iguales.

puntos != ordenados devuelve True porque las listas no son iguales debido al orden de los elementos.

puntos != puntos_textos devuelve True porque puntos es una lista de enteros y puntos_textos es una lista de cadenas de texto.
