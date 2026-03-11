import os
from datetime import datetime

def cargar_desde_archivo(ruta):
    """
    Lee el contenido de un archivo de texto en la ruta especificada.

    Retorna el contenido como string si el archivo existe y no está vacío, 
    de lo contrario retorna None. Maneja errores de lectura silenciosamente.
    """
    try:
        if not os.path.exists(ruta): 
            return None
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            return contenido if contenido.strip() else None
    except Exception:
        return None

def guardar_informe(informe, fuente):
    """
    Exporta el informe generado a un archivo físico en el directorio 'reportes'.

    Crea el directorio si no existe y genera un nombre de archivo único 
    basado en la fecha y hora actual (ISO 8601).
    """
    # 1. Definir el nombre de la carpeta
    carpeta_reportes = "reportes"
    
    # 2. Crear la carpeta si no existe para evitar FileNotFoundError
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)
        
    # 3. Generar el nombre del archivo y la ruta completa
    ahora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"informe_{ahora}.txt"
    ruta_Contador_palabras = os.path.join(carpeta_reportes, nombre_archivo)
    
    # 4. Escribir el archivo (Commit 8)
    try:
        with open(ruta_Contador_palabras, "w", encoding="utf-8") as f:
            f.write(f"INFORME GENERADO EL: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"FUENTE DE DATOS: {fuente}\n")
            f.write("-" * 30 + "\n")
            f.write(informe)
        print(f"\n[OK] Informe guardado exitosamente en: {ruta_Contador_palabras}")
    except Exception as e:
        print(f"\n[Error] No se pudo guardar el informe: {e}")