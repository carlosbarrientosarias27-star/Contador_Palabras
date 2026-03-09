import os
from datetime import datetime

def preparar_datos_reporte(num_palabras, car_con, car_sin, oraciones, parrafos, avanzadas, frecuentes):
    """
    Organiza todos los resultados del análisis en un diccionario estructurado.
    Esta función prepara el terreno para que el exportador reciba datos limpios.
    """
    return {
        "basicos": (num_palabras, car_con, car_sin),
        "estructuras": (oraciones, parrafos),
        "avanzadas": avanzadas,
        "frecuentes": frecuentes
    }

def obtener_info_tiempo():
    """Devuelve la fecha y hora formateada para el informe."""
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y %H:%M:%S")