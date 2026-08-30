# E06: Generador de Contraseñas Seguras

## Contexto
Has sido ascendido y transferido a la división de ciberseguridad corporativa. Tu primera tarea de prueba es auditar y reparar un sistema CLI (Interfaz de Línea de Comandos) que genera contraseñas seguras para los empleados.

El sistema fue desarrollado apresuradamente por un contratista y carece de todas las medidas de "Const Correctness" y de seguridad de memoria. El programa base realiza copias pesadas innecesarias, recalcula constantes durante el tiempo de ejecución (gastando CPU inútilmente) y, peor aún, permite colapsar los servidores si un empleado escribe texto en lugar del PIN numérico, paralizando la emisión de credenciales.

## Tu Misión
Abre el archivo `E06_GeneradorDeContrasenas.cpp`. Tu deber es aplicar TODO lo aprendido en el Módulo 05 para transformar este código ineficiente y frágil en una obra maestra de C++ Moderno:
- **`constexpr`**: Encuentra cálculos matemáticos 100% estáticos y oblígale al compilador a resolverlos antes de que el programa corra.
- **`std::string_view`**: Protege la memoria RAM convirtiendo las funciones de impresión estándar en referencias de lectura ultraligeras.
- **`std::string`**: Usa el poder del objeto dinámico para concatenar la contraseña final y solucionar los Type Errors al fusionar literales estáticos.
- **`const`**: Aplica el modificador inquebrantable a las variables generadas para evitar mutaciones accidentales post-creación.
- **Protocolo de Validación (`std::cin`)**: Limpia el buffer de entrada para que el sistema rechace el *trolleo* (entradas no numéricas) sin entrar en bucles infinitos.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 E06_GeneradorDeContrasenas.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
