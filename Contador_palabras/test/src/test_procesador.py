import unittest
import sys
import os

# Ajuste de ruta para encontrar la carpeta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.procesador import analizar_texto

class TestProcesador(unittest.TestCase):

    def setUp(self):
        """Configuración de un texto de prueba estándar."""
        self.texto_simple = "Hola mundo. Esto es una prueba! ¿Verdad? Hola de nuevo.\n\nSegundo párrafo."

    def test_conteo_basico(self):
        """Verifica el conteo de palabras y caracteres."""
        resultado = analizar_texto("Hola mundo")
        # "Hola mundo" tiene 10 caracteres con espacio y 9 sin espacio
        self.assertIn("Palabras totales: 2", resultado)
        self.assertIn("Caracteres (con espacios): 10", resultado)
        self.assertIn("Caracteres (sin espacios): 9", resultado)

    def test_oraciones_y_parrafos(self):
        """Verifica la detección de delimitadores (. ! ?) y saltos de línea."""
        resultado = analizar_texto(self.texto_simple)
        # Oraciones: "Hola mundo", "Esto es una prueba", "¿Verdad", "Hola de nuevo", "Segundo párrafo"
        self.assertIn("5 oraciones", resultado)
        self.assertIn("2 párrafos", resultado)

    def test_filtrado_stop_words(self):
        """Verifica que palabras como 'el', 'la', 'de' sean ignoradas en el TOP 5."""
        texto = "la casa de papel y el papel de la casa"
        # Palabras: casa (2), papel (2). 'la', 'de', 'y', 'el' son stop_words.
        resultado = analizar_texto(texto)
        self.assertIn("1. casa: 2 veces", resultado)
        self.assertIn("2. papel: 2 veces", resultado)
        # Aseguramos que 'la' no esté en el top (aunque sea frecuente)
        self.assertNotIn("1. la:", resultado)

    def test_estadisticas_avanzadas(self):
        """Verifica palabra más larga, corta y longitud media."""
        resultado = analizar_texto("Sol mar estrella")
        # estrella (8), sol/mar (3). Media: (3+3+8)/3 = 4.66... -> 4.7
        self.assertIn("Longitud media de palabra: 4.7 letras", resultado)
        self.assertIn("Palabra más larga: estrella", resultado)
        self.assertIn("Palabra más corta: sol", resultado) # 'sol' va antes que 'mar' por orden de aparición

    def test_texto_vacio(self):
        """Verifica que el código no rompa con un string vacío."""
        resultado = analizar_texto("")
        self.assertIn("Palabras totales: 0", resultado)
        self.assertIn("Longitud media de palabra: 0.0 letras", resultado)
        self.assertIn("Palabra más larga: -", resultado)
        # Añadimos la comprobación del porcentaje para asegurar que la corrección funciona
        self.assertIn("(0.0% del total)", resultado)

if __name__ == '__main__':
    unittest.main()