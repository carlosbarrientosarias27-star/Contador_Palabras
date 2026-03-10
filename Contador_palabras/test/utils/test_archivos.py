import sys
import os
import unittest
import shutil
import tempfile

ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from utils.archivos import cargar_desde_archivo, guardar_informe

class TestGestionArchivos(unittest.TestCase):
    """Pruebas para los servicios de lectura y escritura de archivos en disco."""

    def setUp(self):
        """Crea un entorno de archivos temporal antes de cada prueba."""
        self.test_dir = tempfile.mkdtemp()
        self.archivo_prueba = os.path.join(self.test_dir, "test.txt")

    def tearDown(self):
        """Elimina el directorio temporal y la carpeta de reportes generada tras cada prueba."""
        shutil.rmtree(self.test_dir)
        if os.path.exists("reportes"):
            shutil.rmtree("reportes")

    def test_cargar_archivo_existente(self):
        """Valida que el contenido de un archivo existente se lea e interprete correctamente."""
        contenido_esperado = "Hola, esto es una prueba unitaria."
        with open(self.archivo_prueba, "w", encoding="utf-8") as f:
            f.write(contenido_esperado)
        
        resultado = cargar_desde_archivo(self.archivo_prueba)
        self.assertEqual(resultado, contenido_esperado)

    def test_cargar_archivo_inexistente(self):
        """Asegura que el sistema retorne None de forma controlada si el archivo no existe."""
        resultado = cargar_desde_archivo("ruta/falsa/archivo.txt")
        self.assertIsNone(resultado)

    def test_cargar_archivo_vacio(self):
        """Verifica que archivos compuestos solo por espacios en blanco sean tratados como nulos."""
        with open(self.archivo_prueba, "w", encoding="utf-8") as f:
            f.write("   \n  ")
        
        resultado = cargar_desde_archivo(self.archivo_prueba)
        self.assertIsNone(resultado)

    def test_guardar_informe_crea_archivo(self):
        """Valida la creación automática de la carpeta de reportes y la integridad del archivo guardado."""
        informe_dummy = "Contenido del informe"
        fuente_dummy = "datos.txt"
        
        guardar_informe(informe_dummy, fuente_dummy)
        
        self.assertTrue(os.path.exists("reportes"))
        archivos_en_reportes = os.listdir("reportes")
        self.assertGreater(len(archivos_en_reportes), 0)
        
        ruta_ultimo = os.path.join("reportes", archivos_en_reportes[0])
        with open(ruta_ultimo, "r", encoding="utf-8") as f:
            contenido = f.read()
            self.assertIn(informe_dummy, contenido)
            self.assertIn(fuente_dummy, contenido)

if __name__ == "__main__":
    unittest.main()