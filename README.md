# BIC01: Cuarto Laboratorio

En este laboratorio implementaremos el juego "Escrabol": una version simplificada del juego de palabras 
[Scrabble](https://es.wikipedia.org/wiki/Scrabble).

## Primera Parte

Complete la implementación de la función `calcular_puntaje_palabra(palabra, letras_disponibles)` en el archivo
`escrabol.py`. 
El puntaje de una palabra es la suma de dos partes: La primera parte es la suma de puntos por cada letra, definidos 
en el diccionario  `PUNTAJE_POR_LETRA`.
La segunda parte se define por la fórmula: `maximo(7 * longitud_palabra  - 3 * (letras_disponibles - letras_disponibles), 1) `. 
`longitud_palabra` es el número de letras de `palabra`, y `letras_disponibles` es el número de letras que el jugador 
tiene en mano.

## Segunda Parte

Complete la implementación de la función `actualizar_diccionario_letras(diccionario_letras, palabra)` en el archivo
`escrabol.py`.
Esta función recibe como parámetros el diccionario `diccionario_letras`, que representa las letras que el jugador 
actualmente tiene en mano, y la cadena de caracteres `palabra`, que representa la palabra que quiere formar.
La función debe retornar un **nuevo** diccionario, donde se represente que las letras de `palabra` hayan sido 
removidas de `diccionario_letras`.

```python
if __name__ == "__main__":
    diccionario_letras = {"p": 1, "e": 1, "r": 1, "u": 1, "a": 1, "n": 1, "o": 1}
    print(diccionario_letras)  # En pantalla: {'p': 1, 'e': 1, 'r': 1, 'u': 1, 'a': 1, 'n': 1, 'o': 1}
    mostrar_diccionario_letras(diccionario_letras)  # En pantalla: a e n o p r u

    nuevo_diccionario = actualizar_diccionario_letras(diccionario_letras, "pan")
    print(nuevo_diccionario)  # En pantalla: {'p': 0, 'e': 1, 'r': 1, 'u': 1, 'a': 0, 'n': 0, 'o': 1}
    mostrar_diccionario_letras(nuevo_diccionario)  # En pantalla: e o r u
    mostrar_diccionario_letras(diccionario_letras)  # En pantalla: a e n o p r u
```

La función `actualizar_diccionario_letras(diccionario_letras, palabra)` **no** verifica si es posible o no formar 
`palabra` con las letras en `diccionario_letras`.
Las letras que encuentra son siempre removidas de `diccionario_letras`, a modo de penalidad.

```python
if __name__ == "__main__":
    diccionario_letras = {"p": 1, "e": 1, "r": 1, "u": 1, "a": 1, "n": 1, "o": 1}
    mostrar_diccionario_letras(diccionario_letras)  # En pantalla: a e n o p r u

    nuevo_diccionario = actualizar_diccionario_letras(diccionario_letras, "peruvian")
    print(nuevo_diccionario)  # En pantalla: {'p': 0, 'e': 0, 'r': 0, 'u': 0, 'a': 0, 'n': 0, 'o': 1}
    mostrar_diccionario_letras(nuevo_diccionario)  # En pantalla: o

```

## Tercera Parte

Complete la implementación de la función `es_palabra_valida(palabra, diccionario_letras, lista_palabras)` en el archivo
`escrabol.py`.
En escrabol, una palabra se considera válida si está en la lista de palabras permitidas `lista_palabras` (sin considerar 
mayúsculas o minúsculas) y es posible formarla con las letras representadas en `diccionario_letras`.

## Cuarta Parte

Al iniciar una ronda, los usuarios reciben un comodín, representado por asterisco (*), entre las letras repartidas.
Los comodines pueden usarse para formar palabras, tomando el lugar de **cualquier vocal**.
Al usar un comodín al formar una palabra, el usuario no recibe puntos por letra en la función 
`calcular_puntaje_palabra(palabra, letras_disponibles)`.

En esta parte del laboratorio, se le solicita realice lo siguiente:

1. Modifique la función `repartir_letras(numero_letras)`, de modo que una de las tres vocales repartidas sea un comodín (*).

2. Modifique la función `es_palabra_valida(palabra, diccionario_letras, lista_palabras)`, de modo que acepte palabras que
   contengan un comodín. Considere que un comodín puede ser reemplazado por cualquier vocal.
   
```python
if __name__ == "__main__":
    random.seed(3)
    lista_palabras = ["tu", "pua", "tope"]
    diccionario_letras = repartir_letras(7)
    mostrar_diccionario_letras(diccionario_letras)  # En pantalla: * e g p t u w y.

    es_valida = es_palabra_valida("t*pe", diccionario_letras, lista_palabras)
    print(es_valida)  # En pantalla: True. "tope" esta en lista_palabras.

    es_valida = es_palabra_valida("w*y", diccionario_letras, lista_palabras)
    print(es_valida)  # En pantalla: False. No es posible formar una palabra valida.
```

## Quinta Parte

Una partida de escrabol consiste en multiples rondas. Complete la implementación de la función 
`jugar_ronda(diccionario_letras, lista_palabras)`, que permite jugar una de estas rondas. 
Considere lo siguiente:

1. Complete la implementación de la función `contar_letras_disponibles(diccionario_letras)`, que retorna el número total 
   de letras representadas en `diccionario_letras`. Necesitara de esta función para 
   implementar `jugar_ronda(diccionario_letras, lista_palabras)`.
   
2. El usuario puede terminar la ronda al ingresar el texto `!!`. La ronda también termina si el usuario se queda sin letras.

3. En caso la palabra ingresada por el usuario sea válida, de acuerdo a `es_palabra_valida(palabra_jugador, diccionario_letras, lista_palabras)`,
   se incrementa el puntaje de acuerdo a `calcular_puntaje_palabra(palabra_jugador, letras_disponibles)`.
   Caso contrario, se muestra un mensaje error.
   
4. Utilice `actualizar_diccionario_letras(diccionario_letras, palabra_jugador)`, para reflejar las letras utilizadas por cada
   palabra ingresada por el usuario.
   
5. Al finalizar la ronda, mostrar en pantalla el puntaje acumulado.

Los mensajes en pantalla deben tener el siguiente formato:

```
Letras en mano: * e g p t u w y 
Ingrese una palabra, o "!!" para indicar que ha terminado: t*pe
La palabra "t*pe" tiene 80 puntos. Puntaje total: 80
Letras en mano: g u w y 
Ingrese una palabra, o "!!" para indicar que ha terminado: wey
No es una palabra valida. Por favor, ingrese otra palabra.
Letras en mano: g u 
Ingrese una palabra, o "!!" para indicar que ha terminado: !!
Puntaje total: 80
```

```
Letras en mano: * a d i p r t 
Ingrese una palabra, o "!!" para indicar que ha terminado: partid*
La palabra "partid*" tiene 441 puntos. Puntaje total: 441
No te quedan mas letras. Puntaje total: 441
```

## Sexta Parte

Finalmente, implemente partidas de escrabol de multiples rondas, mediante la función `iniciar(lista_palabras)`.
Considere lo siguiente:

1. El numero de rondas a jugar es ingresado por el usuario al inicio de la partida.

2. Complete la implementación de la función `reemplazar_letra(diccionario_letras, letra)`. 
   Esta función devuelve un **nuevo diccionario**, donde la clave `letra` en `diccionario_letras` ha sido reemplazada 
   por una nueva letra seleccionada aleatoriamente. Esta nueva letra **no** debe haber estado previamente en 
   `diccionario_letras`.
   
3. El numero de letras repartidas al usuario está determinado por la variable `LETRAS_INICIALES`.  Las letras a repartir 
   son generadas por la función `repartir_letras(numero_letras)`.
   
4. Durante la partida, los usuarios tienen **una oportunidad** para reemplazar una de las letras repartidas,
mediante la función `reemplazar_letra(diccionario_letras, letra)` implementada en la parte 1.
   
5. Cada ronda es iniciada mediante una invocación a la función `jugar_ronda(diccionario_letras, lista_palabras)`.
   
6. Durante la partida, los usuarios tiene **una oportunidad** para repetir una de las rondas recién jugadas.
El puntaje asignado es el maximo entre la ronda original y la repetición.
   
7. Al final de la partida, se muestra el puntaje acumulado en todas las rondas.
   
Los mensajes en pantalla deben tener el siguiente formato:

```
Ingrese el numero de rondas: 2
Letras en mano: * e g p t u w y 
Quieres reemplazar una letra? no
Letras en mano: * e g p t u w y 
Ingrese una palabra, o "!!" para indicar que ha terminado: t*pe
La palabra "t*pe" tiene 80 puntos. Puntaje total: 80
Letras en mano: g u w y 
Ingrese una palabra, o "!!" para indicar que ha terminado: !!
Puntaje total: 80
____________
Quieres repetir la ronda? no
Letras en mano: * a b l t u w y 
Quieres reemplazar una letra? si
Que letra quieres reemplazar? w
Letras en mano: * a b h l t u y 
Ingrese una palabra, o "!!" para indicar que ha terminado: b*ta
La palabra "b*ta" tiene 80 puntos. Puntaje total: 80
Letras en mano: h l u y 
Ingrese una palabra, o "!!" para indicar que ha terminado: !!
Puntaje total: 80
____________
Quieres repetir la ronda? si
Letras en mano: * a b h l t u y 
Ingrese una palabra, o "!!" para indicar que ha terminado: tuy*
La palabra "tuy*" tiene 96 puntos. Puntaje total: 96
Letras en mano: a b h l 
Ingrese una palabra, o "!!" para indicar que ha terminado: !!
Puntaje total: 96
Puntaje acumulado: 176
```

