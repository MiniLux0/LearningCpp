# Módulo 04 — Functions: Cheatsheet

Referencia rápida de los conceptos y patrones clave del Módulo 04. Úsala para recordar la sintaxis y las reglas arquitectónicas aprendidas sobre las rutinas delegadas.

## 1. Anatomía de una Función
Toda función posee 4 componentes esenciales y **debe declararse arriba del `main()`** en esta etapa arquitectónica.

```cpp
// 1. Firma de retorno | 2. Identificador | 3. Parámetros
int sumar(int a, int b) {
    // 4. Cuerpo de la función (Scope local)
    int resultado{a + b};
    return resultado; // Inyecta el valor resultante
}
```

## 2. Invocación y Aislamiento (Scope)
*   **Aislamiento de Memoria:** Las variables instanciadas en el Scope local son destruidas y liberadas al finalizar la rutina.
*   **Ocultamiento de Información:** El Scope invocador (`main()`) carece de visibilidad sobre los identificadores internos de las sub-rutinas, previniendo colisiones de memoria.
*   Los datos inyectados vía `return` deben ser interceptados y almacenados en el Scope que realiza la llamada.

```cpp
int main() {
    // Interceptamos la transferencia de memoria inicializando la variable {}
    int total{sumar(5, 10)};
}
```

## 3. Rutinas Void (Efectos Secundarios)
Si una función ejecuta acciones que modifican el estado (ej. I/O en consola) y no requiere inyectar cálculos de retorno, su firma debe ser `void`.
Es ilegal inicializar variables interceptando el output de una rutina `void` (provocará el error: `void value not ignored as it ought to be`).

```cpp
void imprimirAlerta() {
    std::cout << "[ERROR] Protocolo abortado.\n";
}

int main() {
    imprimirAlerta(); // Correcto. Invocación como instrucción independiente.
}
```

## 4. Pass-by-value (Aislamiento de Clonación)
En C++, al transferir una variable hacia una función, el compilador aprovisiona una **clonación estricta**. La rutina mutará la memoria local aislada; el estado original en el `main()` permanece inmutable. Para consolidar el estado, debes **retornar** y **reasignar**.

```cpp
int aplicarDanio(int memoria_aislada) {
    memoria_aislada = memoria_aislada - 10;
    return memoria_aislada;
}

int main() {
    int vida_boss{100};
    // Interceptamos la memoria de retorno y sobreescribimos la memoria original
    vida_boss = aplicarDanio(vida_boss); 
}
```

## 5. El Arte del Refactoring (Modularidad)
El flujo `main()` debe leerse como un índice de alto nivel (Orquestador). 
*   Identifica bloques acoplados densos.
*   Aplica **Extracción de Rutinas**.
*   **Delega** invocando identificadores expresivos desde el `main()`.

## 6. Generación Pseudoaleatoria (`<random>`)
La librería moderna `<random>` exige arquitecturas de 3 componentes: Entropía, Motor (PRNG) y Distribución.
Es imperativo aplicar el modificador `static` en el motor para evitar el colapso de secuencias estocásticas debido a la reconstrucción instantánea del ciclo de vida.

```cpp
#include <random>

int lanzarDado() {
    // static preserva el estado del motor en memoria entre invocaciones
    static std::mt19937 motor{std::random_device{}()};
    
    // Distribución Estadística
    std::uniform_int_distribution<int> rango{1, 6};
    
    return rango(motor);
}
```

---

⬅️ [Volver al Menú Principal del Módulo](../README.md)

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
