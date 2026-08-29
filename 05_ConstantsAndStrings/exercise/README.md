# 🏋️ Ejercicios Prácticos — Módulo 05

Esta carpeta contiene los retos diseñados para asimilar los conceptos teóricos de **Constants and Strings**, como la inmutabilidad, el rendimiento en tiempo de compilación y el manejo moderno de textos en C++.

## 📁 Lista de Retos

- 📂 **`E01_AsegurandoInventario/`**: Protege las variables críticas de un videojuego aplicando el modificador `const` para evitar bugs de sobreescritura accidental.
- 📂 **`E02_OptimizadorDeCalculos/`**: Ayuda al sistema de sensores de la NASA a ahorrar CPU delegando cálculos matemáticos estáticos al compilador mediante `constexpr`.
- 📂 **`E03_FormateadorDeNombres/`**: Arregla el sistema de perfiles del RPG que actualmente colapsa por intentar fusionar literales estáticos (C-strings) sin utilizar el objeto dinámico `std::string`.
- 📂 **`E04_LectorEficiente/`**: Salva a los servidores de la enciclopedia galáctica optimizando funciones de lectura con `std::string_view` (referencias de solo lectura) en lugar de clonar gigabytes de datos en la RAM.
- 📂 **`E05_EscudoAntiTrolls/`**: Crea un protocolo defensivo de limpieza de tres pasos (`fail()`, `clear()`, `ignore()`) para salvar a un cajero automático de cuelgues y bucles infinitos.
- 📂 **`E06_GeneradorDeContrasenas/`**: Mini-proyecto integrador. Audita el sistema de credenciales de una agencia de ciberseguridad corporativa aplicando todos los conceptos de protección y lectura del módulo simultáneamente.

## 🛠️ Cómo hacer los ejercicios

1. Entra a la carpeta del reto de tu interés.
2. Todo reto tiene un contexto o "lore", así que **siempre lee el `README.md`** que está dentro de la carpeta antes de tocar el código.
3. Abre el archivo principal `.cpp` y sigue las instrucciones que están detalladas en los comentarios (busca los `TODO`).
4. Compila el archivo a mano usando la terminal (ej: `g++ E01_Nombre.cpp -o app`).
5. Si no sabes cómo continuar o el compilador arroja errores, entra a la subcarpeta `solution/` y revisa el código resuelto.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
