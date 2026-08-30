# Reto E07: El Colapso del PRNG

## La Misión

Estás desarrollando el algoritmo de *spawneo* (generación) para que el mapa de un videojuego instancie 3 enemigos pseudo-aleatorios cada vez que el jugador entra a una nueva zona. Los enemigos pueden poseer un nivel del 1 al 10.

El equipo de QA ha reportado un *bug* gravísimo: *"Cada vez que entramos a la zona, el sistema spawnea exactamente los mismos 3 enemigos. ¡Si aparece un enemigo de nivel 7, los otros dos también son de nivel 7!"*.

El desarrollador anterior creó la rutina delegada `generarNivelEnemigo()`, pero ignoró la arquitectura del hardware local (la entropía se lee demasiado rápido) y no proporcionó persistencia en memoria para el motor estocástico.

Tu misión es refactorizar la instanciación del motor para restaurar la distribución estadística.

### Reglas de Oro:
1. Inspecciona la función delegada `generarNivelEnemigo()`.
2. Localiza la instanciación del motor Mersenne Twister (`std::mt19937`).
3. Inyecta el modificador de memoria que le indica al compilador que aloje el motor de forma persistente, previniendo la destrucción y regeneración de su estado interno entre llamadas.

### ⚙️ Instrucciones de Compilación

Compila tu solución desde la terminal con:
```bash
g++ -std=c++17 E07_GeneradorDeSemillas.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
