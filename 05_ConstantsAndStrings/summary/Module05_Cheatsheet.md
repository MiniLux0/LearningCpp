# Hoja de Repaso: Constantes y Strings

¡Guarda esta página! Aquí tienes el resumen de todas las herramientas de seguridad arquitectónica, rendimiento y manipulación de texto que dominaste en el Módulo 05.

## 1. Inmutabilidad (`const`)
Aplica un modificador de acceso inquebrantable a las variables para que su valor jamás pueda cambiar durante la ejecución del programa, protegiendo las direcciones de memoria contra alteraciones accidentales (Mutaciones).
```cpp
const int diasPorSemana{7};
// diasPorSemana = 8; // 🐞 ERROR DEL COMPILADOR: La dirección de memoria está protegida (Read-only).
```

## 2. Evaluación en Tiempo de Compilación (`constexpr`)
Delega cálculos matemáticos al compilador *antes* de que inicie la ejecución binaria. Es ultra rápido, pero solo funciona si el compilador posee toda la información constante por adelantado.
```cpp
constexpr int horas{24};
constexpr int minutosPorDia{horas * 60}; // ⚡ Resuelto antes de correr. Cero ciclos de CPU en tiempo de ejecución.
```

## 3. Cadenas de Texto Dinámicas (`std::string`)
La estructura fundamental para gestionar memoria de texto de forma segura. Se redimensiona y concatena de forma dinámica en el Heap.
**La regla de oro:** Para invocar el operador de concatenación `+`, al menos uno de los operandos debe ser un objeto dinámico (`std::string`), no un literal crudo C-style.
```cpp
#include <string>

std::string palabra{"Hola"};
std::string frase{palabra + " Mundo"}; // ⚡ Correcto: Un objeto dinámico gestiona la memoria del literal.
// std::string fallo = "Hola" + " Mundo"; // 🐞 ERROR: Los literales estáticos (C-strings) carecen de métodos de concatenación.
```

## 4. Las Referencias de Solo Lectura (`std::string_view`)
Sirven para procesar textos pesados sin realizar clones por Pass-by-value en la memoria RAM. Son ultraligeras e instantáneas. Úsalas SIEMPRE como parámetro en funciones si el objetivo es auditar o procesar el texto sin mutarlo.
```cpp
#include <string_view>

void leerTexto(std::string_view texto) {
    // Solo apuntamos al bloque de memoria original. ¡No se consume RAM extra!
}
```
> **⚠️ Peligro (Dangling View):** Jamás inicialices una referencia ligera apuntando a un objeto dinámico temporal que haya sido destruido en la memoria (Dangling Pointer / Fuga de Scope local).

## 5. Validación de Entrada (Sanitizando `std::cin`)
Si el sistema espera un tipo de dato estructurado pero recibe basura en el input, el flujo de entrada (buffer) colapsa provocando bucles infinitos. Aplica siempre este protocolo de sanitización:
```cpp
int numero{0};
std::cin >> numero;

if (std::cin.fail()) { // 1. Detectar: El flujo de entrada (buffer) colapsó por fallo de extracción.
    std::cin.clear();  // 2. Restablecer banderas de error operativo.
    std::cin.ignore(10000, '\n'); // 3. Purgar la basura residual del buffer.
}
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
