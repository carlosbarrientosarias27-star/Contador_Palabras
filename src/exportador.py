import os
from datetime import datetime

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