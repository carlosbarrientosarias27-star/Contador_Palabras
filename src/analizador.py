import re
from collections import Counter

def analizar_conteo_basico(texto):
    """
    Commit 3: Cuenta palabras y caracteres.
    """
    # PROTECCIÓN: Si el texto está vacío, devolvemos ceros
    if not texto or not texto.strip():
        return 0, 0, 0
        
    palabras = texto.split()
    num_palabras = len(palabras)
    caracteres_con = len(texto)
    caracteres_sin = len(texto.replace(' ', ''))
    
    return num_palabras, caracteres_con, caracteres_sin

def analizar_estructuras(texto):
    """
    Commit 4: Cuenta oraciones y párrafos.
    """
    # PROTECCIÓN:
    if not texto or not texto.strip():
        return 0, 0

    oraciones = [o for o in re.split(r'[.!?]', texto) if o.strip()]
    parrafos = [p for p in texto.split('\n') if p.strip()]
    
    return len(oraciones), len(parrafos)

def obtener_frecuencia_palabras(texto, top_n=5):
    """
    Commit 5: Top palabras frecuentes.
    """
    # PROTECCIÓN:
    if not texto or not texto.strip():
        return []

    palabras = re.findall(r'\b\w+\b', texto.lower())
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un', 'es', 'con'}
    
    filtradas = [p for p in palabras if p not in stop_words]
    return Counter(filtradas).most_common(top_n)

def calcular_estadisticas_avanzadas(texto):
    """
    Commit 6: Estadísticas que podrían dar error de división por cero.
    """
    # PROTECCIÓN:
    if not texto or not texto.strip():
        return None

    palabras = re.findall(r'\b\w+\b', texto.lower())
    
    # Segunda protección interna por si re.findall no encuentra palabras
    if not palabras:
        return None

    palabras_unicas = set(palabras)
    total_palabras = len(palabras)
    
    # Aquí es donde el error de división por cero ocurriría sin la protección
    longitud_media = sum(len(p) for p in palabras) / total_palabras
    
    return {
        "unicas": len(palabras_unicas),
        "porcentaje_unicas": (len(palabras_unicas) / total_palabras) * 100,
        "media_longitud": longitud_media,
        "mas_larga": max(palabras, key=len)
    }