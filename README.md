# 📝 Contador de Palabras

Aplicación de contador de palabras de textos: conteo de palabras, frecuencias, estadísticas y generación de reportes. Incluye una interfaz gráfica intuitiva y un módulo analizador de alto rendimiento.

---

# 🎯 Objetivos

- **Analizar textos** de forma automática: contar palabras, caracteres, párrafos y oraciones.
- **Calcular frecuencias** de palabras y generar rankings de términos más usados.
- **Generar reportes** exportables con los resultados del análisis.
- **Ofrecer una interfaz gráfica** amigable para usuarios no técnicos.
- **Facilitar la extensión** del proyecto mediante una arquitectura modular (`core`, `utils`).

---

# 🗂️ Estructura del Proyecto

```
Contador_palabras/
├── core/
│   └── analizador.py         # Motor principal de análisis de texto
├── docs/
│   ├── asistencia_ia.md      # Documentación de asistencia con IA
│   └── caso_edge.md          # Casos edge y comportamientos especiales
├── reportes/                 # Carpeta de salida para reportes generados (informes.txt) 
├── test/
│   ├── core/                 # Tests unitarios del módulo core
│   └── utils/
│       ├── test_archivos.py  # Tests para manejo de archivos
│       ├── test_interfaz.py  # Tests para la interfaz gráfica
│       └── test_main.py      # Tests de integración principal
├── textos/                   # Textos de ejemplo para pruebas
├── utils/
│   ├── archivos.py           # Utilidades de lectura/escritura de archivos
│   └── interfaz.py           # Componentes de la interfaz gráfica
├── main.py                   # Punto de entrada de la aplicación
├── requirements.txt          # Dependencias del proyecto
├── .gitignore
├── LICENSE
└── README.md
```

---

# ⚙️ Requisitos

- Python **3.14**

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/Contador_palabras.git
cd Contador_palabras
```

## 2. Crear un entorno virtual (recomendado)

```
python -m venv venv

# En Linux/macOS:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

## 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

# ▶️ Uso

## Ejecutar la aplicación con interfaz gráfica

```
python main.py
```

Esto abre la ventana principal donde puedes:
- Pegar o escribir texto directamente.
- Cargar un archivo `.txt` desde tu sistema.
- Ver las estadísticas en tiempo real.
- Exportar el reporte a la carpeta `reportes/`.

## Uso desde la línea de comandos (modo CLI)

Si el proyecto admite ejecución sin GUI:

```bash
python main.py --archivo textos/ejemplo.txt
```

## Uso del módulo `analizador` directamente

```python
from core.analizador import Analizador

texto = "Hola mundo. Hola Python. El mundo es grande."
analizador = Analizador(texto)

print(analizador.contar_palabras())       # → 8
print(analizador.contar_caracteres())     # → 44
print(analizador.frecuencia_palabras())   # → {'hola': 2, 'mundo': 2, ...}
print(analizador.palabras_mas_usadas(3))  # → [('hola', 2), ('mundo', 2), ('el', 1)]
```

### Leer un archivo y analizarlo

```python
from utils.archivos import leer_archivo
from core.analizador import Analizador

texto = leer_archivo("textos/mi_documento.txt")
analizador = Analizador(texto)
reporte = analizador.generar_reporte()
print(reporte)
```

---

## 🧪 Ejecutar Tests

```bash
# Todos los tests
python -m pytest test/

# Solo tests del core
python -m pytest test/core/

# Solo tests de utilidades
python -m pytest test/utils/

# Con reporte de cobertura
python -m pytest --cov=core --cov=utils test/
```

---

## 📊 Ejemplo de Reporte Generado

```
========================================
        REPORTE DE ANÁLISIS DE TEXTO
========================================
Palabras totales     : 312
Palabras únicas      : 178
Caracteres (c/esp.)  : 1.847
Caracteres (s/esp.)  : 1.541
Oraciones            : 24
Párrafos             : 6

Top 5 palabras más frecuentes:
  1. "que"      →  18 veces
  2. "de"       →  15 veces
  3. "la"       →  12 veces
  4. "en"       →  10 veces
  5. "Python"   →   7 veces
========================================
```

---

## 📄 Licencia

Este proyecto está bajo la licencia indicada en el archivo [LICENSE](LICENSE).