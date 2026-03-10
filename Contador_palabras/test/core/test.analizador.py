import sys
import os
import unittest 

# Añade la carpeta raíz del proyecto al path de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.analizador import analizar_texto

class TestAnalizadorTexto(unittest.TestCase):

    def test_texto_estandar(self):
        """Verifica el conteo correcto de oraciones, párrafos y longitud de palabras en un texto normal."""
        texto = "Hola mundo. Esto es una prueba.\n\nSegundo párrafo aquí."
        resultado = analizar_texto(texto)
        self.assertEqual(resultado["oraciones"], 3)
        self.assertEqual(resultado["parrafos"], 2)
        self.assertEqual(len(resultado["p_larga"]), 7)

    def test_texto_vacio(self):
        """Asegura que el analizador retorne valores iniciales seguros ante un string vacío."""
        resultado = analizar_texto("")
        self.assertEqual(resultado["total"], 0)
        self.assertEqual(resultado["oraciones"], 0)
        self.assertEqual(resultado["p_larga"], "-")

    def test_solo_numeros(self):
        """Valida que los números puros no se contabilicen como palabras únicas o alfabéticas."""
        resultado = analizar_texto("123 456 789")
        self.assertEqual(resultado["unicas"], 0)
        self.assertEqual(resultado["p_larga"], "-")

    def test_stop_words_filtro(self):
        """Verifica que las palabras funcionales (stop words) se excluyan del ranking de las más frecuentes."""
        texto = "el sol la luna el sol el sol"
        resultado = analizar_texto(texto)
        palabras_en_top = [word for word, count in resultado["top"]]
        self.assertNotIn("el", palabras_en_top)
        self.assertIn("sol", palabras_en_top)

    def test_porcentaje_unicas(self):
        """Comprueba que el cálculo del porcentaje de palabras únicas sobre el total sea matemáticamente preciso."""
        texto = "hola hola adiós"
        resultado = analizar_texto(texto)
        self.assertAlmostEqual(resultado["porcentaje_unicas"], 66.6666666, places=2)

if __name__ == '__main__':
    unittest.main()