import os 

def capturar_texto_manual():
    """
    Pide al usuario que introduzca un texto en la terminal.
    Permite varias líneas usando una línea vacía como delimitador (Commit 2)[cite: 53, 54].
    """
    print("\nEscribe tu texto (deja una línea vacía para terminar):")
    lineas = []
    while True:
        linea = input("> ")
        if not linea:
            break
        lineas.append(linea)
    
    texto = "\n".join(lineas)
    if not texto.strip(): # Manejo de caso sin texto (Commit 2) [cite: 56]
        print("Error: No has introducido ningún texto.")
        return None
    return texto

def cargar_desde_archivo(ruta):
    """
    Carga y lee un archivo .txt manejando errores de ruta o contenido (Commit 7)[cite: 116, 118].
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