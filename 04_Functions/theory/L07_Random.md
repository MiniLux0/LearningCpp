# L07: Números Aleatorios Modernos (`<random>`)

Hacer que un procesador determinista genere un número *verdaderamente* aleatorio es físicamente imposible. En su lugar, utilizamos matemáticas estocásticas complejas para generar secuencias que *parecen* aleatorias. A esto se le conoce en Ciencias de la Computación como **Generación de Números Pseudo-Aleatorios (PRNG)**.

Imagina construir un motor de azar: necesitas una "chispa" inicial de caos, un motor que multiplique ese caos, y un molde para recortar el resultado final a los números que te interesan.

A partir de aquí, formalizaremos la arquitectura del PRNG. Para construir este sistema en C++ Moderno, importamos la librería `<random>` y ensamblamos tres componentes: la **Entropía**, el **Motor Matemático** y la **Distribución Estadística**.

---

## La Arquitectura del PRNG (3 Capas)

Para generar secuencias pseudo-aleatorias de alta calidad para simulación y lógica de sistemas (no criptográficas), ensamblamos:
1. **La Entropía (`std::random_device`):** Lee ruido físico real del hardware (ej. temperatura de la CPU, variaciones magnéticas del disco duro) para generar un número caótico inicial. A esto se le conoce como *Semilla (Seed)*.
2. **El Motor (`std::mt19937`):** Es el algoritmo estocástico (conocido como *Mersenne Twister*) que ingiere la semilla de entropía y comienza a procesar secuencias numéricas altamente impredecibles y gigantescas.
3. **La Distribución (`std::uniform_int_distribution`):** Toma las secuencias masivas del Mersenne Twister y las normaliza estadísticamente para que caigan uniformemente dentro de un rango específico (ej. del 1 al 6).

Como instanciar esta arquitectura directamente en el `main()` violaría la Separación de Responsabilidades (L06), debemos encapsular el sistema dentro de una rutina delegada.

```cpp
#include <random>

int lanzarDado() {
    // 1. Entropía y 2. Motor Mersenne Twister
    // El modificador 'static' ancla el motor en la memoria para que no se destruya
    static std::mt19937 motor{std::random_device{}()};
    
    // 3. Distribución Estadística (rango inclusivo del 1 al 6)
    std::uniform_int_distribution<int> distribucion{1, 6};
    
    // Inyectamos el motor a través de la distribución y retornamos el resultado
    return distribucion(motor);
}
```

<div align="center">
  <img src="assets/l07_rng_machine.gif" alt="Arquitectura de 3 capas para números pseudo-aleatorios en C++">
</div>

#### 🔍 Traducción Visual del Pipeline de Azar (<random>):
* **1. Entropía de Hardware (`std::random_device` - Rojo):** Captura ruido físico del hardware para inyectar una semilla impredecible.
* **2. Motor Pseudo-Aleatorio (`static std::mt19937` - Cian):** Genera secuencias numéricas de 32 bits de alta calidad. El modificador `static` preserva el motor en RAM evitando secuencias duplicadas.
* **3. Distribución Uniforme (`std::uniform_int_distribution` - Oro/Verde):** Normaliza y mapea el output masivo en un rango entero exacto (1 a 6) sin sesgo estadístico.

---

## La anomalía de la regeneración por milisegundo

Nota que hemos introducido el modificador de memoria temporal: `static`.

En el Módulo 03 aprendimos que las variables locales son destruidas al final de su Scope. Si omitiéramos `static`, el motor `mt19937` se destruiría cada vez que la función retornara el valor, obligando al sistema a instanciar uno nuevo utilizando una nueva semilla de entropía.

**Fallo de Arquitectura:** Los procesadores modernos ejecutan instrucciones tan rápido, que si invocas a la función 5 veces consecutivas dentro de la misma ventana de reloj (milisegundos), el hardware de entropía leerá el mismo estado físico y entregará **la misma semilla**. ¡El PRNG te devolverá números clonados idénticos!

El modificador `static` le ordena al compilador: *"Alójalo en la sección de datos estáticos de la RAM y no lo destruyas cuando termine la función"*. De esta manera, el motor retiene su estado interno y continúa mutando su secuencia estocástica a lo largo de todo el ciclo de vida del programa.

---

> 🧪 **Laboratorio:** Observa un PRNG construido correctamente con persistencia en memoria local (`static`). Abre el archivo [`../lab/L07_Random.cpp`](../lab/L07_Random.cpp).
>
> 🐞 **Demo de Bug:** Observa el colapso estocástico cuando un motor se reconstruye sin retención de estado a velocidades de reloj altas. Ejecuta la trampa en [`../lab/demos/D07_StaticRngBug.cpp`](../lab/demos/D07_StaticRngBug.cpp).
>
> 🏋️ **Ejercicio:** El algoritmo de *spawneo* de enemigos del RPG está instanciando hordas de clones idénticos debido a este fallo de memoria temporal. Atrévete con el reto en [`../exercise/E07_GeneradorDeSemillas/E07_GeneradorDeSemillas.cpp`](../exercise/E07_GeneradorDeSemillas/E07_GeneradorDeSemillas.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>Autochequeo: ¿Por qué no utilizamos la antigua función legacy <code>rand()</code> heredada de C?</b></summary>

> **Falla estadística de distribución.** 
> La función `rand()` es repudiada en la ingeniería moderna porque padece de sesgo modular (no distribuye los números uniformemente, propiciando que ciertos valores aparezcan con mayor frecuencia) y su semilla `srand(time)` es vulnerable e hiper-predecible. C++ Moderno exige estrictamente la arquitectura de `<random>`.

</details>

---

| ⬅️ [Anterior: Diseñando con funciones (Refactoring)](L06_Refactoring.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Mini-proyecto (Adivina el Número)](L08_MiniProject.md) |
|---|---|---|

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
