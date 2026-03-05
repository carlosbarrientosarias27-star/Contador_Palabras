import unittest
from unittest.mock import patch
import os
import sys

# Configuración para que el test vea la carpeta 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importamos desde src.main
from src.main import procesar_analisis, menu_principal

class TestMain(unittest.TestCase):
    # ... (el resto de tus tests)

    # --- Test 1: Probar el flujo de procesar_analisis ---
    @patch('src.main.guardar_informe')
    @patch('builtins.input', return_value='n') # Simulamos que el usuario elige NO exportar
    @patch('builtins.print')
    def test_procesar_analisis_flujo_completo(self, mock_print, mock_input, mock_guardar):
        """Verifica que el análisis procese el texto y muestre resultados."""
        texto_prueba = "Hola mundo. Esto es una prueba."
        fuente = "Test Unitario"
        
        procesar_analisis(texto_prueba, fuente)
        
        # Verificamos que se imprimieron resultados (buscamos una palabra clave en los prints)
        llamadas_print = [call.args[0] for call in mock_print.call_args_list if len(call.args) > 0]
        texto_impreso = "".join(str(llamadas_print))
        
        self.assertIn("ANÁLISIS: Test Unitario", texto_impreso)
        self.assertIn("Palabras:", texto_impreso)
        # Verificamos que NO se llamó a guardar_informe porque respondimos 'n'
        mock_guardar.assert_not_called()

    # --- Test 2: Probar la opción de SALIR del menú ---
    @patch('src.main.input', side_effect=['3']) # Simulamos que el usuario presiona '3' (Salir)
    @patch('src.main.limpiar_pantalla')
    @patch('src.main.mostrar_bienvenida')
    def test_menu_principal_salir(self, mock_bienvenida, mock_limpiar, mock_input):
        """Verifica que la opción 3 cierra el bucle del menú."""
        # Si la función termina sin error, es que el 'break' funcionó
        with patch('builtins.print') as mock_print:
            menu_principal()
            mock_print.assert_any_call("Finalizando programa. ¡Gracias por usar el analizador!")

    # --- Test 3: Probar manejo de errores en procesar_analisis ---
    @patch('src.main.analizar_conteo_basico')
    @patch('builtins.print')
    def test_procesar_analisis_error_inesperado(self, mock_print, mock_analizador):
        """Verifica que el bloque except Exception capture fallos críticos."""
        # Simulamos que el analizador explota por un error interno
        mock_analizador.side_effect = Exception("Fallo catastrófico")
        
        procesar_analisis("texto", "fuente")
        
        # Verificamos que se imprimió el mensaje de error capturado
        llamadas_print = [call.args[0] for call in mock_print.call_args_list if len(call.args) > 0]
        self.assertTrue(any("[Error Inesperado]: Fallo catastrófico" in str(p) for p in llamadas_print))

if __name__ == '__main__':
    unittest.main()