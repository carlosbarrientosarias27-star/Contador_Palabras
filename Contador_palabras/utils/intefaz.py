import os

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def capturar_texto_manual():
    """Captura texto del usuario hasta una línea vacía."""
    print("\nEscribe tu texto (deja una línea vacía para terminar):")
    lineas = []
    while True:
        linea = input("> ")
        if not linea: break
        lineas.append(linea)
    return "\n".join(lineas) if lineas else None

def formatear_informe(res):
    """Muestra los resultados formateados en pantalla."""
    # Aquí puedes mover la lógica de impresión de 'analizar_texto'
    return res