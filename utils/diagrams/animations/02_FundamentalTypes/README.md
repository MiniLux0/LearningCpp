# Animaciones del Módulo 02 - Fundamental Types

Este directorio contiene los scripts de Manim para generar los recursos visuales del módulo 02.
Siguiendo las convenciones del repositorio, todos los scripts aquí heredan de `BaseLearningScene` y se exportan automáticamente a `02_FundamentalTypes/theory/assets/`.

### Scripts

- `l01_memoria_tipos.py`: Genera un PNG mostrando cuánto espacio físico en RAM (cuadrícula) ocupan `char`, `int` y `double`.
- `l02_narrowing_conversion.py`: Genera un GIF animado mostrando cómo el operador `=` recorta silenciosamente un decimal, mientras que la inicialización uniforme `{}` actúa como un escudo protector (error de compilación).
- `l03_precedencia_operadores.py`: Genera un PNG contrastando visualmente el orden de evaluación matemática con y sin paréntesis.

### Ejecución

Para generar los assets, ejecuta cualquiera de los scripts directamente con Python:
```powershell
python l01_memoria_tipos.py
```
El bloque de ejecución al final de cada archivo se encargará del renderizado y compresión/copia correctos.
