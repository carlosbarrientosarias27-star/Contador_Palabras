# 🧪 Pruebas de Casos de Borde 

## 1. Texto vacío ("")
Es el origen de muchísimos errores de tipo NullPointerException o fallos de segmentación.

El riesgo: Si tu lógica intenta acceder al primer índice de la cadena (como texto[0]) y la cadena no tiene nada, el programa colapsará.

La prueba: ¿Qué hace tu función si no le pasas nada? Debería retornar un error controlado o un valor neutro, pero nunca cerrarse inesperadamente.

## 2. Un solo carácter ("a")
A veces los algoritmos funcionan bien con grupos de datos, pero fallan en la unidad mínima.

El riesgo: Muchos bucles (como los for o while) están diseñados pensando en "empezar en 0 y terminar en N-1". Si la longitud es 1, algunos límites mal configurados podrían saltarse el proceso por completo o intentar buscar un "siguiente elemento" que no existe.

## 3. Texto con solo números o símbolos ("12345" / "$%&#")
Si tu función espera procesar lenguaje humano, los caracteres no alfabéticos son el caso edge perfecto.

El riesgo: Si usas funciones de conversión de mayúsculas/minúsculas o intentas calcular una "puntuación" basada en letras, un número podría devolver un valor inesperado o romper la lógica de validación.