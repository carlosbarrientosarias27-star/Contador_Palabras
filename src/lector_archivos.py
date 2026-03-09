import os

def crear_archivo_ejemplo(ruta):
    """Crea un archivo de texto con contenido de prueba."""
    contenido = (
        "Línea 1: El análisis de datos es fundamental.\n"
        "Línea 2: Python facilita la manipulación de archivos.\n"
        "Línea 3: Manejar excepciones evita que el programa falle.\n"
        "Línea 4: ¡Prueba de carga exitosa!"
    )
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"✅ Archivo creado exitosamente en: {ruta}")
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")

def leer_archivo(ruta):
    """Lee el contenido de un archivo .txt con manejo de errores."""
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"La ruta '{ruta}' no existe.")
    
    if not ruta.endswith('.txt'):
        raise ValueError("El archivo debe tener extensión .txt")

    with open(ruta, 'r', encoding='utf-8') as f:
        contenido = f.read()
        
    if not contenido.strip():
        raise EOFError("El archivo está vacío.")
        
    return contenido

def ejecutar_analisis_completo(ruta):
    """Coordina la carga y el análisis del texto."""
    try:
        texto = leer_archivo(ruta)
        print("📖 Contenido cargado correctamente. Iniciando análisis...")
        
        # Aquí llamarías a tus funciones de análisis previas
        # Ejemplo:
        # resultado1 = contar_palabras(texto)
        # resultado2 = analizar_sentimiento(texto)
        
        print("📊 Análisis finalizado con éxito.")
        return texto
        
    except FileNotFoundError as e:
        print(f"⚠️ Error: No se encontró el archivo. {e}")
    except EOFError as e:
        print(f"⚠️ Error: Archivo sin contenido. {e}")
    except ValueError as e:
        print(f"⚠️ Error de formato: {e}")
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

# --- Bloque de ejecución ---
if __name__ == "__main__":
    ruta_ejemplo = "textos/ejemplo.txt"
    crear_archivo_ejemplo(ruta_ejemplo)
    ejecutar_analisis_completo(ruta_ejemplo)