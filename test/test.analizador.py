import unittest
import sys
import os

# 1. Configuración de rutas para encontrar 'src'
directorio_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
if directorio_src not in sys.path:
    sys.path.insert(0, directorio_src)

# 2. Importación de las funciones del analizador
from analizador import (
    limpiar_palabras, 
    contar_estadisticas_basicas, 
    analizar_estructura, 
    analizar_vocabulario
)

class TestAnalizadorTexto(unittest.TestCase):

    def setUp(self):
        """Configuración de datos de prueba comunes"""
        self.texto_simple = "Hola mundo. Esto es una prueba!"
        self.palabras_simple = ["hola", "mundo", "esto", "es", "una", "prueba"]

    def test_limpiar_palabras(self):
        """Verifica que se elimine puntuación y se pase a minúsculas"""
        texto = "¡Hola, MUNDO! ¿Python?"
        resultado = limpiar_palabras(texto)
        self.assertEqual(resultado, ["hola", "mundo", "python"])

    def test_contar_estadisticas_basicas(self):
        """Verifica el conteo de palabras y caracteres"""
        # "hola mundo" -> 10 char con espacio, 9 sin espacio, 2 palabras
        total_p, c_con, c_sin, l_med = contar_estadisticas_basicas("hola mundo", ["hola", "mundo"])
        self.assertEqual(total_p, 2)
        self.assertEqual(c_con, 10)
        self.assertEqual(c_sin, 9)
        self.assertEqual(l_med, 4.5) # (4+5)/2

    def test_analizar_estructura(self):
        """Verifica el conteo de oraciones y párrafos"""
        texto = "Primera oración. Segunda oración!\n\nSegundo párrafo."
        oraciones, parrafos = analizar_estructura(texto)
        self.assertEqual(oraciones, 3)
        self.assertEqual(parrafos, 2)

    def test_analizar_vocabulario_extremos(self):
        """Verifica identificación de palabra más larga y corta"""
        palabras = ["ia", "tecnologia", "programacion"]
        unicas, porc, larga, corta = analizar_vocabulario(palabras)
        self.assertEqual(larga, "programacion")
        self.assertEqual(corta, "ia")
        self.assertEqual(unicas, 3)

    def test_casos_vacios(self):
        """Prueba el comportamiento con listas o textos vacíos"""
        total_p, _, _, l_med = contar_estadisticas_basicas("", [])
        self.assertEqual(total_p, 0)
        self.assertEqual(l_med, 0)
        
        _, _, larga, corta = analizar_vocabulario([])
        self.assertEqual(larga, "N/A")
        self.assertEqual(corta, "N/A")

if __name__ == "__main__":
    unittest.main()