# 📦 Repositorio: Contador_palabras & Proyecto de Prueba

Este repositorio contiene dos proyectos Python relacionados: **Contador_palabras**, una aplicación modular para el procesamiento y conteo de texto, y **Proyecto de Prueba**, un módulo auxiliar de apoyo.

---

# 📁 Estructura del Repositorio

```
raíz/
├── Contador_palabras/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── entrada.py
│   │   ├── procesador.py
│   │   └── utilidades.py
│   ├── test/
│   │   ├── src/
│   │   │   ├── __init__.py
│   │   │   ├── test_entrada.py
│   │   │   ├── test_procesador.py
│   │   │   └── test_utilidades.py
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── textos/
│   │   └── ejemplo.txt
│   ├── docs/
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
└── Proyecto de Prueba/
    ├── __init__.py
    ├── Contador.py
    └── readme.md
```

---

# 🔡 Contador_palabras

## Descripción

**Contador_palabras** es una aplicación Python modular diseñada para leer, procesar y analizar texto. Permite contar palabras, frecuencias u otras métricas textuales a partir de archivos de entrada.

## Módulos principales (`src/`)

| Módulo | Descripción |
|---|---|
| `entrada.py` | Gestiona la lectura y validación de los archivos de texto de entrada. |
| `procesador.py` | Contiene la lógica central de procesamiento y análisis del texto. |
| `utilidades.py` | Funciones de apoyo reutilizables (limpieza, normalización, etc.). |

## Archivos de texto (`textos/`)

- `ejemplo.txt` — Archivo de muestra utilizado para pruebas y demostración.

## Tests (`test/`)

Las pruebas unitarias están organizadas en `test/src/` y cubren los tres módulos principales:

- `test_entrada.py`
- `test_procesador.py`
- `test_utilidades.py`
- `test_main.py` — Prueba de integración del flujo completo.

## Ejecución

```
# Ejecutar la aplicación
python main.py

---

# 🧪 Proyecto de Prueba

## Descripción

**Proyecto de Prueba** es un módulo complementario que incluye una implementación independiente de un contador (`Contador.py`), útil para pruebas aisladas o como referencia de integración con `Contador_palabras`.

## Archivos

| Archivo | Descripción |
|---|---|
| `__init__.py` | Inicializa el módulo Python. |
| `Contador.py` | Implementación del contador de palabras en formato simplificado. |
| `readme.md` | Documentación específica del proyecto de prueba. |

## Uso básico

```python
from Contador import Contador

c = Contador()
resultado = c.contar("Hola mundo, esto es una prueba")
print(resultado)
```

---

# ⚙️ Requisitos generales

- Python 3.14

---

# 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo [`LICENSE`](Contador_palabras/LICENSE).

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* o un *pull request* con tus sugerencias o mejoras.
