# Reto E06: Refactorización Arquitectónica

## La Misión

Has heredado el código base del menú transaccional de un famoso videojuego RPG.
Desafortunadamente, el desarrollador anterior acopló las 40 líneas de código del renderizado del menú, la petición de entrada de datos y el flujo de salida, **todo comprimido dentro del Scope del `main()`**.

Leer y mantener el código resulta arquitectónicamente insostenible (Código Espagueti).

Tu misión es aplicar el principio de *Extracción de Rutinas* para modularizar el bloque monolítico en sub-rutinas delegadas especializadas.

### Reglas de Oro:
1. Extrae el código definiendo tres funciones nuevas por encima del `main()`:
   * `void dibujarMenu()` (Efecto Secundario: Exclusiva para el output de consola).
   * `int pedirOpcion()` (Flujo de I/O: Captura la entrada del usuario y la inyecta como retorno).
   * `void ejecutarSalida()` (Efecto Secundario: Exclusiva para la rutina de finalización).
2. Refactoriza el `main()` eliminando las líneas acopladas y delegando el flujo invocando a tus nuevas sub-rutinas.
3. Al finalizar, tu `main()` debería poseer un alto nivel de abstracción y leerse como un flujo auto-documentado de menos de 15 líneas.
