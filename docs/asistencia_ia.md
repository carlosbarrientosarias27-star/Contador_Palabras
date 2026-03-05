# Registro de Asistencia de IA - Proyecto Contador de Palabras

Este documento detalla la interacción con la IA para el desarrollo de las pruebas unitarias y la resolución de problemas de estructura del proyecto.

## 1. Módulo: lector.py
**Prompt:** "necesito hacer un test.py donde realizar pruebas unitarias de mi carpeta src donde esta mi archivo lector.py"

**Resultado:**
- Creación de `test/test_lector.py` usando `unittest.mock`.
- Implementación de simulación de entradas de terminal (`patch('builtins.input')`).
- Implementación de simulación de archivos (`mock_open`).

## 2. Módulo: analizador.py
**Prompt:** "necesito hacer un test.py donde realizar pruebas unitarias de mi carpeta src donde esta mi archivo analizador.py"

**Resultado:**
- Creación de `test/test_analizador.py`.
- Pruebas para conteo básico, estructuras (oraciones/párrafos) y estadísticas avanzadas.
- Resolución de error de precisión en `media_longitud` usando `assertAlmostEqual` para manejar decimales como `4.6666...`.

## 3. Módulo: exportador.py
**Prompt:** "necesito hacer un test.py donde realizar pruebas unitarias de mi carpeta src donde esta mi archivo exportador.py"

**Resultado:**
- Creación de `test/test_exportador.py`.
- Verificación de la escritura correcta en `informe.txt` sin crear archivos físicos.
- Validación del manejo de errores cuando no hay permisos de escritura.

## 4. Módulo: main.py (Orquestador)
**Prompt:** "necesito hacer un test.py donde realizar pruebas unitarias de mi carpeta src donde esta mi archivo main.py"

**Resultado:**
- Creación de `test/test_main.py`.
- Pruebas de flujo del menú principal y captura de la salida de consola (`patch('builtins.print')`).
- Simulación de la opción "Salir" para verificar el cierre correcto del bucle.

## 5. Resolución de Errores Técnicos (Estructura y Rutas)
**Problema:** `ModuleNotFoundError: No module named 'src'`
**Prompts de resolución:**
- "File "...test_lector.py", line 9, in <module> from src.lector import ... ModuleNotFoundError: No module named 'src'"

**Solución aplicada:**
1. **Configuración de Path:** Inserción dinámica de la raíz del proyecto en `sys.path` dentro de cada archivo de test.
2. **Importaciones de Paquete:** Ajuste en `main.py` para usar importaciones absolutas (`from src.lector import...`) en lugar de relativas.
3. **Paquetes Python:** Creación de archivos `__init__.py` en las carpetas `src/` y `test/` para reconocimiento de módulos.

## 6. Comandos de Ejecución Identificados
Para ejecutar las pruebas correctamente desde la raíz del proyecto:
- `python -m unittest test/test_lector.py`
- `python -m unittest test/test_analizador.py`
- `python -m unittest test/test_exportador.py`
- `python -m unittest test/test_main.py`