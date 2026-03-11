import os 
from datetime import datetime 

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo (Commit 9)."""
    os.system('cls' if os.name == 'nt' else 'clear') 

def guardar_resultados(informe, fuente):
    """
    Escribe los resultados en informe.txt con fecha y hora (Commit 8).
    """
    opcion = input("\n¿Guardar informe? (s/n): ").lower()
    if opcion == 's':
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("info_analisis/informe.txt", "w", encoding="utf-8") as f:
            f.write(f"INFORME - {ahora}\nFuente: {fuente}\n{informe}")
        print("Informe guardado en informe.txt")
