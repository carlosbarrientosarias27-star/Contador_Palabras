import sys
import os
import unittest
import shutil
import tempfile

# 1. Ajustar el path para que encuentre la carpeta 'utils'
# Sube dos niveles desde: proyecto/test/utils/test_archivos.py 
# Hasta la raíz: proyecto/
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

# 2. Ahora sí importamos desde utils
from utils.archivos import cargar_desde_archivo, guardar_informe


class TestGestionArchivos(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test: crea un directorio temporal."""
        self.test_dir = tempfile.mkdtemp()
        self.archivo_prueba = os.path.join(self.test_dir, "test.txt")

    def tearDown(self):
        """Se ejecuta después de cada test: limpia los archivos creados."""
        shutil.rmtree(self.test_dir)
        # También limpiamos la carpeta 'reportes' si el test la creó
        if os.path.exists("reportes"):
            shutil.rmtree("reportes")

    def test_cargar_archivo_existente(self):
        """Verifica que lee correctamente un archivo con contenido."""
        contenido_esperado = "Hola, esto es una prueba unitaria."
        with open(self.archivo_prueba, "w", encoding="utf-8") as f:
            f.write(contenido_esperado)
        
        resultado = cargar_desde_archivo(self.archivo_prueba)
        self.assertEqual(resultado, contenido_esperado)

    def test_cargar_archivo_inexistente(self):
        """Verifica que devuelve None si el archivo no existe (Commit 7)."""
        resultado = cargar_desde_archivo("ruta/falsa/archivo.txt")
        self.assertIsNone(resultado)

    def test_cargar_archivo_vacio(self):
        """Verifica que devuelve None si el archivo solo tiene espacios o está vacío."""
        with open(self.archivo_prueba, "w", encoding="utf-8") as f:
            f.write("   \n  ")
        
        resultado = cargar_desde_archivo(self.archivo_prueba)
        self.assertIsNone(resultado)

    def test_guardar_informe_crea_archivo(self):
        """Verifica que la carpeta 'reportes' y el archivo se crean correctamente."""
        informe_dummy = "Contenido del informe"
        fuente_dummy = "datos.txt"
        
        # Ejecutar función
        guardar_informe(informe_dummy, fuente_dummy)
        
        # Verificar que la carpeta existe
        self.assertTrue(os.path.exists("reportes"))
        
        # Verificar que hay al menos un archivo dentro
        archivos_en_reportes = os.listdir("reportes")
        self.assertGreater(len(archivos_en_reportes), 0)
        
        # Verificar contenido del último archivo creado
        ruta_ultimo = os.path.join("reportes", archivos_en_reportes[0])
        with open(ruta_ultimo, "r", encoding="utf-8") as f:
            contenido = f.read()
            self.assertIn(informe_dummy, contenido)
            self.assertIn(fuente_dummy, contenido)

if __name__ == "__main__":
    unittest.main()