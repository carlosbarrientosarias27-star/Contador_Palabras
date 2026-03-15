# Contador de Palabras

Aplicación en Python para el análisis y conteo de palabras en textos, con una suite de pruebas unitarias integrada.

---

# 📁 Estructura del Proyecto

```
Contador_palabras/
├── docs/
│   ├── asistencia_ia.md
│   └── caso edge.md
├── src/
│   ├── __init__.py
│   ├── entrada.py
│   ├── procesador.py
│   └── utilidades.py
├── test/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── test_entrada.py
│   │   ├── test_procesador.py
│   │   └── test_utilidades.py
│   ├── __init__.py
│   └── test_main.py
├── textos/
│   └── ejemplo.txt
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

---

## 🧩 Módulos principales (`src/`)

| Archivo | Descripción |
|---|---|
| `entrada.py` | Gestión y lectura de la entrada de texto (archivo o texto directo) |
| `procesador.py` | Lógica central de procesamiento y conteo de palabras |
| `utilidades.py` | Funciones auxiliares y helpers del proyecto |

---

## 🧪 Tests (`test/`)

| Archivo | Descripción |
|---|---|
| `test_entrada.py` | Pruebas unitarias del módulo de entrada |
| `test_procesador.py` | Pruebas unitarias del procesador de palabras |
| `test_utilidades.py` | Pruebas unitarias de las utilidades |
| `test_main.py` | Pruebas de integración del flujo principal |

---

# 📂 Proyecto de Prueba

Proyecto auxiliar de demostración que integra y valida el funcionamiento del contador de palabras.

```
Proyecto de Prueba/
├── __init__.py
├── Contador.py
└── readme.md
```

| Archivo | Descripción |
|---|---|
| `Contador.py` | Implementación de prueba que consume la lógica de `Contador_palabras` |

---

# 🚀 Instalación y uso

## Prerrequisitos

- Python 3.14

## Instalación

```
git clone <url-del-repositorio>
cd Contador_palabras
pip install -r requirements.txt
```

## Ejecución

```
python main.py
```

## Ejecutar los tests

```
python -m pytest test/
```

---

# 📄 Documentación

En la carpeta `docs/` se encuentran:

- **`asistencia_ia.md`** — Notas sobre el uso de IA como asistencia en el desarrollo.
- **`caso edge.md`** — Descripción y manejo de casos límite contemplados en el procesador.

---

# 📝 Licencia

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](LICENSE MIT).