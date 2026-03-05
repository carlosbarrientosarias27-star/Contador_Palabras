# 📝 Contador de Palabras de Texto

![Version](https://img.shields.io/badge/versión-1.0.0-blue)
![License](https://img.shields.io/badge/licencia-MIT-green)
![Status](https://img.shields.io/badge/estado-activo-brightgreen)

## Descripción

**Contador de Palabras de Texto** es una herramienta diseñada para analizar y procesar texto de forma rápida y precisa. Permite a los usuarios obtener estadísticas detalladas sobre cualquier contenido textual: palabras, caracteres, oraciones, párrafos y mucho más, sin necesidad de instalaciones complejas ni conocimientos técnicos avanzados.

Ideal para escritores, estudiantes, traductores, periodistas y cualquier persona que trabaje con texto de forma habitual.

---

## 🎯 Objetivos del Proyecto

### Objetivo General
Proporcionar una herramienta accesible, precisa y eficiente para el análisis estadístico de texto, que ayude a los usuarios a comprender y medir la extensión y complejidad de sus contenidos.

### Objetivos Específicos

1. **Contar palabras con precisión**  
   Detectar y contabilizar correctamente las palabras de un texto, ignorando espacios múltiples, saltos de línea y signos de puntuación.

2. **Analizar caracteres**  
   Ofrecer el conteo de caracteres totales, con y sin espacios, para adaptarse a distintos requisitos editoriales o de plataforma.

3. **Estadísticas adicionales**  
   Calcular el número de oraciones, párrafos y la frecuencia de palabras más usadas dentro del texto.

4. **Tiempo estimado de lectura**  
   Estimar el tiempo de lectura promedio basado en la cantidad de palabras (velocidad estándar: ~200 palabras por minuto).

5. **Soporte multilenguaje**  
   Funcionar correctamente con textos en español, inglés y otros idiomas con caracteres especiales (tildes, ñ, ü, etc.).

6. **Interfaz intuitiva y accesible**  
   Ofrecer una experiencia de usuario clara, sin curva de aprendizaje, accesible desde navegador o línea de comandos.

7. **Rendimiento con textos largos**  
   Procesar documentos extensos (libros, informes, artículos) de forma eficiente sin pérdida de rendimiento.

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

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/contador-palabras.git

# Entrar al directorio
cd contador-palabras

# Instalar dependencias
npm install
```

---

## 🛠️ Uso

```bash
# Ejecutar con un archivo de texto
node index.js --archivo mi_texto.txt

# Analizar texto directamente desde la terminal
node index.js --texto "Escribe tu texto aquí"

# Ver todas las opciones disponibles
node index.js --ayuda
```

---

## 📁 Estructura del Proyecto

```
contador-palabras/
├── src/
│   ├── contador.js       # Lógica principal de conteo
│   ├── analizador.js     # Análisis estadístico
│   └── utils.js          # Funciones auxiliares
├── tests/
│   └── contador.test.js  # Pruebas unitarias
├── examples/
│   └── ejemplo.txt       # Texto de muestra
├── index.js              # Punto de entrada
├── package.json
└── README.md
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* para discutir cambios importantes antes de enviar un *pull request*.

1. Haz un fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m 'Agrega nueva funcionalidad'`
4. Sube la rama: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

> Desarrollado con ❤️ para facilitar el trabajo con texto cotidiano.