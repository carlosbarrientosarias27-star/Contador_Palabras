# 🧪 Pruebas de Casos de Borde 

## 1. Texto Vacío
Qué ingresar: Simplemente presiona Enter cuando el programa pida el texto.

Resultado esperado:

- total_caracteres: 0

- total_palabras: 0

- total_lineas: 0

- palabra_mas_larga: "N/A" (Gracias a tu condición if palabras else "N/A").

Observación: Tu código ya maneja esto correctamente para evitar un ValueError al intentar calcular el max() de una lista vacía.

## 2. Un solo carácter 
Qué ingresar: Una sola letra (ej: a) o un símbolo (ej: @).

Resultado esperado:

- total_caracteres: 1

- total_palabras: 1

- total_lineas: 1

- palabra_mas_larga: El carácter ingresado.

## 3. Texto con solo números 
Qué ingresar: 123 4567 89

Resultado esperado:

- total_caracteres: 11 (contando espacios).

- total_palabras: 3

- palabra_mas_larga: 4567

Nota técnica: En Python, los números en un string se tratan como caracteres alfanuméricos. El método .split() no diferencia entre letras y números, por lo que los contará como "palabras" igualmente.