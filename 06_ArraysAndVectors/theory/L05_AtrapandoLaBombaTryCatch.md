# L05: Atrapando la Bomba: Manejo Táctico de Excepciones con `try / catch`

Imagina un artefacto explosivo con temporizador: si se detona al aire libre en medio de una central eléctrica, la onda expansiva destruirá todo el complejo apagando la ciudad entera; pero si el equipo de seguridad coloca el artefacto dentro de una cápsula blindada de contención, la detonación queda neutralizada en su interior y la estación continúa operando con normalidad. Desvanecemos la metáfora de las cápsulas y las bombas para entrar al mecanismo formal de resiliencia en software: **Lanzamiento de excepciones (*Throwing Exceptions*)**, **Bloque de contención `try`**, **Capturador de fallo `catch`** y el diagnóstico con **`std::out_of_range`**.

---

## 1. El Problema de las Excepciones No Controladas

En la lección anterior aprendimos que `.at()` lanza una excepción `std::out_of_range` cuando un índice está fuera de los límites. Sin embargo, si nuestro programa no hace nada para manejar esa excepción, el sistema operativo ejecutará la función `std::terminate()`, cerrando el programa de forma abrupta e inmediata (*Crash*).

En aplicaciones de misión crítica (sistemas bancarios, servidores de videojuegos, control médico o automotriz), un cierre forzado es inaceptable. Necesitamos **atrapar el error táctico**, registrar lo sucedido y continuar la ejecución sin caer.

---

## 2. La Estructura de Contención: `try` y `catch`

C++ proporciona la estructura de control `try / catch` (incluyendo la cabecera `<stdexcept>`) para interceptar fallos en tiempo de ejecución:

```cpp
#include <iostream>
#include <vector>
#include <stdexcept> // Contiene std::out_of_range

int main() {
    std::vector<int> inventario{10, 20, 30}; // size = 3

    try {
        // Bloque protegido: Código que puede detonar una excepción
        std::cout << "Accediendo a casilla 1: " << inventario.at(1) << '\n';
        
        // Esta línea lanzará la excepción std::out_of_range:
        std::cout << "Accediendo a casilla 99: " << inventario.at(99) << '\n';
        
        std::cout << "Esta linea NUNCA se ejecutara.\n";
    } 
    catch (const std::out_of_range& error) {
        // Bloque de contención: Se ejecuta si y solo si ocurre el error
        std::cout << "Se atrapo una excepcion de rango!\n";
        std::cout << "Diagnostico tecnico: " << error.what() << '\n';
    }

    std::cout << "El programa continua ejecutandose con total normalidad.\n";
    return 0;
}
```

---

## 3. ¿Cómo Funciona el Flujo de Ejecución?

```text
FLUJO DE EJECUCIÓN CON TRY/CATCH:
1. Entra al bloque try.
2. Ejecuta operaciones normales.
3. Se detecta un fallo en .at(99) ──> SE DETONA EXCEPCIÓN.
4. Salta INMEDIATAMENTE al bloque catch correspondiente.
5. Ejecuta la lógica de recuperación o mensaje de error (error.what()).
6. Continúa con el resto del programa debajo del bloque catch.
```

### El Método `.what()`
El objeto atrapado por referencia constante (`const std::out_of_range& error`) posee un método miembro llamado `.what()` que retorna una cadena de texto describiendo técnicamente la causa del fallo proporcionada por la biblioteca estándar.

---

> [!NOTE]
> En este módulo aprendemos el uso táctico y básico de `try / catch` enfocado exclusivamente en la contención de `std::out_of_range`. En el Módulo 13 profundizaremos en el diseño avanzado de arquitecturas resilientes y el desenrollado de pila (*Stack Unwinding*).

---

> 🧪 **Laboratorio:** Observa cómo `try/catch` rescata un programa de un colapso inminente. Abre el archivo [`../lab/L05_TryCatchBasico.cpp`](../lab/L05_TryCatchBasico.cpp).
>
> 🏋️ **Ejercicio:** Blinda el terminal de un banco automatizado para que solicitudes con índices inválidos no apaguen el servidor. Atrévete con el reto en [`../exercise/E05_AtrapandoLaBomba/E05_AtrapandoLaBomba.cpp`](../exercise/E05_AtrapandoLaBomba/E05_AtrapandoLaBomba.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. ¿Qué sucede con las líneas de código restantes dentro del bloque <code>try</code> una vez que una instrucción detona una excepción?</b></summary>

> Se omiten por completo. La ejecución salta de forma instantánea al bloque `catch` correspondiente sin ejecutar ninguna línea posterior dentro del `try`.
</details>

<details>
<summary><b>2. ¿Qué información técnica proporciona el método <code>error.what()</code>?</b></summary>

> Retorna una cadena de texto descriptiva generada por el contenedor explicando el motivo técnico por el cual se lanzó la excepción (por ejemplo, que el índice solicitado excedió el tamaño del vector).
</details>

---

| ⬅️ [Anterior: L04 — Acceso Seguro: .at() vs []](L04_AccesoSeguroAtVsSubscript.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: L06 — Range-based for](L06_RangeBasedFor.md) |
|:---|:---:|---:|

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
