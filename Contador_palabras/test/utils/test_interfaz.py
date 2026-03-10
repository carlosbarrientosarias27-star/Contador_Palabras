import sys
import os
import unittest
from unittest.mock import patch
import io

# Ajuste de ruta para encontrar la carpeta 'utils'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from utils.interfaz import formatear_informe, capturar_texto_manual

class TestInterfaz(unittest.TestCase):

    def test_formatear_informe_contenido(self):
        """Verifica que el informe contenga los datos clave del diccionario de stats."""
        stats_ejemplo = {
            "oraciones": 2, "parrafos": 1, "total": 10,
            "unicas": 8, "porcentaje_unicas": 80.0, "media": 5.2,
            "p_larga": "computadora", "top": [("hola", 2), ("mundo", 1)]
        }
        
        resultado = formatear_informe(stats_ejemplo)
        
        # Comprobamos que los datos importantes aparezcan en el string final
        self.assertIn("RESULTADOS DEL ANÁLISIS", resultado)
        self.assertIn("10", resultado) # total palabras
        self.assertIn("computadora", resultado) # palabra más larga
        self.assertIn("hola: 2 veces", resultado) # top 5

    @patch('builtins.input', side_effect=['Esta es una línea', 'Segunda línea', ''])
    def test_capturar_texto_manual_exito(self, mock_input):
        """Simula a un usuario escribiendo dos líneas y luego presionando Enter."""
        resultado = capturar_texto_manual()
        texto_esperado = "Esta es una línea\nSegunda línea"
        
        self.assertEqual(resultado, texto_esperado)

    @patch('builtins.input', side_effect=[''])
    def test_capturar_texto_manual_vacio(self, mock_input):
        """Simula a un usuario presionando Enter sin escribir nada."""
        resultado = capturar_texto_manual()
        self.assertIsNone(resultado)

    @patch('os.system')
    def test_limpiar_pantalla(self, mock_os):
        """Verifica que se llame al comando del sistema para limpiar la pantalla."""
        from utils.interfaz import limpiar_pantalla
        limpiar_pantalla()
        # Verifica que os.system fue llamado al menos una vez
        mock_os.assert_called()

if __name__ == "__main__":
    unittest.main()