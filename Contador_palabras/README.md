# 📝 Contador de Palabras de Texto

## Descripción

Contador de Palabras de Texto es una herramienta en Python diseñada para analizar y procesar texto de forma rápida y precisa. Permite obtener estadísticas detalladas sobre palabras, caracteres, oraciones y frecuencia de términos, facilitando el trabajo de escritores, estudiantes y editores.

## 🎯 Objetivos del Proyecto

- Precisión: Contabilizar palabras ignorando ruidos como espacios múltiples o signos de puntuación.

- Análisis profundo: Proveer métricas de caracteres (con/sin espacios), oraciones y párrafos.

- Frecuencia: Identificar las palabras más utilizadas y la densidad del texto.

- Eficiencia: Procesar archivos extensos sin degradar el rendimiento del sistema.
---

## ✨ Funcionalidades

| Funcionalidad             | Descripción                                      |
|--------------------------|--------------------------------------------------|
| 📊 Conteo de palabras     | Total de palabras únicas y repetidas             |
| 🔤 Conteo de caracteres   | Con y sin espacios                               |
| 📄 Párrafos y oraciones   | Detección automática de estructura               |
| ⏱️ Tiempo de lectura      | Estimación basada en velocidad promedio          |
| 🔁 Palabras frecuentes    | Ranking de las palabras más utilizadas           |
| 📋 Análisis de densidad   | Porcentaje de repetición por palabra clave       |
| 🌍 Soporte multilenguaje  | Compatible con caracteres especiales y acentos   |

---

## 🚀 Instalación
Asegúrate de tener Python 3.x instalado en tu sistema.

## 1. Clonar el repositorio
git clone https://github.com/tu-usuario/CONTADOR_PALABRAS.git

## 2. Entrar al directorio
cd CONTADOR_PALABRAS

---

## 🛠️ Uso y Ejemplos de Ejecución

El punto de entrada principal del programa es src/main.py.

## 1. Ejecución Básica
Para analizar uno de los archivos de texto incluidos en la carpeta texto/:

python src/main.py --archivo texto/informe.txt

## 2. Ejemplo de Salida en Terminal
Al ejecutar el comando anterior, verás un resumen como este:

## 📊 Resumen de Estadísticas: `informe.txt`

| Métrica | Resultado |
| :--- | :--- |
| **Palabras totales** | 450 |
| **Caracteres (sin espacios)** | 2,100 |
| **Párrafos detectados** | 5 |
| **Tiempo estimado de lectura** | 2 min 15 seg |

## 📊 🔝 Top 3 Palabras más Frecuentes

| Rango | Palabra | Frecuencia |
| :---: | :--- | :--- |
| 1° | "desarrollo" | 12 veces |
| 2° | "sistema" | 8 veces |
| 3° | "análisis" | 5 veces |


## 📁 Estructura del Proyecto

```
CONTADOR_PALABRAS/
├── .qodo/                 # Configuración de herramientas de IA/Agentes
├── docs/                  # Documentación del proyecto
│   ├── asistencia_ia.md
│   └── caso edge.md
├── src/                   # Código fuente principal
│   ├── __init__.py
│   ├── analizador.py      # Lógica de conteo y procesamiento
│   ├── exportador.py      # Generación de reportes (CSV, JSON, etc.)
│   ├── lector_archivos.py # Manejo de apertura de archivos (.txt, .pdf)
│   └── main.py            # Punto de entrada de la aplicación
├── tests/                 # Pruebas unitarias e integración
│   ├── __init__.py
│   ├── test_analizador.py
│   ├── test_exportador.py
│   ├── test_lector.py
│   └── test_main.py
├── data/                  # Carpeta para archivos de entrada/salida (antes 'texto')
│   ├── inputs/            # Archivos a procesar (ejemplos.txt)
│   └── outputs/           # Resultados generados (informe.txt)
├── .gitignore             # Archivos que Git debe ignorar (ej. __pycache__)
├── LICENSE                # Licencia del software
├── README.md              # Descripción general y cómo usar el proyecto
└── requirements.txt       # Librerías externas necesarias
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---