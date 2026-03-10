# Registro de Asistencia por IA - Contador de Palabras
Este documento detalla los prompts y la interacción con modelos de IA utilizados para el diseño, desarrollo y pruebas del proyecto.

## 1. Fase de Arquitectura y Estructura
Prompt:

"Genera una estructura de archivos para un proyecto de Python llamado 'Contador de Palabras' que siga las buenas prácticas. Debe incluir una carpeta src para la lógica, test para pruebas unitarias con pytest, docs para documentación y una carpeta para archivos de texto de ejemplo."

Resultado:

Creación de la jerarquía de carpetas: src/, test/, docs/, textos/.

Inclusión de archivos base: requirements.txt, .gitignore y README.md.

## 2. Desarrollo de Módulos (Lógica Core)
Prompt:

"Escribe el código para src/lector_archivos.py que maneje la lectura de archivos .txt y maneje errores de archivo no encontrado. También, crea src/analizador.py con una función que cuente palabras, ignorando signos de puntuación básicos."

## 3. Pruebas Unitarias
Prompt:

"Basado en los archivos en src/, genera pruebas unitarias utilizando pytest. Crea casos de prueba para test_analizador.py que cubran: cadenas vacías, múltiples espacios y caracteres especiales. Asegúrate de incluir un __init__.py en la carpeta de tests para el manejo de módulos."

## 4. Documentación y Casos de Borde
Prompt:

"Ayúdame a redactar un documento de 'Casos de Borde' (docs/caso edge.md) para este contador de palabras. ¿Qué debería considerar además de archivos vacíos? (Ej: codificación UTF-8, archivos extremadamente grandes, símbolos matemáticos)."

# Notas de Implementación
Modelo utilizado: Gemini.

Uso de herramientas: Generación de código base y plantillas de pruebas.

Revisión humana: El archivo main.py fue ajustado manualmente para integrar todos los módulos y manejar el flujo de usuario por consola.