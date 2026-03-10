import sys
import os

# Fuerza a Python a buscar módulos en el directorio actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ahora las importaciones funcionarán correctamente
from utils.interfaz import limpiar_pantalla, capturar_texto_manual, formatear_informe 
from utils.archivos import cargar_desde_archivo, guardar_informe
from core.analizador import analizar_texto

def main():
    while True:
        limpiar_pantalla()
        print("|| CONTADOR DE PALABRAS OPTIMIZADO ||")
        print("1. Manual | 2. Archivo | 3. Salir")
        
        opc = input("\nOpción: ")
        texto, fuente = None, ""

        if opc == '1':
            texto = capturar_texto_manual()
            fuente = "Entrada manual"
        elif opc == '2':
            ruta = input("Ruta: ")
            texto = cargar_desde_archivo(ruta)
            fuente = ruta
        elif opc == '3': break
        
        if texto:
            stats = analizar_texto(texto)
            informe_texto = formatear_informe(stats)
            print(informe_texto)
            
            if input("¿Guardar? (s/n): ").lower() == 's':
                guardar_informe(informe_texto, fuente)
            input("\nPresiona Enter...")

if __name__ == "__main__":
    main()