import os
from lector_archivos import leer_archivo, crear_archivo_ejemplo
from exportador import guardar_informe

def limpiar_pantalla():
    """Limpiar la terminal entre operaciones con os.system()"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Mostrar pantalla de bienvenida con el título del programa al iniciar"""
    print("========================================")
    print("      ANALIZADOR DE TEXTO PRO v1.0     ")
    print("========================================\n")

def realizar_analisis(texto):
    """Aplica funciones de análisis al texto del archivo o manual"""
    # Caso Edge: Texto que solo contiene espacios, tabs o saltos de línea
    if not texto or not texto.strip():
        return {
            "total_caracteres": len(texto),
            "total_palabras": 0,
            "total_lineas": 0,
            "palabra_mas_larga": "N/A"
        }

    palabras = texto.split()
    
    # Caso Edge: Limpiar puntuación para que "Hola!" cuente como "Hola" (4 caracteres)
    # Esto evita que los signos influyan en cuál es la palabra más larga.
    palabras_limpias = [p.strip(".,!?;:()[]\"'") for p in palabras]
    # Filtramos por si al limpiar quedaron strings vacíos (ej: el texto era solo "!!!")
    palabras_reales = [p for p in palabras_limpias if p]

    return {
        "total_caracteres": len(texto),
        "total_palabras": len(palabras),
        "total_lineas": len(texto.splitlines()),
        "palabra_mas_larga": max(palabras_reales, key=len) if palabras_reales else "N/A"
    }

def menu_principal():
    ruta_ejemplo = "textos/ejemplo.txt" 
    
    # Asegurar que el directorio existe antes de intentar crear el archivo
    if not os.path.exists("textos"):
        os.makedirs("textos")

    if not os.path.exists(ruta_ejemplo):
        crear_archivo_ejemplo(ruta_ejemplo)

    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        print("1. Analizar texto manual")
        print("2. Analizar archivo (.txt)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        texto_a_analizar = ""
        fuente = ""

        if opcion == "1":
            entrada = input("\nIngrese el texto a analizar: ")
            # Caso Edge: Evitar procesar si el usuario solo da Enter o espacios
            if not entrada.strip():
                print("⚠️ Error: No se ingresó texto válido para analizar.")
            else:
                texto_a_analizar = entrada
                fuente = "Entrada Manual"
        
        elif opcion == "2":
            ruta_usuario = input("\nIngrese la ruta del archivo (ej: textos/ejemplo.txt): ")
            try:
                texto_a_analizar = leer_archivo(ruta_usuario)
                # Caso Edge: El archivo existe pero está totalmente vacío o solo tiene espacios
                if not texto_a_analizar or not texto_a_analizar.strip():
                    print("⚠️ El archivo seleccionado está vacío.")
                    texto_a_analizar = "" # Reset para no procesar
                else:
                    fuente = ruta_usuario
            except FileNotFoundError:
                print("⚠️ Error: Archivo no encontrado.")
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")
        
        if texto_a_analizar:
            resultados = realizar_analisis(texto_a_analizar)
            print("\n📊 ESTADÍSTICAS ENCONTRADAS:")
            for clave, valor in resultados.items():
                print(f"- {clave.replace('_', ' ').capitalize()}: {valor}")
            
            desea_guardar = input("\n¿Desea guardar el informe? (s/n): ").lower()
            if desea_guardar == 's':
                ruta_confirmada = guardar_informe(resultados, fuente)
                if ruta_confirmada:
                    print(f"✅ Informe guardado con éxito en: {os.path.abspath(ruta_confirmada)}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()