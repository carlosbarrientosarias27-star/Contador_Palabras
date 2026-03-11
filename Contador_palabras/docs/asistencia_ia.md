# Registro de Asistencia de IA - Proyecto Contador_palabras

Este documento detalla la metodología y los prompts utilizados durante el desarrollo del proyecto para garantizar la transparencia en el uso de herramientas de Inteligencia Artificial.

---

# 1. Diseño de Arquitectura y Estructura
**Objetivo:** Definir la jerarquía de carpetas y la modularización del código.

* **Prompt:** > "Actúa como un arquitecto de software senior. Diseña una estructura de proyecto en Python para una herramienta de conteo de palabras que sea modular. Debe incluir carpetas para código fuente (`src`), pruebas (`test`), documentación (`docs`) y manejo de archivos de texto (`textos`). Asegúrate de seguir las buenas prácticas de Python (PEP 8)."

---

# 2. Desarrollo de Módulos Core (`src/`)
**Objetivo:** Implementar la lógica de procesamiento y utilidades.

* **Módulo `procesador.py`:**
    > "Genera una función en Python que reciba un string y devuelva un diccionario con la frecuencia de cada palabra, ignorando mayúsculas/minúsculas y eliminando signos de puntuación básicos."
* **Módulo `entrada.py`:**
    > "Crea una función para leer archivos .txt de forma segura, manejando excepciones en caso de que el archivo no exista o esté vacío."

---

# 3. Estrategia de Testing (`test/`)
**Objetivo:** Asegurar la calidad del código mediante pruebas unitarias.

* **Prompt para `test_procesador.py`:**
    > "Usando la librería `unittest`, escribe pruebas para un procesador de palabras. Incluye casos para: strings vacíos, palabras repetidas, y mezcla de caracteres especiales."
* **Prompt para `caso edge.md`:**
    > "Identifica posibles casos de borde (edge cases) para un contador de palabras que lee archivos externos, como archivos con codificación distinta a UTF-8 o archivos extremadamente grandes."

---

# 4. Documentación y DevOps
**Objetivo:** Preparar el proyecto para su distribución y mantenimiento.

* **Prompt para `.gitignore`:**
    > "Genera un archivo .gitignore estándar para un proyecto de Python, asegurándote de incluir carpetas de cache como `__pycache__` y entornos virtuales."
* **Prompt para `requirements.txt`:**
    > "Analiza la estructura del proyecto y sugiere las dependencias mínimas necesarias si solo uso la biblioteca estándar y unittest."

---

# Resumen de Herramientas
* **Modelo IA:** Gemini 3 Flash / GPT-4 (según corresponda).
* **Uso principal:** Refactorización de código, generación de pruebas unitarias y estructuración de documentación técnica.