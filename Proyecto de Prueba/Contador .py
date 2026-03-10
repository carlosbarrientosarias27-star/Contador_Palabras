import re
import os
from collections import Counter
from datetime import datetime

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo (Commit 9)[cite: 141]."""
    os.system('cls' if os.name == 'nt' else 'clear')

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

def analizar_texto(texto):
    """
    Realiza el análisis estadístico del texto aplicando SRP (Commits 3, 4, 5, 6 y 10).
    """
    # 1. Palabras y Caracteres (Commit 3) [cite: 67, 68]
    palabras_totales = texto.split() # Ignora espacios múltiples automáticamente [cite: 69]
    total_palabras = len(palabras_totales)
    caracteres_con = len(texto)
    caracteres_sin = len(texto.replace(" ", "").replace("\n", ""))

    # 2. Oraciones y Párrafos (Commit 4) [cite: 78, 79]
    # Usamos re para detectar múltiples delimitadores . ! ? (Commit 4) 
    oraciones = [o for o in re.split(r'[.!?]+', texto) if o.strip()]
    parrafos = [p for p in texto.split('\n\n') if p.strip()]

    # 3. Palabras frecuentes (Commit 5) [cite: 90, 94]
    # Normalización a minúsculas y limpieza de símbolos
    palabras_limpias = re.findall(r'\b\w+\b', texto.lower())
    stop_words = {'el', 'la', 'de', 'que', 'y', 'en', 'a', 'un'} # Filtrado (Commit 5) [cite: 94]
    filtradas = [p for p in palabras_limpias if p not in stop_words]
    top_5 = Counter(filtradas).most_common(5)

    # 4. Estadísticas Avanzadas (Commit 6) [cite: 104]
    unicas = set(palabras_limpias)
    longitud_media = sum(len(p) for p in palabras_limpias) / len(palabras_limpias) if palabras_limpias else 0
    p_larga = max(palabras_limpias, key=len) if palabras_limpias else "-"
    p_corta = min(palabras_limpias, key=len) if palabras_limpias else "-"

    # Construcción del informe formateado (Commit 6) [cite: 105]
    res = (
        f"\n{'='*30}\n RESULTADOS DEL ANÁLISIS\n{'='*30}\n"
        f"Texto analizado: {len(oraciones)} oraciones | {len(parrafos)} párrafos\n"
        f"Palabras totales: {total_palabras}\n"
        f"Caracteres (con espacios): {caracteres_con}\n"
        f"Caracteres (sin espacios): {caracteres_sin}\n"
        f"Palabras únicas: {len(unicas)} ({ (len(unicas)/total_palabras)*100:.1f}% del total)\n"
        f"Longitud media de palabra: {longitud_media:.1f} letras\n"
        f"Palabra más larga: {p_larga}\n"
        f"Palabra más corta: {p_corta}\n"
        f"\nTOP 5 palabras más frecuentes:\n"
    )
    for i, (pal, cant) in enumerate(top_5, 1):
        res += f"{i}. {pal}: {cant} {'vez' if cant == 1 else 'veces'}\n"
    
    return res

def guardar_resultados(informe, fuente):
    """
    Escribe los resultados en informe.txt con fecha y hora (Commit 8)[cite: 130, 131].
    """
    opcion = input("\n¿Guardar informe? (s/n): ").lower()
    if opcion == 's':
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("informe.txt", "w", encoding="utf-8") as f:
            f.write(f"INFORME - {ahora}\nFuente: {fuente}\n{informe}")
        print("Informe guardado en informe.txt")

def main():
    """
    Bucle principal con el menú interactivo (Commit 9)[cite: 140, 142].
    """
    while True:
        limpiar_pantalla()
        print("|| CONTADOR DE PALABRAS DE UN TEXTO ||")
        print("1. Introducir texto manualmente")
        print("2. Cargar desde archivo .txt")
        print("3. Salir")
        
        opc = input("\nElige una opción: ")
        texto, fuente = None, ""

        if opc == '1':
            texto = capturar_texto_manual()
            fuente = "Entrada manual"
        elif opc == '2':
            ruta = input("Ruta del archivo (ej: textos/ejemplo.txt): ")
            texto = cargar_desde_archivo(ruta)
            fuente = ruta
        elif opc == '3':
            print("Saliendo del programa...")
            break
        
        if texto:
            resultado = analizar_texto(texto)
            print(resultado)
            guardar_resultados(resultado, fuente)
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()