import unittest
from unittest.mock import patch, mock_open
import os
import sys

# --- SOLUCIÓN AL MODULENOTFOUNDERROR ---
# 1. Buscamos la carpeta 'test' donde está este archivo
current_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Subimos un nivel para llegar a 'Contador_Palabras'
project_root = os.path.abspath(os.path.join(current_dir, ".."))
# 3. Lo añadimos al principio de la lista de búsqueda de Python
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Ahora ya puedes importar usando 'src.exportador'
from src.exportador import guardar_informe

class TestExportador(unittest.TestCase):

    def setUp(self):
        """Datos de ejemplo que simulan la salida del analizador."""
        self.resultados_mock = {
            "basicos": (10, 50, 40),        # palabras, con_esp, sin_esp
            "estructuras": (2, 1),          # oraciones, párrafos
            "avanzadas": {
                "unicas": 8,
                "porcentaje_unicas": 80.0,
                "media_longitud": 4.5,
                "mas_larga": "computadora"
            },
            "frecuentes": [("hola", 2), ("mundo", 1)]
        }
        self.fuente = "Texto de prueba"

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.abspath')
    def test_guardar_informe_escritura(self, mock_abs, mock_file):
        """Verifica que se intente abrir el archivo correcto y escribir en él."""
        mock_abs.return_value = "/ruta/falsa/informe.txt"
        
        guardar_informe(self.resultados_mock, self.fuente)

        # 1. Verificar que se abrió 'informe.txt' para escribir ('w')
        mock_file.assert_called_once_with("informe.txt", "w", encoding="utf-8")

        # 2. Obtener todo lo que se escribió en el archivo
        # handle() es el simulador del archivo abierto
        manejador = mock_file()
        contenido_escrito = "".join(call.args[0] for call in manejador.write.call_args_list)

        # 3. Comprobar que los datos clave están en el texto generado
        self.assertIn("INFORME DE ANÁLISIS DE TEXTO", contenido_escrito)
        self.assertIn(f"Fuente del texto: {self.fuente}", contenido_escrito)
        self.assertIn("Palabras totales: 10", contenido_escrito)
        self.assertIn("Palabra más larga: computadora", contenido_escrito)
        self.assertIn("1. hola: 2 vez/veces", contenido_escrito)

    @patch('builtins.open', side_effect=PermissionError("Permiso denegado"))
    def test_guardar_informe_error(self, mock_file):
        """Verifica que el programa no explote si no hay permisos de escritura."""
        # Esto debería capturarse en el bloque try/except de tu función
        try:
            guardar_informe(self.resultados_mock, self.fuente)
            exito = True
        except Exception:
            exito = False
        
        self.assertTrue(exito, "La función debería manejar la excepción internamente y no relanzarla.")

    # --- AQUÍ ESTÁ EL TERCER TEST ---
    @patch('builtins.open', new_callable=mock_open)
    def test_guardar_informe_sin_datos_avanzados(self, mock_file):
        """Verifica que el informe se genere aunque falten estadísticas avanzadas."""
        resultados_reducidos = {
            "basicos": (5, 20, 15),
            "estructuras": (1, 1),
            "avanzadas": {}, # Diccionario vacío para probar el 'if avanzadas:'
            "frecuentes": []
        }
        
        guardar_informe(resultados_reducidos, "Test Vacío")
        
        manejador = mock_file()
        contenido = "".join(call.args[0] for call in manejador.write.call_args_list)
        
        # Debe contener lo básico
        self.assertIn("Palabras totales: 5", contenido)
        # NO debe contener la cabecera de avanzadas (según tu lógica en exportador.py)
        self.assertNotIn("ESTADÍSTICAS AVANZADAS:", contenido)

if __name__ == '__main__':
    unittest.main()