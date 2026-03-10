import sys
import os
import unittest
from unittest.mock import patch
import io

ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from utils.interfaz import formatear_informe, capturar_texto_manual

class TestInterfaz(unittest.TestCase):
    """Suite de pruebas para los componentes de interacción con el usuario (CLI)."""

    def test_formatear_informe_contenido(self):
        """Verifica que el string generado para el informe contenga los indicadores clave calculados."""
        stats_ejemplo = {
            "oraciones": 2, "parrafos": 1, "total": 10,
            "unicas": 8, "porcentaje_unicas": 80.0, "media": 5.2,
            "p_larga": "computadora", "top": [("hola", 2), ("mundo", 1)]
        }
        
        resultado = formatear_informe(stats_ejemplo)
        
        self.assertIn("RESULTADOS DEL ANÁLISIS", resultado)
        self.assertIn("10", resultado) 
        self.assertIn("computadora", resultado) 
        self.assertIn("hola: 2 veces", resultado) 

    @patch('builtins.input', side_effect=['Esta es una línea', 'Segunda línea', ''])
    def test_capturar_texto_manual_exito(self, mock_input):
        """Simula la entrada multilínea de un usuario y valida la reconstrucción del texto."""
        resultado = capturar_texto_manual()
        texto_esperado = "Esta es una línea\nSegunda línea"
        
        self.assertEqual(resultado, texto_esperado)

    @patch('builtins.input', side_effect=[''])
    def test_capturar_texto_manual_vacio(self, mock_input):
        """Asegura que presionar Enter sin contenido devuelva None."""
        resultado = capturar_texto_manual()
        self.assertIsNone(resultado)

    @patch('os.system')
    def test_limpiar_pantalla(self, mock_os):
        """Verifica que se invoque el comando del sistema operativo para limpiar la terminal."""
        from utils.interfaz import limpiar_pantalla
        limpiar_pantalla()
        mock_os.assert_called()

if __name__ == "__main__":
    unittest.main()