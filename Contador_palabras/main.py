from src.utilidades import limpiar_pantalla, guardar_resultados
from src.entrada import capturar_texto_manual,cargar_desde_archivo 
from src.procesador import analizar_texto 

def main():
    """
    Bucle principal con el menú interactivo (Commit 9)[cite: 140, 142].
    """
    while True:
        limpiar_pantalla()
        print("|| CONTADOR DE PALABRAS DE UN TEXTO ||")
        print("1. Introducir texto manualmente")
        print("2. Cargar desde archivo .txt")
        print("3. Salir")
        
        opc = input("\nElige una opción: ")
        texto, fuente = None, ""

        if opc == '1':
            texto = capturar_texto_manual()
            fuente = "Entrada manual"
        elif opc == '2':
            ruta = input("Ruta del archivo (ej: textos/ejemplo.txt): ")
            texto = cargar_desde_archivo(ruta)
            fuente = ruta
        elif opc == '3':
            print("Saliendo del programa...")
            break
        
        if texto:
            resultado = analizar_texto(texto)
            print(resultado)
            guardar_resultados(resultado, fuente)
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()