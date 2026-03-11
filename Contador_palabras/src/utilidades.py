import os 
from datetime import datetime 

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo (Commit 9)."""
    os.system('cls' if os.name == 'nt' else 'clear') 

def guardar_resultados(informe, fuente):
    """
    Escribe los resultados en informe.txt dentro de info_analisis (Commit 8 corregido).
    """
    opcion = input("\n¿Guardar informe? (s/n): ").lower()
    if opcion == 's':
        # 1. Definir la ruta de la carpeta
        directorio = "info_analisis"
        
        # 2. Crear la carpeta si no existe para evitar el FileNotFoundError
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"Carpeta '{directorio}' creada automáticamente.")

        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. Construir la ruta completa del archivo
        ruta_archivo = os.path.join(directorio, "informe.txt")
        
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:
                f.write(f"INFORME - {ahora}\nFuente: {fuente}\n{informe}")
            print(f"Informe guardado con éxito en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")