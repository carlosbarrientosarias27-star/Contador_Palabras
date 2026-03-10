import sys
import os
import unittest 

# Añade la carpeta raíz del proyecto al path de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core.analizador import analizar_texto

class TestAnalizadorTexto(unittest.TestCase):

    def test_texto_estandar(self):
        """Prueba un texto normal con oraciones y párrafos."""
        texto = "Hola mundo. Esto es una prueba.\n\nSegundo párrafo aquí."
        resultado = analizar_texto(texto)
        self.assertEqual(resultado["oraciones"], 3)
        self.assertEqual(resultado["parrafos"], 2)
        self.assertEqual(len(resultado["p_larga"]), 7)

    def test_texto_vacio(self):
        """Verifica que el sistema no explote con strings vacíos."""
        resultado = analizar_texto("")
        self.assertEqual(resultado["total"], 0)
        self.assertEqual(resultado["oraciones"], 0)
        self.assertEqual(resultado["p_larga"], "-")

    def test_solo_numeros(self):
        """Verifica el manejo de texto que no contiene palabras (solo dígitos)."""
        resultado = analizar_texto("123 456 789")
        self.assertEqual(resultado["unicas"], 0)
        self.assertEqual(resultado["p_larga"], "-")

    def test_stop_words_filtro(self):
        """Asegura que las stop_words no aparezcan en el top 5."""
        texto = "el sol la luna el sol el sol"
        resultado = analizar_texto(texto)
        palabras_en_top = [word for word, count in resultado["top"]]
        self.assertNotIn("el", palabras_en_top)
        self.assertIn("sol", palabras_en_top)

    def test_porcentaje_unicas(self):
        """Valida el cálculo matemático de palabras únicas."""
        texto = "hola hola adiós"
        resultado = analizar_texto(texto)
        self.assertAlmostEqual(resultado["porcentaje_unicas"], 66.6666666, places=2)

if __name__ == '__main__':
    unittest.main()