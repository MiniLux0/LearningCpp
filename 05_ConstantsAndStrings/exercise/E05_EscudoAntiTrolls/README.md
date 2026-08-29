# E05: Escudo Anti-Trolls

## Contexto
Eres el desarrollador de interfaz para la pantalla táctil de un nuevo modelo de cajero automático. El sistema solicita al usuario su Número de Identificación Personal (PIN) que debe ser estrictamente un número entero de 4 dígitos.

Lamentablemente, algunos usuarios rebeldes descubrieron que al escribir letras (como "Mil") en lugar de números, el flujo de entrada (buffer) de lectura colapsa. Al carecer de protecciones defensivas, el cajero entra en un bucle infinito de la muerte, sobrecalienta su procesador y requiere que un técnico viaje al banco para reiniciar el equipo físicamente.

## Tu Misión
Abre el archivo `E05_EscudoAntiTrolls.cpp`.
1. Detecta si el flujo de entrada (buffer) colapsó usando el medidor de fallos interno del sistema.
2. Si detectas un error, apaga inmediatamente la alarma de fallo para que la lectura pueda reiniciarse.
3. Desatasca el flujo de entrada (buffer) lavando la basura estancada (indicando descartar hasta 10000 caracteres o hasta hallar el salto de línea `\n`).
