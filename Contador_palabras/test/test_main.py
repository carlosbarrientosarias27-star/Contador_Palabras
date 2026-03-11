import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Asegura que la raíz del proyecto (donde está main.py) se añada al path
# Si el test está en proyecto/test/test_main.py, subimos dos niveles
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

try:
    from main import main
except ImportError:
    # Intento alternativo si la estructura varía
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    from main import main

class TestMain(unittest.TestCase):

    @patch('main.limpiar_pantalla')
    @patch('main.input', side_effect=['3'])
    def test_main_salir_inmediato(self, mock_input, mock_limpiar):
        """Verifica que el programa termina correctamente al elegir la opción 3."""
        with patch('builtins.print') as mock_print:
            main()
            # Verifica que se imprimió el mensaje de salida
            mock_print.assert_any_call("Saliendo del programa...")
            # Verifica que el bucle se ejecutó al menos una vez
            self.assertEqual(mock_input.call_count, 1)

    @patch('main.capturar_texto_manual')
    @patch('main.analizar_texto')
    @patch('main.guardar_resultados')
    @patch('main.limpiar_pantalla')
    # Se añade '' para el input de "Presiona Enter para continuar..."
    @patch('main.input', side_effect=['1', '', '3']) 
    def test_flujo_entrada_manual(self, mock_input, mock_limpiar, mock_guardar, mock_analizar, mock_capturar):
        """Simula un flujo completo: entrada manual -> análisis -> guardado -> salir."""
        mock_capturar.return_value = "Texto de prueba"
        mock_analizar.return_value = "Informe generado"

        main()

        mock_capturar.assert_called_once()
        # Se verifica que input se llamó 3 veces: opción, continuar y salir
        self.assertEqual(mock_input.call_count, 3) 
        mock_guardar.assert_called_once_with("Informe generado", "Entrada manual")

    @patch('main.cargar_desde_archivo')
    @patch('main.analizar_texto')
    @patch('main.guardar_resultados')
    @patch('main.limpiar_pantalla')
    # Se añade '' para el input de "Presiona Enter para continuar..."
    @patch('main.input', side_effect=['2', 'test.txt', '', '3']) 
    def test_flujo_archivo(self, mock_input, mock_limpiar, mock_guardar, mock_analizar, mock_cargar):
        """Simula la carga de un archivo y el procesamiento."""
        mock_cargar.return_value = "Contenido del archivo"
        mock_analizar.return_value = "Informe"

        main()

        mock_cargar.assert_called_once_with('test.txt')
        self.assertEqual(mock_input.call_count, 4) # Opción, ruta, continuar y salir

if __name__ == '__main__':
    unittest.main()