import re
from collections import Counter

def obtener_texto():
    """Pide texto al usuario permitiendo múltiples líneas hasta una línea vacía."""
    print("Introduce el texto a analizar (presiona ENTER en una línea vacía para finalizar):")
    lineas = []
    while True:
        linea = input()
        if not linea:
            break
        lineas.append(linea)
    
    texto = "\n".join(lineas).strip()
    
    if not texto:
        print("\n⚠️ No se introdujo ningún texto.")
        return None
    
    print(f"\n--- Texto recibido ---\n{texto}\n----------------------")
    return texto

def limpiar_palabras(texto):
    """Limpia el texto y devuelve una lista de palabras normalizadas."""
    # Convertir a minúsculas y usar split() para ignorar múltiples espacios
    palabras = texto.lower().split()
    # Eliminar puntuación básica pegada a las palabras
    palabras_limpias = [re.sub(r'[^\w\s]', '', p) for p in palabras if p]
    return [p for p in palabras_limpias if p]

def contar_estadisticas_basicas(texto, palabras):
    """Calcula palabras, caracteres y longitudes."""
    total_palabras = len(palabras)
    caracteres_con_espacio = len(texto)
    caracteres_sin_espacio = len(texto.replace(" ", "").replace("\n", ""))
    
    # Longitud media
    longitud_media = sum(len(p) for p in palabras) / total_palabras if total_palabras > 0 else 0
    
    return total_palabras, caracteres_con_espacio, caracteres_sin_espacio, longitud_media

def analizar_estructura(texto):
    """Cuenta oraciones y párrafos usando regex."""
    # Oraciones: terminan en . ! o ?
    oraciones = re.findall(r'[^.!?]+[.!?]', texto)
    num_oraciones = len(oraciones) if oraciones else (1 if texto else 0)
    
    # Párrafos: separados por una o más líneas en blanco
    parrafos = [p for p in re.split(r'\n\s*\n', texto) if p.strip()]
    num_parrafos = len(parrafos)
    
    return num_oraciones, num_parrafos

def palabras_frecuentes(palabras, top_n=5):
    """Filtra stop words y devuelve el top N de palabras más comunes."""
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un'}
    palabras_filtradas = [p for p in palabras if p not in stop_words]
    
    contador = Counter(palabras_filtradas)
    return contador.most_common(top_n)

def analizar_vocabulario(palabras):
    """Identifica palabras únicas, extremos y porcentajes."""
    palabras_unicas = set(palabras)
    num_unicas = len(palabras_unicas)
    
    total = len(palabras)
    porcentaje_unicas = (num_unicas / total * 100) if total > 0 else 0
    
    if palabras:
        mas_larga = max(palabras, key=len)
        mas_corta = min(palabras, key=len)
    else:
        mas_larga = mas_corta = "N/A"
        
    return num_unicas, porcentaje_unicas, mas_larga, mas_corta

def mostrar_resultados(stats):
    """Muestra todas las estadísticas en un bloque formateado."""
    print("\n" + "="*40)
    print("📊 REPORTE DEL ANALIZADOR DE TEXTO")
    print("="*40)
    
    print(f"📝 ESTRUCTURA:")
    print(f"   - Párrafos: {stats['parrafos']}")
    print(f"   - Oraciones: {stats['oraciones']}")
    print(f"   - Palabras totales: {stats['total_palabras']}")
    print(f"   - Palabras únicas: {stats['unicas']} ({stats['porc_unicas']:.2f}%)")
    
    print(f"\n🔠 CARACTERES:")
    print(f"   - Con espacios: {stats['char_con']}")
    print(f"   - Sin espacios: {stats['char_sin']}")
    
    print(f"\n📏 DIMENSIONES:")
    print(f"   - Longitud media palabra: {stats['long_media']:.2f} letras")
    print(f"   - Palabra más larga: '{stats['larga']}'")
    print(f"   - Palabra más corta: '{stats['corta']}'")
    
    print(f"\n🔝 TOP 5 PALABRAS (sin conectores):")
    for word, count in stats['top_palabras']:
        print(f"   • {word}: {count} veces")
    print("="*40)

def main():
    texto = obtener_texto()
    if not texto:
        return

    palabras = limpiar_palabras(texto)
    
    # Recolección de datos
    total_p, c_con, c_sin, l_med = contar_estadisticas_basicas(texto, palabras)
    num_or, num_pa = analizar_estructura(texto)
    top_5 = palabras_frecuentes(palabras)
    u_cant, u_porc, p_larga, p_corta = analizar_vocabulario(palabras)
    
    # Empaquetado de resultados
    resultados = {
        'total_palabras': total_p, 'char_con': c_con, 'char_sin': c_sin,
        'long_media': l_med, 'oraciones': num_or, 'parrafos': num_pa,
        'top_palabras': top_5, 'unicas': u_cant, 'porc_unicas': u_porc,
        'larga': p_larga, 'corta': p_corta
    }
    
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()