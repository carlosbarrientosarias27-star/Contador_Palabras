import os 
from datetime import datetime 

def limpiar_pantalla():
    """
    Limpia la consola del terminal según el sistema operativo actual.
    
    Ejecuta 'cls' para sistemas Windows (nt) y 'clear' para sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear') 

def guardar_resultados(informe, fuente):
    """
    Guarda el informe de análisis en un archivo físico si el usuario lo desea.

    Crea automáticamente el directorio 'info_analisis' si no existe y genera
    un archivo llamado 'informe.txt' con la fecha y la fuente del texto.

    Args:
        informe (str): El contenido de los resultados a guardar.
        fuente (str): La descripción del origen del texto (manual o ruta de archivo).
    """
    opcion = input("\n¿Guardar informe? (s/n): ").lower()
    if opcion == 's':
        directorio = "info_analisis"
        
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"Carpeta '{directorio}' creada automáticamente.")

        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ruta_archivo = os.path.join(directorio, "informe.txt")
        
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(f"INFORME - {ahora}\nFuente: {fuente}\n{informe}")
            print(f"Informe guardado con éxito en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")