# Reto E08: Adivina el Número (Proyecto Integrador)

## La Misión

Es el momento de graduarte del Módulo 04. Construirás el sistema interactivo "Adivina el Número" implementando una arquitectura de componentes completamente desacoplados.

El sistema deberá instanciar un número objetivo (del 1 al 100) utilizando un PRNG seguro.
Posteriormente, entrará en un ciclo de ejecución continuo (*Game Loop*) que evaluará entradas por teclado.
Si el input es superior al objetivo, el sistema alertará: *"[INFO] Objetivo menor."*.
Si el input es inferior al objetivo, el sistema alertará: *"[INFO] Objetivo mayor."*.
Si la evaluación coincide exactamente, el sistema romperá el ciclo reportando: *"¡Calibración exacta! Logrado en X ciclos"* y liberará el proceso.

### Reglas de Oro Arquitectónicas:
1. **PROHIBIDO** desarrollar bloques lógicos en el Scope del `main()`. El orquestador principal debe reducirse a no más de 3 líneas invocando sub-rutinas.
2. Construye una rutina `int generarNumeroSecreto()` que instancie la entropía `<random>` fijada en memoria (`static mt19937`) para inyectar y retornar un número del 1 al 100.
3. Construye una rutina `int pedirIntento()` que maneje exclusivamente el flujo de I/O de la terminal.
4. Construye la rutina controladora `void jugarPartida(int objetivo)` que gestione el bucle `while(true)`, audite el conteo de iteraciones y aplique las condicionales lógicas comunicándose con el resto de los componentes.

### ⚙️ Instrucciones de Compilación

Compila tu solución desde la terminal con:
```bash
g++ -std=c++17 E08_AdivinaElNumero.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
