# 📝 Contador de Palabras

Aplicación Python para el análisis y conteo de palabras en textos, con soporte para procesamiento de archivos y generación de estadísticas lingüísticas.

---

# 📋 Descripción

**Contador de Palabras** es una herramienta de análisis de texto desarrollada en Python que permite procesar archivos de texto y obtener métricas detalladas sobre su contenido. El proyecto está diseñado con una arquitectura modular que separa claramente la entrada de datos, el procesamiento y las utilidades auxiliares.

---

# 🎯 Objetivos

- Contar el número total de palabras, caracteres y líneas en un texto o archivo.
- Calcular la frecuencia de aparición de cada palabra.
- Identificar las palabras más frecuentes en un texto.
- Proporcionar estadísticas lingüísticas: promedio de palabras por línea, longitud media de palabras, etc.
- Soportar múltiples formatos de entrada (texto directo, archivos `.txt`).
- Facilitar el análisis de textos mediante una interfaz simple y extensible.

---

# 🗂️ Estructura del Proyecto

```
Contador_palabras/
│
├── docs/                        # Documentación del proyecto
│   ├── asistencia_ia.md         # Registro de asistencia con IA
│   └── caso_edge.md             # Casos borde y consideraciones especiales
│
├── src/                         # Código fuente principal
│   ├── __init__.py
│   ├── entrada.py               # Módulo de entrada de datos
│   ├── procesador.py            # Lógica principal de procesamiento
│   └── utilidades.py            # Funciones auxiliares y helpers
│
├── test/                        # Suite de pruebas
│   └── src/
│       ├── __init__.py
│       ├── test_entrada.py      # Tests del módulo de entrada
│       ├── test_procesador.py   # Tests del módulo procesador
│       ├── test_utilidades.py   # Tests de utilidades
│       └── test_main.py         # Tests de integración
│
├── textos/                      # Archivos de texto de ejemplo/prueba
├── info_analisis/               # Resultados y reportes de análisis
│
├── main.py                      # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
├── .gitignore
├── LICENSE
└── README.md
```

---

# ⚙️ Requisitos Previos

- Python **3.14**

---

# 🚀 Instalación

1. **Clona el repositorio:**

```
git clone https://github.com/tu-usuario/Contador_palabras.git
cd Contador_palabras
```
---

# 📖 Uso

## Ejecución básica

```
python main.py
```

## Analizar un archivo de texto

```
python main.py --archivo textos/mi_texto.txt
```

## Analizar texto directo desde la terminal

```
python main.py --texto "El veloz zorro marrón salta sobre el perro perezoso"
```

## Ver las N palabras más frecuentes

```
python main.py --archivo textos/mi_texto.txt --top 10
```

## Guardar resultados en un archivo

```
python main.py --archivo textos/mi_texto.txt --salida info_analisis/resultado.txt
```

---

## 📊 Ejemplo de Salida

```
============================================================
          ANÁLISIS DE TEXTO - CONTADOR DE PALABRAS
============================================================

📄 Archivo analizado : textos/ejemplo.txt
📏 Total de líneas   : 42
🔤 Total de palabras : 318
🔡 Total caracteres  : 1,847

📈 Estadísticas:
   - Palabras únicas          : 124
   - Promedio palabras/línea  : 7.57
   - Longitud media de palabra: 4.82

🏆 Top 5 palabras más frecuentes:
   1. "que"     →  18 veces
   2. "de"      →  15 veces
   3. "la"      →  12 veces
   4. "en"      →  10 veces
   5. "el"      →   9 veces

============================================================
```

---

## 🧪 Ejecutar Tests

```
# Todos los tests
python -m pytest test/

# Tests con detalle
python -m pytest test/ -v

# Tests de un módulo específico
python -m pytest test/src/test_procesador.py -v

# Tests con reporte de cobertura
python -m pytest test/ --cov=src --cov-report=term-missing
```

---

## 🧩 Módulos Principales

| Módulo | Descripción |
|---|---|
| `entrada.py` | Lectura y validación de archivos o texto de entrada |
| `procesador.py` | Algoritmos de conteo, análisis de frecuencias y estadísticas |
| `utilidades.py` | Funciones de apoyo: limpieza de texto, formateo de salida |
| `main.py` | Punto de entrada, parseo de argumentos CLI |

---

## 📄 Licencia

Este proyecto está licenciado bajo los términos del archivo [LICENSE](LICENSE MIT).

---
