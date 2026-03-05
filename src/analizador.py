def contar_palabras(texto):
    """
    Cuenta el número total de palabras ignorando espacios múltiples.
    split() sin argumentos divide por cualquier espacio en blanco y elimina vacíos.
    """
    palabras = texto.split()
    return len(palabras)

def contar_caracteres(texto):
    """
    Retorna una tupla con (total_con_espacios, total_sin_espacios).
    """
    con_espacios = len(texto)
    sin_espacios = len(texto.replace(" ", ""))
    return con_espacios, sin_espacios 

import re

def contar_oraciones(texto):
    """
    Cuenta oraciones usando expresiones regulares.
    Busca puntos, signos de exclamación o interrogación (. ! ?)
    """
    # El patrón [.!?] busca cualquiera de esos tres caracteres
    oraciones = re.findall(r'[.!?]+', texto)
    return len(oraciones)

def contar_parrafos(texto):
    """
    Cuenta párrafos separados por una o más líneas en blanco.
    Busca secuencias de dos o más saltos de línea (\n\n+).
    """
    # Eliminamos espacios al inicio y final, luego dividimos por 2 o más saltos de línea
    if not texto.strip():
        return 0
    parrafos = re.split(r'\n\s*\n', texto.strip())
    return len(parrafos)

import re
from collections import Counter

# Lista de palabras a ignorar (stop words)
PALABRAS_VACIAS = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un', 'los', 'las', 'con', 'por'}

def palabras_mas_frecuentes(texto, n=5):
    """
    Limpia el texto, filtra palabras vacías y devuelve las N más comunes.
    """
    # 1. Convertir a minúsculas y extraer solo palabras (letras/números)
    # El patrón \w+ extrae palabras ignorando signos de puntuación
    todas_las_palabras = re.findall(r'\w+', texto.lower())
    
    # 2. Filtrar las palabras que están en nuestra lista de "vacías"
    palabras_filtradas = [p for p in todas_las_palabras if p not in PALABRAS_VACIAS]
    
    # 3. Usar Counter para obtener el ranking
    contador = Counter(palabras_filtradas)
    return contador.most_common(n)

def obtener_metricas_avanzadas(texto):
    """
    Calcula longitud media, palabras únicas, porcentajes y extremos.
    """
    # 1. Obtener lista de palabras limpias (sin puntuación y en minúsculas)
    palabras = re.findall(r'\w+', texto.lower())
    
    if not palabras:
        return None

    # 2. Palabras únicas (usando un set para eliminar duplicados)
    palabras_unicas = set(palabras)
    total_palabras = len(palabras)
    num_unicas = len(palabras_unicas)
    
    # 3. Cálculos de longitud
    # La longitud media es la suma de caracteres de todas las palabras / total de palabras
    longitud_media = sum(len(p) for p in palabras) / total_palabras
    
    # 4. Palabras más larga y corta (usando la función min/max con clave de longitud)
    palabra_larga = max(palabras, key=len)
    palabra_corta = min(palabras, key=len)
    
    # 5. Porcentaje de palabras únicas
    porcentaje_unicas = (num_unicas / total_palabras) * 100

    return {
        "longitud_media": longitud_media,
        "num_unicas": num_unicas,
        "porcentaje_unicas": porcentaje_unicas,
        "palabra_larga": palabra_larga,
        "palabra_corta": palabra_corta
    }