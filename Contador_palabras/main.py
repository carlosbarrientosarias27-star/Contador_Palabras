from utils.interfaz import limpiar_pantalla, capturar_texto_manual, formatear_informe
from utils.archivos import cargar_desde_archivo, guardar_informe
from core.analizador import analizar_texto


def formatear_informe(stats):
    """Convierte el diccionario de estadísticas en el texto visual."""
    res = (
        f"\n{'='*30}\n RESULTADOS DEL ANÁLISIS\n{'='*30}\n"
        f"Texto: {stats['oraciones']} oraciones | {stats['parrafos']} párrafos\n"
        f"Palabras totales: {stats['total']}\n"
        f"Palabras únicas: {stats['unicas']} ({stats['porcentaje_unicas']:.1f}%)\n"
        f"Longitud media: {stats['media']:.1f} letras\n"
        f"Palabra más larga: {stats['p_larga']}\n"
        f"\nTOP 5 palabras:\n"
    )
    for i, (pal, cant) in enumerate(stats['top'], 1):
        res += f"{i}. {pal}: {cant} {'vez' if cant == 1 else 'veces'}\n"
    return res


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