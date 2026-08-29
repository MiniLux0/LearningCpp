# Reto E02: La Calculadora de Área

## La Misión

Trabajas para una compañía de arquitectura. Recientemente, el equipo de backend creó una función `calcularArea` para obtener los metros cuadrados de una pared dados su base y su altura.

La regla de negocio (lógica) estipula:
- Si la base y la altura son válidas (mayores a cero), devuelve la multiplicación de ambas.
- Si cualquiera de los dos parámetros es inválido (cero o negativo), el sistema debe abortar el cálculo y devolver `0` como medida de seguridad.

El problema es que cuando el sistema procesa planos con errores (valores negativos), la función en lugar de devolver `0`, está inyectando números basura gigantescos, provocando un *Undefined Behavior* que corrompe toda la renderización 3D.

Tu misión es refactorizar la función `calcularArea` para cubrir las fugas.

### Reglas de Oro:
1. Inspecciona la función y encuentra el camino lógico (la rama de decisión) que carece de un bloque `return`.
2. Asegúrate de que **absolutamente todos** los caminos lógicos retornen explícitamente un valor tipo `int` al hilo principal (`main`).
