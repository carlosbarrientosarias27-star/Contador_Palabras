import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Añade la carpeta raíz del proyecto al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.utilidades import limpiar_pantalla, guardar_resultados


class TestUtilidades(unittest.TestCase):

    @patch('os.system')
    def test_limpiar_pantalla_nt(self, mock_system):
        """Prueba que use 'cls' si el sistema es Windows (nt)."""
        with patch('os.name', 'nt'):
            limpiar_pantalla()
            mock_system.assert_called_once_with('cls')

    @patch('os.system')
    def test_limpiar_pantalla_posix(self, mock_system):
        """Prueba que use 'clear' en Linux/Mac (posix)."""
        with patch('os.name', 'posix'):
            limpiar_pantalla()
            mock_system.assert_called_once_with('clear')

    @patch('builtins.input', return_value='s')
    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_guardar_resultados_exito(self, mock_file, mock_exists, mock_makedirs, mock_input):
        """Simula el guardado de un informe sin crear archivos reales."""
        informe = "Contenido de prueba"
        fuente = "test_source.csv"
        
        guardar_resultados(informe, fuente)

        # 1. Verificamos que se llamó a write()
        handle = mock_file()
        handle.write.assert_called_once() 

        # 2. Obtenemos el argumento real que se le pasó a write()
        # call_args[0][0] es el primer argumento posicional de la primera llamada
        argumento_escrito = handle.write.call_args[0][0]

        # 3. Verificamos que el contenido esperado esté DENTRO de lo que se escribió
        self.assertIn(f"Fuente: {fuente}", argumento_escrito)
        self.assertIn(informe, argumento_escrito)
        self.assertIn("INFORME - ", argumento_escrito)

        # Verificamos que intentó crear la carpeta
        mock_makedirs.assert_called_once_with("info_analisis")

    @patch('builtins.input', return_value='n')
    @patch('os.path.exists')
    def test_guardar_resultados_cancelado(self, mock_exists, mock_input):
        """Verifica que si el usuario dice 'n', no se hace nada."""
        guardar_resultados("nada", "fuente")
        mock_exists.assert_not_called()

if __name__ == '__main__':
    unittest.main()