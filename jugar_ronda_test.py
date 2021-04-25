import io
import sys
from unittest import TestCase, mock

from escrabol import jugar_ronda, iniciar


class JugarRondaTest(TestCase):

    @mock.patch('escrabol.input', create=True)
    def test_jugar_ronda(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["jar", "f*x", "!!"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        letras_en_mano = {"a": 1, "j": 1, "e": 1, "*": 1, "f": 1, "r": 1, "x": 1}
        palabras = ["jar", "fix"]
        puntaje_final = jugar_ronda(letras_en_mano, palabras)
        self.assertEqual(306, puntaje_final)

        with open("test_files/jugar_ronda.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())

    @mock.patch('escrabol.input', create=True)
    def test_jugar_ronda_sin_letras(self, input_mock):
        input_mock.side_effect = ["fix", "ac", "*t"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        letras_en_mano = {"a": 1, "c": 1, "f": 1, "i": 1, "*": 1, "t": 1, "x": 1}
        palabras = ["jar", "fix", "it"]
        puntaje_final = jugar_ronda(letras_en_mano, palabras)
        self.assertEqual(131, puntaje_final)

        with open("test_files/jugar_ronda_sin_letras.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())

    @mock.patch('escrabol.input', create=True)
    @mock.patch('escrabol.repartir_letras', create=True)
    @mock.patch('escrabol.reemplazar_letra', create=True)
    def test_jugar_dos_rondas(self, reemplazar_letra_mock, repartir_letras_mock, input_mock):
        input_mock.side_effect = ["2", "no", "part", "ic*", "no", "si", "l", "out", "!!",
                                  "si", "d*d", "out", "!!"]
        repartir_letras_mock.side_effect = [{"a": 1, "c": 1, "i": 1, "p": 1, "*": 1, "t": 1, "r": 1},
                                            {"d": 2, "l": 1, "o": 1, "u": 1, "*": 1, "t": 1}]
        reemplazar_letra_mock.side_effect = [{"d": 2, "h": 1, "o": 1, "u": 1, "*": 1, "t": 1}]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        palabras = ["jar", "fix", "it", "part", "ice", "out", "dad"]
        puntaje_final = iniciar(palabras)
        self.assertEqual(288, puntaje_final)

        with open("test_files/jugar_dos_rondas.txt", "r") as archivo_salida:
            resultado_esperado = archivo_salida.readlines()

        resultad_actual = resultado_test.getvalue().strip().split('\n')
        self.assertEqual(len(resultado_esperado), len(resultad_actual))

        for linea_esperada, linea_actual in zip(resultado_esperado, resultad_actual):
            self.assertEqual(linea_esperada.strip(), linea_actual.strip())
