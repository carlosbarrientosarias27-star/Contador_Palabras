import unittest
import os
import sys

# 1. Configuración de rutas para encontrar 'src'
directorio_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if directorio_src not in sys.path:
    sys.path.insert(0, directorio_src)

# 2. Importación de las funciones del módulo lector_archivos
from lector_archivos import leer_archivo, crear_archivo_ejemplo

class TestLectorArchivos(unittest.TestCase):

    def setUp(self):
        """Configuración de rutas de prueba"""
        self.ruta_test = "textos/test_unidad.txt"
        self.ruta_vacia = "textos/vacio.txt"
        self.ruta_no_txt = "textos/documento.pdf"
        
        # Asegurar que el directorio de pruebas existe
        os.makedirs("textos", exist_ok=True)

    def tearDown(self):
        """Limpieza de archivos creados durante las pruebas"""
        for ruta in [self.ruta_test, self.ruta_vacia, self.ruta_no_txt]:
            if os.path.exists(ruta):
                os.remove(ruta)

    def test_crear_archivo_exitoso(self):
        """Verifica que crear_archivo_ejemplo genere el archivo físico"""
        crear_archivo_ejemplo(self.ruta_test)
        self.assertTrue(os.path.exists(self.ruta_test))

    def test_leer_archivo_contenido_correcto(self):
        """Verifica que la lectura recupere el contenido esperado"""
        crear_archivo_ejemplo(self.ruta_test)
        contenido = leer_archivo(self.ruta_test)
        self.assertIn("Python facilita la manipulación de archivos", contenido)

    def test_error_archivo_no_existe(self):
        """Verifica que se lance FileNotFoundError si la ruta es falsa"""
        with self.assertRaises(FileNotFoundError):
            leer_archivo("ruta/inexistente.txt")

    def test_error_extension_incorrecta(self):
        """Verifica que se lance ValueError si no es un archivo .txt"""
        # Creamos un archivo con extensión distinta para la prueba
        with open(self.ruta_no_txt, 'w') as f:
            f.write("contenido")
        
        with self.assertRaises(ValueError):
            leer_archivo(self.ruta_no_txt)

    def test_error_archivo_vacio(self):
        """Verifica que se lance EOFError si el archivo no tiene texto"""
        with open(self.ruta_vacia, 'w') as f:
            f.write("   ") # Solo espacios
        
        with self.assertRaises(EOFError):
            leer_archivo(self.ruta_vacia)

if __name__ == "__main__":
    unittest.main()