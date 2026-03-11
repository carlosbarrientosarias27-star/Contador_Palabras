import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Ajuste de ruta para encontrar la carpeta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.entrada import capturar_texto_manual, cargar_desde_archivo

class TestEntrada(unittest.TestCase):

    # --- Pruebas para capturar_texto_manual ---

    @patch('builtins.input', side_effect=["Hola", "Mundo", ""])
    def test_capturar_texto_manual_exito(self, mock_input):
        """Verifica que se capturen varias líneas hasta encontrar una vacía."""
        resultado = capturar_texto_manual()
        self.assertEqual(resultado, "Hola\nMundo")
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', return_value="")
    def test_capturar_texto_manual_vacio(self, mock_input):
        """Verifica que devuelva None si no se introduce texto."""
        resultado = capturar_texto_manual()
        self.assertIsNone(resultado)

    # --- Pruebas para cargar_desde_archivo ---

    @patch('os.path.exists', return_value=True)
    def test_cargar_desde_archivo_exito(self, mock_exists):
        """Simula la lectura de un archivo con contenido."""
        contenido_falso = "Texto del archivo"
        with patch("builtins.open", mock_open(read_data=contenido_falso)):
            resultado = cargar_desde_archivo("ruta/test.txt")
            self.assertEqual(resultado, contenido_falso)

    @patch('os.path.exists', return_value=False)
    def test_cargar_desde_archivo_no_existe(self, mock_exists):
        """Verifica el error si el archivo no existe."""
        resultado = cargar_desde_archivo("fantasma.txt")
        self.assertIsNone(resultado)

    @patch('os.path.exists', return_value=True)
    def test_cargar_desde_archivo_vacio(self, mock_exists):
        """Verifica el error si el archivo existe pero no tiene contenido."""
        with patch("builtins.open", mock_open(read_data="   ")):
            resultado = cargar_desde_archivo("vacio.txt")
            self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()