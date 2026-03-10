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

def formatear_informe(stats):
    """
    Recibe el diccionario 'stats' generado por el analizador 
    y lo convierte en un texto visual para el usuario.
    """
    res = (
        f"\n{'='*30}\n RESULTADOS DEL ANÁLISIS\n{'='*30}\n"
        f"Texto: {stats['oraciones']} oraciones | {stats['parrafos']} párrafos\n"
        f"Palabras totales: {stats['total']}\n"
        f"Palabras únicas: {stats['unicas']} ({stats['porcentaje_unicas']:.1f}%)\n"
        f"Longitud media: {stats['media']:.1f} letras\n"
        f"Palabra más larga: {stats['p_larga']}\n"
        f"\nTOP 5 palabras:\n"
    )
    
    # Recorremos la lista de tuplas para el TOP 5
    for i, (pal, cant) in enumerate(stats['top'], 1):
        res += f"{i}. {pal}: {cant} {'vez' if cant == 1 else 'veces'}\n"
        
    return res