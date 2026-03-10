import os
from datetime import datetime

def cargar_desde_archivo(ruta):
    """
    Carga y lee un archivo .txt manejando errores de ruta (Commit 7).
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
    Guarda el informe en la carpeta 'reportes' con marca de tiempo.
    """
    # 1. Definir el nombre de la carpeta
    carpeta_reportes = "reportes"
    
    # 2. Crear la carpeta si no existe para evitar FileNotFoundError
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)
        
    # 3. Generar el nombre del archivo y la ruta completa
    ahora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"informe_{ahora}.txt"
    ruta_destino = os.path.join(carpeta_reportes, nombre_archivo)
    
    # 4. Escribir el archivo (Commit 8)
    try:
        with open(ruta_destino, "w", encoding="utf-8") as f:
            f.write(f"INFORME GENERADO EL: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"FUENTE DE DATOS: {fuente}\n")
            f.write("-" * 30 + "\n")
            f.write(informe)
        print(f"\n[OK] Informe guardado exitosamente en: {ruta_destino}")
    except Exception as e:
        print(f"\n[Error] No se pudo guardar el informe: {e}")