import unittest
import sys
import os

# 1. Obtenemos la ruta absoluta de donde está ESTE archivo de test
directorio_test = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos un nivel para llegar a la raíz (Contador_Palabras)
ruta_raiz = os.path.join(directorio_test, '..')

# 3. La insertamos al principio del path
sys.path.insert(0, os.path.abspath(ruta_raiz))

# Ahora la importación debería funcionar sin problemas
from src.analizador import (
    analizar_conteo_basico, 
    analizar_estructuras, 
    obtener_frecuencia_palabras, 
    calcular_estadisticas_avanzadas
)

class TestAnalizador(unittest.TestCase):

    def setUp(self):
        """Texto de ejemplo para las pruebas."""
        self.texto_simple = "Hola mundo. Esto es una prueba! Funciona?"
        self.texto_vacio = "   "

    # --- Pruebas: analizar_conteo_basico ---
    def test_conteo_basico_exito(self):
        palabras, con_espacios, sin_espacios = analizar_conteo_basico("Hola mundo")
        self.assertEqual(palabras, 2)
        self.assertEqual(con_espacios, 10)
        self.assertEqual(sin_espacios, 9)

    def test_conteo_basico_vacio(self):
        self.assertEqual(analizar_conteo_basico(self.texto_vacio), (0, 0, 0))

    # --- Pruebas: analizar_estructuras ---
    def test_estructuras_exito(self):
        # 3 oraciones (. ! ?), 2 párrafos
        texto = "Primera oración.\nSegunda oración! Tercera?"
        oraciones, parrafos = analizar_estructuras(texto)
        self.assertEqual(oraciones, 3)
        self.assertEqual(parrafos, 2)

    def test_estructuras_vacio(self):
        self.assertEqual(analizar_estructuras(None), (0, 0))

    # --- Pruebas: obtener_frecuencia_palabras ---
    def test_frecuencia_filtrado_stopwords(self):
        # 'el' y 'la' son stopwords y deben ignorarse
        texto = "el perro corre la calle el perro"
        resultado = obtener_frecuencia_palabras(texto)
        # Debería quedar: [('perro', 2), ('corre', 1), ('calle', 1)]
        self.assertEqual(resultado[0], ('perro', 2))
        self.assertNotIn('el', [palabra for palabra, cuenta in resultado])

    # --- Pruebas: calcular_estadisticas_avanzadas ---
    def test_estadisticas_avanzadas_exito(self):
        texto = "Python es genial"
        stats = calcular_estadisticas_avanzadas(texto)
        self.assertIsNotNone(stats)
        self.assertEqual(stats["unicas"], 3)
        self.assertEqual(stats["mas_larga"], "python")
        # (6+2+6) / 3 = 4.66...
        self.assertAlmostEqual(stats["media_longitud"], 4.67, places=2)

    def test_estadisticas_avanzadas_division_cero(self):
        """Verifica que la protección contra división por cero funcione."""
        # Un texto con solo símbolos no genera palabras en re.findall(r'\b\w+\b')
        texto_simbolos = "!!! ???"
        self.assertIsNone(calcular_estadisticas_avanzadas(texto_simbolos))

if __name__ == '__main__':
    unittest.main()