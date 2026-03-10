import os
from datetime import datetime

def cargar_desde_archivo(ruta):
    try:
        if not os.path.exists(ruta): return None
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            return contenido if contenido.strip() else None
    except Exception:
        return None

def guardar_informe(informe, fuente):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("informe.txt", "w", encoding="utf-8") as f:
        f.write(f"INFORME - {ahora}\nFuente: {fuente}\n{informe}")