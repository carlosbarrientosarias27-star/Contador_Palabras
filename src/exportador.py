import os
from datetime import datetime  # Importamos la clase directamente

   
    # ... resto del código igual ...
def generar_informe_archivo(estadisticas, top_palabras, fuente="Entrada manual"):
    """
    Crea un archivo llamado informe.txt con todos los datos del análisis.
    """
    ahora = datetime.now()
    fecha_formateada = ahora.strftime("%d/%m/%Y")
    hora_formateada = ahora.strftime("%H:%M:%S")
    
    nombre_archivo = "informe.txt"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            # Encabezado
            f.write("="*50 + "\n")
            f.write("       INFORME DETALLADO DE ANÁLISIS DE TEXTO\n")
            f.write("="*50 + "\n")
            f.write(f"Fecha: {fecha_formateada}\n")
            f.write(f"Hora:  {hora_formateada}\n")
            f.write(f"Fuente: {fuente}\n")
            f.write("-" * 50 + "\n\n")

            # Estadísticas de Estructura
            f.write("1. ESTRUCTURA GENERAL\n")
            f.write(f"   - Párrafos:           {estadisticas['parrafos']}\n")
            f.write(f"   - Oraciones:          {estadisticas['oraciones']}\n")
            f.write(f"   - Palabras totales:   {estadisticas['total_palabras']}\n\n")

            # Diversidad y Métricas
            f.write("2. MÉTRICAS DE VOCABULARIO\n")
            f.write(f"   - Palabras únicas:    {estadisticas['unicas']}\n")
            f.write(f"   - Densidad léxica:    {estadisticas['densidad']:.2f}%\n")
            f.write(f"   - Longitud media:     {estadisticas['long_media']:.2f} caracteres\n")
            f.write(f"   - Palabra más larga:  '{estadisticas['p_larga']}'\n")
            f.write(f"   - Palabra más corta:  '{estadisticas['p_corta']}'\n\n")

            # Frecuencia
            f.write("3. TOP 5 PALABRAS MÁS FRECUENTES\n")
            for i, (pal, frec) in enumerate(top_palabras, 1):
                f.write(f"   {i}. {pal}: {frec} veces\n")
            
            f.write("\n" + "="*50 + "\n")
            f.write("             FIN DEL INFORME\n")

        # Retornar la ruta absoluta para confirmar al usuario
        return os.path.abspath(nombre_archivo)
    
    except Exception as e:
        return f"Error al guardar el archivo: {e}" 
    
import os
from datetime import datetime  # Importación correcta: Clase desde el módulo

def guardar_informe(resultados, fuente):
    """
    Crea un archivo llamado informe.txt con todos los datos del análisis.
    Incluye fecha, hora, fuente y estadísticas completas.
    """
    # Uso correcto de la clase datetime
    ahora = datetime.now() 
    fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_archivo = "informe.txt"
    
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("==========================================\n")
            f.write("      INFORME DE ANÁLISIS DE TEXTO        \n")
            f.write("==========================================\n\n")
            
            # 1. Metadatos (Requerido por Commit 8)
            f.write(f"Fecha y hora: {fecha_formateada}\n")
            f.write(f"Fuente del texto: {fuente}\n")
            f.write("-" * 42 + "\n\n")
            
            # 2. Extracción de datos desde el diccionario (Commit 8)
            basicos = resultados.get("basicos", (0, 0, 0))
            estructuras = resultados.get("estructuras", (0, 0))
            avanzadas = resultados.get("avanzadas", {})
            frecuentes = resultados.get("frecuentes", [])
            
            # 3. Escritura de estadísticas
            f.write(f"Palabras totales: {basicos[0]}\n")
            f.write(f"Caracteres (con espacios): {basicos[1]}\n")
            f.write(f"Caracteres (sin espacios): {basicos[2]}\n")
            f.write(f"Oraciones: {estructuras[0]} | Párrafos: {estructuras[1]}\n\n")
            
            if avanzadas:
                f.write("ESTADÍSTICAS AVANZADAS:\n")
                f.write(f"- Palabras únicas: {avanzadas.get('unicas', 0)} ({avanzadas.get('porcentaje_unicas', 0):.1f}%)\n")
                f.write(f"- Longitud media: {avanzadas.get('media_longitud', 0):.1f} letras\n")
                f.write(f"- Palabra más larga: {avanzadas.get('mas_larga', 'N/A')}\n\n")
            
            if frecuentes:
                f.write("TOP 5 PALABRAS MÁS FRECUENTES:\n")
                for i, (palabra, cuenta) in enumerate(frecuentes, 1):
                    f.write(f"{i}. {palabra}: {cuenta} vez/veces\n")
            
            f.write("\n" + "=" * 42 + "\n")
            
        # 4. Confirmación de ruta absoluta (Requerido por Commit 8)
        ruta_absoluta = os.path.abspath(nombre_archivo)
        print(f"\n[OK] Informe guardado con éxito en: {ruta_absoluta}")
        
    except Exception as e:
        print(f"\n[Error] No se pudo guardar el informe: {e}")