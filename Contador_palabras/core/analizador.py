import re
from collections import Counter

def analizar_texto(texto):
    """Realiza el análisis estadístico del texto (SRP)."""
    palabras_totales = texto.split() 
    total_palabras = len(palabras_totales)
    
    # Oraciones y Párrafos
    oraciones = [o for o in re.split(r'[.!?]+', texto) if o.strip()]
    parrafos = [p for p in texto.split('\n\n') if p.strip()]

    # Palabras frecuentes y limpieza
    palabras_limpias = re.findall(r'\b\w+\b', texto.lower())
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un'}
    filtradas = [p for p in palabras_limpias if p not in stop_words]
    top_5 = Counter(filtradas).most_common(5)

    # Estadísticas avanzadas
    unicas = set(palabras_limpias)
    longitud_media = sum(len(p) for p in palabras_limpias) / len(palabras_limpias) if palabras_limpias else 0
    
    return {
        "oraciones": len(oraciones),
        "parrafos": len(parrafos),
        "total": total_palabras,
        "unicas": len(unicas),
        "media": longitud_media,
        "top": top_5
    }
