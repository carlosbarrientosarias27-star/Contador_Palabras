import os 

def capturar_texto_manual():
    """
    Captura texto multilínea introducido manualmente por el usuario.

    Permite al usuario escribir varias líneas en la terminal, finalizando
    la captura al introducir una línea vacía.
    
    Returns:
        str: El texto completo unido por saltos de línea, o None si está vacío.
    """
    print("\nEscribe tu texto (deja una línea vacía para terminar):")
    lineas = []
    while True:
        linea = input("> ")
        if not linea:
            break
        lineas.append(linea)
    
    texto = "\n".join(lineas)
    if not texto.strip():
        print("Error: No has introducido ningún texto.")
        return None
    return texto

def cargar_desde_archivo(ruta):
    """
    Carga y lee el contenido de un archivo de texto plano.

    Verifica la existencia del archivo y maneja posibles errores de lectura
    o archivos vacíos.

    Args:
        ruta (str): La ubicación relativa o absoluta del archivo .txt.

    Returns:
        str: El contenido del archivo como cadena de texto, o None si hay error.
    """
    try:
        if not os.path.exists(ruta):
            print(f"Error: El archivo en '{ruta}' no existe.")
            return None
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if not contenido.strip():
                print("Error: El archivo está vacío.")
                return None
            return contenido
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None