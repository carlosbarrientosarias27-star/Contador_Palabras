# Registro de Asistencia de Inteligencia Artificial - Contador de Palabras

Este documento recopila los prompts y la lógica de interacción con la IA para el desarrollo del proyecto **Contador_palabras**.

---

## 1. Arquitectura del Proyecto
**Prompt:**
> "Genera una estructura de carpetas para un proyecto de Python llamado 'Contador_palabras'. Organiza el código en una carpeta 'core' para el análisis de texto, 'utils' para manejo de archivos e interfaz, y una carpeta 'test' que replique esta estructura para pruebas unitarias. Incluye directorios para reportes y documentos."

---

## 2. Lógica de Análisis (`core/analizador.py`)
**Prompt:**
> "Crea una función en Python que reciba un string y devuelva un diccionario con: el número total de palabras, el número de caracteres (con y sin espacios) y la frecuencia de cada palabra. Ignora mayúsculas y signos de puntuación básicos."

---

## 3. Utilidades y Archivos (`utils/archivos.py` e `interfaz.py`)
**Prompts:**
> "Escribe un módulo que lea archivos `.txt` de forma segura y maneje excepciones si el archivo no existe o no tiene permisos de lectura."
> 
> "Genera una interfaz de línea de comandos (CLI) simple usando `argparse` que permita al usuario pasar la ruta de un archivo como argumento."

---

## 4. Generación de Reportes (`reportes/`)
**Prompt:**
> "Crea una función que exporte los resultados del análisis de texto a un archivo `.txt` con un formato limpio. El nombre del archivo debe incluir la fecha y hora actual (timestamp), por ejemplo: 'informe_2026-03-10_10-14-13.txt'."

---

## 5. Estrategia de Pruebas (`test/`)
**Prompt:**
> "Genera casos de prueba con `pytest` para:
> 1. `test.analizador.py`: Validar el conteo exacto con strings vacíos, palabras repetidas y caracteres especiales.
> 2. `test_archivos.py`: Simular (mock) la lectura de un archivo para verificar que el contenido se procesa correctamente.
> 3. `test_main.py`: Probar el flujo completo desde la entrada del usuario hasta la generación del reporte."

---

## 6. Manejo de Casos Especiales (`docs/caso edge.md`)
**Prompt:**
> "¿Qué debería considerar mi contador de palabras al procesar archivos extremadamente grandes o archivos con codificaciones de texto no estándar (como UTF-16 o ISO-8859-1)? Ayúdame a documentar estos casos de borde."