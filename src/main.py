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
    palabras = texto.split()
    return {
        "total_caracteres": len(texto),
        "total_palabras": len(palabras),
        "total_lineas": len(texto.splitlines()),
        "palabra_mas_larga": max(palabras, key=len) if palabras else "N/A"
    }

def menu_principal():
    # Definimos la ruta fija para el archivo de prueba
    ruta_ejemplo = "textos/ejemplo.txt" 
    
    # Crear el archivo textos/ejemplo.txt con un texto de prueba de varias líneas
    if not os.path.exists(ruta_ejemplo):
        crear_archivo_ejemplo(ruta_ejemplo)

    # Implementar bucle principal que mantenga el menú activo
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        # Crear menú principal con tres opciones
        print("1. Analizar texto manual")
        print("2. Analizar archivo (.txt)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        texto_a_analizar = ""
        fuente = ""

        if opcion == "1":
            texto_a_analizar = input("\nIngrese el texto a analizar: ")
            fuente = "Entrada Manual"
        
        elif opcion == "2":
            ruta_usuario = input("\nIngrese la ruta del archivo (ej: textos/ejemplo.txt): ")
            try:
                # Carga y lee un archivo .txt dado su ruta con manejo de errores
                texto_a_analizar = leer_archivo(ruta_usuario)
                fuente = ruta_usuario
            except FileNotFoundError:
                print("⚠️ Error: Archivo no encontrado.")
            except EOFError:
                print("⚠️ Error: El archivo está vacío.")
            except ValueError as e:
                print(f"⚠️ Error de formato: {e}")
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
        
        # Si hay texto cargado, procedemos al análisis y guardado
        if texto_a_analizar:
            resultados = realizar_analisis(texto_a_analizar)
            print("\n📊 ESTADÍSTICAS ENCONTRADAS:")
            for clave, valor in resultados.items():
                print(f"- {clave.replace('_', ' ').capitalize()}: {valor}")
            
            # Preguntar al usuario si quiere guardar el informe de análisis
            desea_guardar = input("\n¿Desea guardar el informe? (s/n): ").lower()
            if desea_guardar == 's':
                # Escribir todos los resultados en un archivo informe.txt (incluye fecha, hora y fuente)
                ruta_confirmada = guardar_informe(resultados, fuente)
                if ruta_confirmada:
                    # Confirmar al usuario la ruta donde se ha guardado el archivo
                    print(f"✅ Informe guardado con éxito en: {os.path.abspath(ruta_confirmada)}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()