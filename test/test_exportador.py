import unittest
from unittest.mock import patch, mock_open
import os
import sys

# --- SOLUCIÓN AL MODULENOTFOUNDERROR ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Importación corregida
from src.exportador import guardar_informe

class TestExportador(unittest.TestCase):

    def setUp(self):
        """Datos de ejemplo que coinciden con la estructura plana de exportador.py"""
        self.resultados_mock = {
            "total_palabras": 10,
            "total_caracteres": 50,
            "palabra_mas_larga": "computadora"
        }
        self.fuente = "Texto de prueba"

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.makedirs') # Simulamos la creación de carpetas para no crear directorios reales
    def test_guardar_informe_escritura(self, mock_mkdir, mock_file):
        """Verifica que se escriban los datos correctamente en el formato de exportador.py"""
        
        ruta_generada = guardar_informe(self.resultados_mock, self.fuente)

        # 1. Verificar que se intentó abrir un archivo en la carpeta 'informes'
        # Usamos call_args para verificar que el primer argumento contenga 'informes'
        args, kwargs = mock_file.call_args
        self.assertIn("informes", args[0])
        self.assertEqual(args[1], "w")
        self.assertEqual(kwargs['encoding'], "utf-8")

        # 2. Obtener todo lo que se escribió en el archivo
        manejador = mock_file()
        contenido_escrito = "".join(call.args[0] for call in manejador.write.call_args_list)

        # 3. Comprobar que los datos clave están en el texto generado según el formato real
        self.assertIn("INFORME DE ANÁLISIS DE TEXTO", contenido_escrito)
        self.assertIn(f"📂 Fuente: {self.fuente}", contenido_escrito)
        # La función transforma 'total_palabras' en '🔹 Total palabras: 10'
        self.assertIn("🔹 Total palabras: 10", contenido_escrito)
        self.assertIn("🔹 Palabra mas larga: computadora", contenido_escrito)

    @patch('builtins.open', side_effect=PermissionError("Permiso denegado"))
    @patch('os.makedirs')
    def test_guardar_informe_error(self, mock_mkdir, mock_file):
        """Verifica que la función maneje errores de permisos sin detener el programa"""
        # Según exportador.py, si hay error devuelve None y no lanza excepción
        resultado = guardar_informe(self.resultados_mock, self.fuente)
        self.assertIsNone(resultado, "La función debería devolver None ante un error de escritura.")

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.makedirs')
    def test_guardar_informe_diccionario_vacio(self, mock_mkdir, mock_file):
        """Verifica que el informe se genere aunque el diccionario de datos esté vacío"""
        resultados_vacios = {}
        
        ruta = guardar_informe(resultados_vacios, "Test Vacío")
        
        self.assertIsNotNone(ruta)
        manejador = mock_file()
        contenido = "".join(call.args[0] for call in manejador.write.call_args_list)
        
        # Debe contener la cabecera básica pero no estadísticas
        self.assertIn("📂 Fuente: Test Vacío", contenido)
        self.assertNotIn("🔹", contenido) # No debe haber viñetas de estadísticas

if __name__ == '__main__':
    unittest.main()