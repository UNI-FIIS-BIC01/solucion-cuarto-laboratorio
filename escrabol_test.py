from escrabol import calcular_puntaje_palabra, actualizar_diccionario_letras, convertir_palabra_a_diccionario, es_palabra_valida


def test_puntaje_por_palabra():
    escenarios = {("", 7): 0, ("it", 7): 2, ("was", 7): 54, ("weed", 6): 176,
                  ("scored", 7): 351, ("WaYbILl", 7): 735, ("Outgnaw", 7): 539,
                  ("fork", 7): 209, ("FORK", 4): 308}
    for escenario in escenarios:
        puntaje_esperado = escenarios[escenario]
        palabra, letras_disponibles = escenario
        puntaje_actual = calcular_puntaje_palabra(palabra, letras_disponibles)

        mensaje = ("Palabra: " + palabra + " Numero letras: " + str(letras_disponibles) + " Puntaje esperado: " +
                   str(puntaje_esperado) + " Puntaje actual: " + str(puntaje_actual))
        assert puntaje_actual == puntaje_esperado, mensaje


def test_puntaje_por_palabra_comodin():
    escenarios = {("h*ney", 7): 290, ("c*ws", 6): 176, ("wa*ls", 7): 203}
    for escenario in escenarios:
        puntaje_esperado = escenarios[escenario]
        palabra, letras_disponibles = escenario
        puntaje_actual = calcular_puntaje_palabra(palabra, letras_disponibles)

        mensaje = ("Palabra: " + palabra + " Numero letras: " + str(letras_disponibles) + " Puntaje esperado: " +
                   str(puntaje_esperado) + " Puntaje actual: " + str(puntaje_actual))
        assert puntaje_actual == puntaje_esperado, mensaje


def test_formar_palabra_quail():
    diccionario_original = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    copia_diccionario_original = diccionario_original.copy()
    palabra = "quail"

    resultado = actualizar_diccionario_letras(copia_diccionario_original, palabra)
    diccionario_esperado_1 = {'l': 1, 'm': 1}
    diccionario_esperado_2 = {'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}

    mensaje_error = ("Usando el diccionario " + str(diccionario_original) + " y la palabra " + palabra + " se obtuvo " +
                     str(resultado) + ". Se esperada " + str(diccionario_esperado_1) + " o " + str(
                diccionario_esperado_2))
    assert resultado == diccionario_esperado_1 or resultado == diccionario_esperado_2, mensaje_error

    mensaje_error = "El diccionario original " + str(copia_diccionario_original) + " ha sido modificado " + str(
        diccionario_original)
    assert copia_diccionario_original == diccionario_original, mensaje_error


def test_formar_palabra_hello():
    diccionario_original = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    copia_diccionario_original = diccionario_original.copy()
    palabra = "HELLO"

    resultado = actualizar_diccionario_letras(copia_diccionario_original, palabra)
    diccionario_esperado_1 = {}
    diccionario_esperado_2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}

    mensaje_error = ("Usando el diccionario " + str(diccionario_original) + " y la palabra " + palabra + " se obtuvo " +
                     str(resultado) + ". Se esperada " + str(diccionario_esperado_1) + " o " + str(
                diccionario_esperado_2))
    assert resultado == diccionario_esperado_1 or resultado == diccionario_esperado_2, mensaje_error

    mensaje_error = "El diccionario original " + str(copia_diccionario_original) + " ha sido modificado " + str(
        diccionario_original)
    assert copia_diccionario_original == diccionario_original, mensaje_error


def test_palabra_valida_hello():
    palabra = "hello"
    listado_palabras = [palabra.lower()]

    diccionario_letras = convertir_palabra_a_diccionario(palabra)
    copia_diccionario_letras = diccionario_letras.copy()

    resultado = es_palabra_valida(palabra, copia_diccionario_letras, listado_palabras)
    assert resultado is True, ("Se esperaba True para la palabra " + palabra + " y el diccionario " +
                               str(copia_diccionario_letras))

    assert diccionario_letras == copia_diccionario_letras, (
            "El diccionario original " + str(copia_diccionario_letras) + " ha sido modificado " + str(
        diccionario_letras))

    assert palabra in listado_palabras, " La lista de palabras no debe modificarse"


def test_palabra_valida_rapture():
    palabra = "Rapture"
    listado_palabras = [palabra.lower()]

    diccionario_letras = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))


def test_palabra_valida_honey():
    palabra = "honey"
    listado_palabras = [palabra.lower()]

    diccionario_letras = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is True, ("Se esperaba True para la palabra " + palabra + " y el diccionario " +
                               str(diccionario_letras))

    diccionario_letras = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))


def test_palabra_valida_evil():
    palabra = "EVIL"
    listado_palabras = [palabra.lower()]

    diccionario_letras = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is True, ("Se esperaba True para la palabra " + palabra + " y el diccionario " +
                               str(diccionario_letras))

    palabra = "Even"
    listado_palabras.append(palabra.lower())

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))


def test_palabra_valida_comodin():
    palabra = "e*m"
    listado_palabras = ["honey", "cows", "wails"]

    diccionario_letras = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))


def test_palabra_valida_comodin_honey():
    palabra = "honey"
    listado_palabras = ["honey", "cows", "wails"]

    diccionario_letras = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))

    palabra = "h*ney"
    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is True, ("Se esperaba True para la palabra " + palabra + " y el diccionario " +
                               str(diccionario_letras))


def test_palabra_valida_comodin_cows():
    palabra = "c*wz"
    listado_palabras = ["honey", "cows", "wails"]

    diccionario_letras = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2}

    resultado = es_palabra_valida(palabra, diccionario_letras, listado_palabras)
    assert resultado is False, ("Se esperaba False para la palabra " + palabra + " y el diccionario " +
                                str(diccionario_letras))


if __name__ == "__main__":
    test_puntaje_por_palabra()
    test_puntaje_por_palabra_comodin()
    test_formar_palabra_quail()
    test_formar_palabra_hello()
    test_palabra_valida_hello()
    test_palabra_valida_rapture()
    test_palabra_valida_honey()
    test_palabra_valida_evil()
    test_palabra_valida_comodin()
    test_palabra_valida_comodin_honey()
    test_palabra_valida_comodin_cows()

    print("Todos los test han pasado :)")
