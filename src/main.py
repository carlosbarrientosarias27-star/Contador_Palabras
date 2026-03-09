import os
import platform
from src.lector_archivos import leer_archivo, ejecutar_analisis_completo
# En la parte superior de main.py
from src.exportador import guardar_informe, preguntar_guardado # Agrega preguntar_guardado

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_bienvenida():
    """Muestra el banner principal del programa."""
    print("========================================")
    print("      SISTEMA DE ANÁLISIS DE TEXTO      ")
    print("========================================")
    print("Bienvenido/a. Seleccione una opción para comenzar.\n")

def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        print("1. Analizar texto manual (Ingreso por teclado)")
        print("2. Analizar archivo (.txt)")
        print("3. Salir")
        print("-" * 40)
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            limpiar_pantalla()
            print("--- ANALIZADOR MANUAL ---")
            texto_usuario = input("\nIngrese el texto que desea analizar:\n> ")
            if texto_usuario.strip():
                # Aquí llamarías a tus funciones de análisis (ej. contar_palabras(texto_usuario))
                print("\n[Simulación] Analizando texto manual...")
                print(f"Longitud del texto: {len(texto_usuario)} caracteres.")
            else:
                print("\n⚠️ No ingresaste ningún texto.")
            input("\nPresione Enter para volver al menú...")

        elif opcion == "2":
            limpiar_pantalla()
            print("--- ANALIZADOR DE ARCHIVOS ---")
            ruta = input("\nIngrese la ruta del archivo (ej: textos/ejemplo.txt):\n> ")
            # Ejecutamos la función que creamos en el commit anterior
            ejecutar_analisis_completo(ruta)
            input("\nPresione Enter para volver al menú...")

        elif opcion == "3":
            print("\n¡Gracias por usar el Analizador de Texto! Saliendo...")
            break

        else:
            print("\n❌ Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()