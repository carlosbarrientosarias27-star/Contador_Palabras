import os
from datetime import datetime

def generar_informe(datos_analisis, fuente="Manual"):
    """
    Guarda los resultados del análisis en un archivo .txt con metadatos.
    
    :param datos_analisis: Diccionario con los resultados (conteo, palabras, etc.)
    :param fuente: Origen del texto (nombre del archivo o 'Entrada Manual')
    """
    ahora = datetime.now()
    fecha_str = ahora.strftime("%d/%m/%Y %H:%M:%S")
    nombre_texto = f"informe_{ahora.strftime('%Y%m%d_%H%M%S')}.txt"
    ruta_salida = os.path.join("informes", nombre_texto)

    # Crear carpeta de informes si no existe
    os.makedirs("informes", exist_ok=True)

    try:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            f.write("========================================\n")
            f.write("      INFORME DE ANÁLISIS DE TEXTO      \n")
            f.write("========================================\n\n")
            f.write(f"📅 Fecha y Hora: {fecha_str}\n")
            f.write(f"📂 Fuente: {fuente}\n")
            f.write("-" * 40 + "\n")
            
            # Escribir las estadísticas dinámicamente
            for clave, valor in datos_analisis.items():
                f.write(f"🔹 {clave.replace('_', ' ').capitalize()}: {valor}\n")
            
            f.write("\n" + "=" * 40 + "\n")
            f.write("Fin del informe.\n")

        print(f"\n✅ Informe guardado con éxito en: {ruta_salida}")
        return ruta_salida

    except Exception as e:
        print(f"❌ Error al guardar el informe: {e}")
        return None

def preguntar_guardado(datos, fuente="Manual"):
    """Consulta al usuario si desea exportar los resultados."""
    opcion = input("\n¿Desea guardar el informe de análisis en un archivo? (s/n): ").lower()
    if opcion == 's':
        generar_informe(datos, fuente)
    else:
        print("ℹ️ Informe no guardado.")