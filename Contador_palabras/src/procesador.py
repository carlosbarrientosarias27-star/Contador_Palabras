import re 
from collections import Counter 

def analizar_texto(texto):
    """
    Realiza un análisis estadístico y lingüístico exhaustivo del texto.

    Calcula métricas como total de palabras, oraciones, párrafos, 
    caracteres y frecuencia de términos, retornando un informe formateado.

    Args:
        texto (str): La cadena de texto que se desea procesar.

    Returns:
        str: Un informe detallado con los resultados del análisis.
    """
    # 1. Palabras y Caracteres
    palabras_totales = texto.split() 
    total_palabras = len(palabras_totales)
    caracteres_con = len(texto)
    caracteres_sin = len(texto.replace(" ", "").replace("\n", ""))

    # 2. Oraciones y Párrafos
    oraciones = [o for o in re.split(r'[.!?]+', texto) if o.strip()]
    parrafos = [p for p in texto.split('\n\n') if p.strip()]

    # 3. Palabras frecuentes
    palabras_limpias = re.findall(r'\b\w+\b', texto.lower())
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un'} 
    filtradas = [p for p in palabras_limpias if p not in stop_words]
    top_5 = Counter(filtradas).most_common(5)

    # 4. Estadísticas Avanzadas
    unicas = set(palabras_limpias)
    longitud_media = sum(len(p) for p in palabras_limpias) / len(palabras_limpias) if palabras_limpias else 0
    p_larga = max(palabras_limpias, key=len) if palabras_limpias else "-"
    p_corta = min(palabras_limpias, key=len) if palabras_limpias else "-"

    porcentaje_unicas = (len(unicas) / total_palabras) * 100 if total_palabras > 0 else 0

    res = (
        f"\n{'='*30}\n RESULTADOS DEL ANÁLISIS\n{'='*30}\n"
        f"Texto analizado: {len(oraciones)} oraciones | {len(parrafos)} párrafos\n"
        f"Palabras totales: {total_palabras}\n"
        f"Caracteres (con espacios): {caracteres_con}\n"
        f"Caracteres (sin espacios): {caracteres_sin}\n"
        f"Palabras únicas: {len(unicas)} ({porcentaje_unicas:.1f}% del total)\n"
        f"Longitud media de palabra: {longitud_media:.1f} letras\n"
        f"Palabra más larga: {p_larga}\n"
        f"Palabra más corta: {p_corta}\n"
        f"\nTOP 5 palabras más frecuentes:\n"
    )
    for i, (pal, cant) in enumerate(top_5, 1):
        res += f"{i}. {pal}: {cant} {'vez' if cant == 1 else 'veces'}\n"
    
    return res