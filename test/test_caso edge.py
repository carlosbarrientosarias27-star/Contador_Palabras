import unittest
import sys
import os

# Configuración de ruta para que el test encuentre la carpeta 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.analizador import (
    analizar_conteo_basico, 
    analizar_estructuras, 
    obtener_frecuencia_palabras, 
    calcular_estadisticas_avanzadas
)

class TestAnalizador(unittest.TestCase):

    # --- TUS TESTS ANTERIORES (Ejemplo) ---
    def test_conteo_basico_exito(self):
        palabras, con_esp, sin_esp = analizar_conteo_basico("Hola mundo")
        self.assertEqual(palabras, 2)

    # --- NUEVOS CASOS BORDE (Añádelos aquí) ---

    def test_caso_vacio(self):
        """Prueba con texto vacío o solo espacios."""
        texto = "   "
        self.assertEqual(analizar_conteo_basico(texto), (0, 0, 0))
        self.assertEqual(analizar_estructuras(texto), (0, 0))
        self.assertIsNone(calcular_estadisticas_avanzadas(texto))

    def test_un_solo_caracter(self):
        """Prueba con un solo carácter."""
        texto = "A"
        palabras, _, sin_esp = analizar_conteo_basico(texto)
        self.assertEqual(palabras, 1)
        self.assertEqual(sin_esp, 1)

    def test_solo_numeros(self):
        """Prueba con solo números."""
        texto = "12345"
        # El conteo básico lo trata como una palabra separada por espacios
        res = analizar_conteo_basico(texto)
        self.assertEqual(res[0], 1)
        
        # Las estadísticas avanzadas usan regex que detecta números como palabras
        stats = calcular_estadisticas_avanzadas(texto)
        self.assertIsNotNone(stats)
        self.assertEqual(stats["unicas"], 1)

if __name__ == '__main__':
    unittest.main()
