import os

def leer_terminal():
    """
    Pide al usuario texto por terminal permitiendo múltiples líneas.
    Finaliza al detectar una línea vacía.
    """
    print("\nEscribe tu texto (deja una línea vacía para terminar):")
    lineas = []
    
    while True:
        linea = input("> ")
        if linea == "":
            break
        lineas.append(linea)
    
    texto_completo = "\n".join(lineas)
    
    # Manejar el caso en que el usuario no introduzca nada
    if not texto_completo.strip():
        print("Error: No se ha introducido ningún texto.")
        return None
        
    # Mostrar el texto de vuelta para confirmarlo
    print("\n--- Texto recibido correctamente ---")
    return texto_completo

def leer_archivo(ruta):
    """
    Carga y lee un archivo .txt dado su ruta.
    Maneja errores de archivo no encontrado o vacío.
    """
    # Manejar error: ruta incorrecta o archivo no existe
    if not os.path.exists(ruta):
        print(f"Error: La ruta '{ruta}' no es válida o el archivo no existe.")
        return None
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
            # Manejar error: archivo vacío
            if not contenido.strip():
                print("Error: El archivo está vacío.")
                return None
                
            return contenido
            
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return None