import unittest
import sys
import os

# 1. Configuramos la ruta hacia 'src'
# Tomamos la ubicación de este test, subimos un nivel y entramos a 'src'
directorio_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# 2. Insertamos 'src' en el path. 
# Esto permite que 'main.py' encuentre a 'lector_archivos.py' y 'exportador.py'
if directorio_src not in sys.path:
    sys.path.insert(0, directorio_src)

# 3. IMPORTACIÓN CORREGIDA: Importamos directamente desde 'main'
# Ya NO usamos 'from src.main', solo 'from main'
from main import realizar_analisis

class TestAnalizadorTexto(unittest.TestCase):

    def test_analisis_estandar(self):
        """Prueba un texto normal con varias palabras."""
        texto = "Hola mundo"
        resultado = realizar_analisis(texto)
        self.assertEqual(resultado["total_palabras"], 2)
        self.assertEqual(resultado["palabra_mas_larga"], "mundo")

    def test_texto_vacio(self):
        """Prueba el comportamiento con un string totalmente vacío."""
        resultado = realizar_analisis("")
        self.assertEqual(resultado["total_palabras"], 0)
        self.assertEqual(resultado["palabra_mas_larga"], "N/A")

    def test_solo_espacios(self):
        """Prueba un texto que solo contiene espacios y saltos de línea."""
        resultado = realizar_analisis("   \n   ")
        self.assertEqual(resultado["total_palabras"], 0)
        # Según tu main.py, len(texto) cuenta espacios físicos
        self.assertEqual(resultado["total_caracteres"], 7) 

    def test_limpieza_puntuacion(self):
        """Verifica que los signos de puntuación no afecten a la palabra más larga."""
        texto = "¡Hola! ¿Estás programando?"
        resultado = realizar_analisis(texto)
        # 'programando' (11) es más larga que 'Estás' (5 tras limpiar)
        self.assertEqual(resultado["palabra_mas_larga"], "programando")

    def test_multiples_espacios(self):
        """Verifica que múltiples espacios entre palabras no aumenten el conteo."""
        texto = "Palabra1    Palabra2"
        resultado = realizar_analisis(texto)
        self.assertEqual(resultado["total_palabras"], 2)

if __name__ == "__main__":
    unittest.main()