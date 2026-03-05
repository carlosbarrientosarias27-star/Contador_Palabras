import unittest
from unittest.mock import patch, mock_open
import os
import sys

# Esto calcula la ruta de la raíz del proyecto (un nivel arriba de /test)
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ruta_raiz)

# Ahora ya puedes importar desde src
from src.lector import leer_terminal, leer_archivo
class TestLector(unittest.TestCase):

    # --- Pruebas para leer_terminal ---

    @patch('builtins.input', side_effect=['Hola', 'Mundo', ''])
    def test_leer_terminal_exito(self, mock_input):
        """Prueba que se lea correctamente el texto multilínea."""
        resultado = leer_terminal()
        self.assertEqual(resultado, "Hola\nMundo")

    @patch('builtins.input', side_effect=[''])
    def test_leer_terminal_vacio(self, mock_input):
        """Prueba que devuelva None si no se introduce texto."""
        resultado = leer_terminal()
        self.assertIsNone(resultado)

    # --- Pruebas para leer_archivo ---

    @patch('os.path.exists')
    def test_leer_archivo_no_existe(self, mock_exists):
        """Prueba el error cuando el archivo no existe."""
        mock_exists.return_value = False
        resultado = leer_archivo("ruta/falsa.txt")
        self.assertIsNone(resultado)

    @patch('os.path.exists')
    def test_leer_archivo_vacio(self, mock_exists):
        """Prueba el error cuando el archivo existe pero está vacío."""
        mock_exists.return_value = True
        # Simulamos un archivo abierto que devuelve un string vacío
        with patch('builtins.open', mock_open(read_data="   ")):
            resultado = leer_archivo("vacio.txt")
            self.assertIsNone(resultado)

    @patch('os.path.exists')
    def test_leer_archivo_exito(self, mock_exists):
        """Prueba la lectura exitosa de un archivo."""
        mock_exists.return_value = True
        contenido_simulado = "Línea 1\nLínea 2"
        with patch('builtins.open', mock_open(read_data=contenido_simulado)):
            resultado = leer_archivo("archivo.txt")
            self.assertEqual(resultado, contenido_simulado)

if __name__ == '__main__':
    unittest.main()