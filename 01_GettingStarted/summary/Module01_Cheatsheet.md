# Módulo 01 — Getting Started: Cheatsheet

Referencia rápida de los conceptos y patrones de ingeniería fundamentales del Módulo 01.

---

## 1. ¿Qué es programar y el Ciclo de Compilación?

Un programa es una secuencia determinista de instrucciones. La CPU solo comprende instrucciones binarias (`0` y `1`). El código fuente (`.cpp`) es el texto estructurado por el humano, y el compilador (`g++`) lo traduce a un binario ejecutable (`.exe`).

```bash
# Compilación estándar obligatoria en C++ Moderno
g++ -std=c++17 archivo.cpp -o programa
```

---

## 2. Anatomía de `int main()` y Salida Estándar

Todo programa en C++ inicia ineludiblemente en la función `main`. La biblioteca `<iostream>` permite enviar texto a la consola mediante `std::cout`.

```cpp
#include <iostream>

int main() {
    std::cout << "Hola, Mundo!\n";
    return 0; // 0 indica terminación exitosa al Sistema Operativo
}
```

> **⚠️ Peligro:** Omitir `#include <iostream>` o escribir instrucciones fuera de una función impedirá la compilación.

---

## 3. Namespaces y la Regla de Oro de `std::`

Los *namespaces* aíslan identificadores para evitar colisiones de nombres entre bibliotecas.

```cpp
// ✅ FORMA OFICIAL DE LA INDUSTRIA (Acceso Explícito):
std::cout << "Código seguro y libre de ambigüedades\n";

// 🚫 VETO TOTAL: Prohibido a nivel global en todo el curso
// using namespace std; // Contamina el ámbito global con miles de nombres
```

> **⚠️ Peligro:** Usar `using namespace std;` globalmente causa colisiones de nombres y fallos de compilación masivos en proyectos de producción.

---

## 4. Formato de Salida y Secuencias de Escape

Usa el carácter de escape `\` dentro de cadenas de texto para dar formato visual.

| Secuencia | Propósito | Ejemplo |
|:---:|---|---|
| `\n` | Salto de línea limpio (sin flush de buffer) | `std::cout << "Hola\n";` |
| `\t` | Tabulación horizontal para columnas | `std::cout << "ID\tNombre\n";` |
| `\"` | Comilla doble literal dentro del string | `std::cout << "\"Texto\"\n";` |
| `\\` | Barra invertida literal | `std::cout << "C:\\Ruta\n";` |

> **⚠️ Peligro:** `std::endl` fuerza un vaciado de buffer (*flush*) innecesario que ralentiza severamente la ejecución. Usa siempre `'\n'`.

---

## 5. Inicialización Uniforme `{}` y Variables Seguras

En C++ Moderno, jamás dejes una variable primitiva sin inicializar. Las llaves `{}` garantizan que la variable no retenga datos basura de la RAM.

```cpp
#include <string>

int edadUsuario{0};            // Inicializado en 0 (Seguro)
double balance{0.0};           // Inicializado en 0.0 (Seguro)
std::string nombreUsuario{""}; // Inicializado vacío (Seguro)
```

> **⚠️ Peligro:** Escribir `int puntaje;` deja la variable con cualquier número binario residual que estuviera en esa celda de RAM (ej. `4291032`).

---

## 6. Captura de Datos: `std::cin` vs `std::getline`

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nombreCompleto{""};
    int edad{0};

    // 1. std::getline para texto con espacios (lee toda la línea)
    std::cout << "Nombre completo: ";
    std::getline(std::cin, nombreCompleto);

    // 2. std::cin >> para valores individuales sin espacios
    std::cout << "Edad: ";
    std::cin >> edad;

    return 0;
}
```

> **⚠️ Peligro:** `std::cin >> string` se detiene en el primer espacio en blanco, dejando el resto del texto atascado en el buffer de entrada para la siguiente lectura.

---

## Checklist de Ingeniería del Módulo 01

- [ ] Compilo manualmente con `g++ -std=c++17` desde la terminal.
- [ ] Uso siempre el prefijo explícito `std::` y jamás `using namespace std;`.
- [ ] Inicializo el 100% de mis variables primitivas y objetos con `{}`.
- [ ] Utilizo `'\n'` y jamás `std::endl` para saltos de línea.
- [ ] Sé cuándo usar `std::cin >>` y cuándo `std::getline(std::cin, var)`.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>