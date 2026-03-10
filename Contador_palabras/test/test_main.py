import unittest
import sys
import os

directorio_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if directorio_src not in sys.path:
    sys.path.insert(0, directorio_src)

from main import realizar_analisis

class TestAnalizadorTexto(unittest.TestCase):
    """Suite de pruebas de integración para el punto de entrada principal del programa."""

    def test_analisis_estandar(self):
        """Prueba la integración completa con un flujo de texto estándar."""
        texto = "Hola mundo"
        resultado = realizar_analisis(texto)
        self.assertEqual(resultado["total_palabras"], 2)
        self.assertEqual(resultado["palabra_mas_larga"], "mundo")

    def test_texto_vacio(self):
        """Valida que la función de análisis principal maneje strings vacíos sin errores."""
        resultado = realizar_analisis("")
        self.assertEqual(resultado["total_palabras"], 0)
        self.assertEqual(resultado["palabra_mas_larga"], "N/A")

    def test_solo_espacios(self):
        """Verifica que el sistema distinga correctamente entre palabras inexistentes y caracteres físicos (espacios)."""
        resultado = realizar_analisis("   \n   ")
        self.assertEqual(resultado["total_palabras"], 0)
        self.assertEqual(resultado["total_caracteres"], 7) 

    def test_limpieza_puntuacion(self):
        """Comprueba que los caracteres especiales no se cuenten como parte de la longitud de las palabras."""
        texto = "¡Hola! ¿Estás programando?"
        resultado = realizar_analisis(texto)
        self.assertEqual(resultado["palabra_mas_larga"], "programando")

    def test_multiples_espacios(self):
        """Asegura que el uso de espaciado irregular no altere el conteo real de palabras."""
        texto = "Palabra1    Palabra2"
        resultado = realizar_analisis(texto)
        self.assertEqual(resultado["total_palabras"], 2)

if __name__ == "__main__":
    unittest.main()