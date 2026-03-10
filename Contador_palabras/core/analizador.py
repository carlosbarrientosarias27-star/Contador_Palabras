import re
from collections import Counter

def analizar_texto(texto):
    """
    Realiza un análisis estadístico exhaustivo del texto proporcionado.

    Calcula métricas como conteo de oraciones, párrafos, palabras totales, 
    palabras únicas, longitud media y las palabras más frecuentes (Top 5).
    Maneja casos de error como textos vacíos o compuestos solo por números.
    """
    # 1. Limpieza y Normalización
    palabras_totales = texto.split()
    total_palabras = len(palabras_totales)
    
    # Extraer solo palabras (letras), ignorando números puros
    palabras_limpias = re.findall(r'\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b', texto.lower())
    
    # 2. Manejo de Texto Vacío o Solo Números
    if total_palabras == 0 or not palabras_limpias:
        return {
            "oraciones": 0, "parrafos": 0, "total": total_palabras,
            "unicas": 0, "porcentaje_unicas": 0.0, "media": 0.0,
            "p_larga": "-", "top": []
        }

    # 3. Estadísticas (Lógica normal)
    oraciones = [o for o in re.split(r'[.!?]+', texto) if o.strip()]
    parrafos = [p for p in texto.split('\n\n') if p.strip()]
    
    unicas = set(palabras_limpias)
    longitud_media = sum(len(p) for p in palabras_limpias) / len(palabras_limpias)
    p_larga = max(palabras_limpias, key=len)
    
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un'}
    filtradas = [p for p in palabras_limpias if p not in stop_words]
    top_5 = Counter(filtradas).most_common(5)

    return {
        "oraciones": len(oraciones),
        "parrafos": len(parrafos),
        "total": total_palabras,
        "unicas": len(unicas),
        "porcentaje_unicas": (len(unicas) / total_palabras) * 100,
        "media": longitud_media,
        "p_larga": p_larga,
        "top": top_5
    }