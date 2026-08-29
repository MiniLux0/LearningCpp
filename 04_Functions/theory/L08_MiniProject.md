# L08: Mini-Proyecto - El Game Loop Modular

¡Felicidades por llegar al final del Módulo 04! Has aprendido a encapsular lógica en rutinas delegadas (Funciones), a proteger el estado temporal (Scope), a transferir datos de forma segura (Pass-by-value) y a instanciar arquitecturas caóticas persistentes (`<random>`).

En este proyecto integrador, combinarás este conocimiento arquitectónico con las estructuras de control (`while`, `if/else`) del Módulo 03 para desarrollar tu primer sistema interactivo.

---

## La Arquitectura del Game Loop

Ningún sistema interactivo escalable acopla su lógica en el Scope principal. Por el contrario, se basan en un ciclo de vida, conocido en la industria como *Game Loop*, coordinado por un orquestador modular.

Para el sistema "Adivina el Número", la arquitectura debe leerse mediante llamadas de alto nivel:

1. **Configuración (`generarObjetivo`):** El motor PRNG es instanciado y provee la semilla objetivo.
2. **Ciclo de Ejecución (`iniciarLoopDeJuego`):** Un bucle indefinido que, en cada frame lógico:
   * Solicita el input del usuario en la terminal (`pedirIntento`).
   * Evalúa el diferencial lógico (si es mayor, menor, o idéntico).
   * Solo aborta el bucle (`break` o `return`) si se cumple la condición de victoria.
3. **Cierre:** El sistema retorna el control al orquestador para finalizar el proceso.

---

## Intercepción de Bucles mediante Retorno Temprano

Una técnica de arquitectura avanzada: Si instancias un bucle infinito `while (true)` dentro de una sub-rutina, y la condición de victoria lógica se satisface, puedes utilizar la instrucción `return` como mecanismo de escape en lugar de `break`.

Como vimos en la L02, `return` destruye inmediatamente el Scope local actual. Esto implica que **abortará instantáneamente cualquier bucle que estuviera ejecutándose en ese nivel de memoria**, devolviendo el control al hilo invocador.

```cpp
void buscarArchivo() {
    while (true) {
        int codigo_estado{escanearDisco()};
        
        if (codigo_estado == 1) { 
            std::cout << "[INFO] Archivo localizado.\n";
            return; // ¡Destruye el bucle y el Scope de la función al instante!
        }
    }
}
```

---

> 🧪 **Laboratorio:** Observa la limpieza visual del esqueleto arquitectónico de un sistema antes de inyectar su lógica interna. Abre el archivo [`../lab/L08_MiniProject.cpp`](../lab/L08_MiniProject.cpp).
>
> 🏋️ **Ejercicio (PROYECTO FINAL):** Es hora de ensamblar tu primer software interactivo desde cero, aplicando la estricta metodología de Extracción de Rutinas. Atrévete con el reto final en [`../exercise/E08_AdivinaElNumero/E08_AdivinaElNumero.cpp`](../exercise/E08_AdivinaElNumero/E08_AdivinaElNumero.cpp).

---

| ⬅️ [Anterior: Números Aleatorios Modernos](L07_Random.md) | 📖 [Menú del Módulo](../README.md) |
|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
