# Reto E08: Refactorización en Header

## Contexto
El equipo de analítica espacial desarrolló un script monolítico de 2,000 líneas que contiene algoritmos de procesamiento de señales vectoriales mezclados directamente con el `main`. Otros departamentos de la estación necesitan utilizar las funciones `sumarElementos` y `encontrarMaximo`, pero no pueden hacerlo porque las funciones están atrapadas dentro del archivo principal.

Tu misión es refactorizar esta arquitectura aplicando los estándares profesionales de C++ Moderno:
1. Extraer los prototipos a un archivo de cabecera protegido: `VectorUtils.h`.
2. Implementar los cuerpos de las funciones en `VectorUtils.cpp`.
3. Consumir el módulo modularizado desde `E08_RefactorizacionHeader.cpp`.

## Tu Misión
1. En `VectorUtils.h`, protege el archivo con `#pragma once` y declara los prototipos de `sumarElementos` y `encontrarMaximo`.
2. En `VectorUtils.cpp`, incluye `"VectorUtils.h"` e implementa ambas funciones.
3. En `E08_RefactorizacionHeader.cpp`, incluye `"VectorUtils.h"` e invoca las funciones para procesar el vector de prueba.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra VectorUtils.cpp E08_RefactorizacionHeader.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
