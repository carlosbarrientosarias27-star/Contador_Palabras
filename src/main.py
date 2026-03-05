"""
Módulo principal del Analizador de Texto.

Este script coordina la interfaz de usuario por terminal, gestiona el menú 
interactivo y orquestra el flujo entre la lectura, el análisis y la 
exportación de resultados.
"""

import os
import sys

# Antes: from lector import ...
# Ahora:
from src.lector import leer_terminal, leer_archivo
from src.analizador import (
    analizar_conteo_basico, 
    analizar_estructuras, 
    obtener_frecuencia_palabras, 
    calcular_estadisticas_avanzadas
)
from src.exportador import guardar_informe

def limpiar_pantalla():
    """
    Limpia la terminal del sistema para mejorar la legibilidad de la interfaz.
    
    Utiliza comandos del sistema operativo para detectar si se ejecuta en 
    Windows (cls) o sistemas basados en Unix (clear).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """
    Imprime el encabezado visual del programa en la consola.
    """
    print("==========================================")
    print("   CONTADOR DE PALABRAS DE UN TEXTO ||    ")
    print("==========================================\n")

def procesar_analisis(texto, fuente):
    """
    Ejecuta el pipeline de análisis protegiendo el flujo de errores de datos.
    """
    try:
        # 1. Análisis Básico (Commit 3)
        # Asegúrate de que analizador.py devuelva exactamente 3 valores
        res_basicos = analizar_conteo_basico(texto)
        num_palabras, car_con, car_sin = res_basicos

        # 2. Estructuras (Commit 4)
        num_oraciones, num_parrafos = analizar_estructuras(texto)

        # 3. Frecuencias y Avanzadas (Commits 5 y 6)
        frecuentes = obtener_frecuencia_palabras(texto)
        avanzadas = calcular_estadisticas_avanzadas(texto)

        # --- MOSTRAR RESULTADOS ---
        print("\n" + "="*30)
        print(f"ANÁLISIS: {fuente}")
        print("="*30)
        print(f"Palabras: {num_palabras}")
        print(f"Oraciones: {num_oraciones} | Párrafos: {num_parrafos}")
        print(f"Caracteres: {car_con} (con espacios) / {car_sin} (sin)")
        
        if avanzadas:
            print(f"Únicas: {avanzadas.get('unicas', 0)}")
            print(f"Promedio: {avanzadas.get('media_longitud', 0):.1f} letras")
            print(f"Más larga: {avanzadas.get('mas_larga', 'N/A')}")

        # --- GUARDAR (Commit 8) ---
        guardar = input("\n¿Exportar a informe.txt? (s/n): ").lower()
        if guardar == 's':
            datos_informe = {
                "basicos": (num_palabras, car_con, car_sin),
                "estructuras": (num_oraciones, num_parrafos),
                "frecuentes": frecuentes,
                "avanzadas": avanzadas
            }
            guardar_informe(datos_informe, fuente)

    except ValueError as e:
        print(f"\n[Error de Datos]: Revisa que analizador.py devuelva los valores correctos. {e}")
    except Exception as e:
        print(f"\n[Error Inesperado]: {e}")
        

def menu_principal():
    """
    Gestiona el ciclo de vida de la aplicación y la navegación del usuario.
    
    Mantiene un bucle activo que permite realizar múltiples análisis hasta 
     que el usuario decida salir del programa.
    """
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        print("¿Qué desea analizar?")
        print("1. Introducir texto manualmente")
        print("2. Cargar desde archivo .txt")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            texto = leer_terminal()
            if texto:
                procesar_analisis(texto, "Entrada manual")
        
        elif opcion == '2':
            ruta = input("Introduce la ruta (ej: textos/ejemplo.txt): ")
            texto = leer_archivo(ruta)
            if texto:
                procesar_analisis(texto, ruta)
        
        elif opcion == '3':
            print("Finalizando programa. ¡Gracias por usar el analizador!")
            break
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    menu_principal()