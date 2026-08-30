# Reto E09: Sistema de Registro de Calificaciones

## Contexto
El departamento de evaluación académica de la universidad necesita un sistema automatizado en consola para que los profesores registren y analicen las calificaciones de sus exámenes. El sistema debe ser interactivo, intuitivo y, sobre todo, altamente resiliente ante entradas inválidas o consultas erróneas.

## Tu Misión
Abre el archivo `E09_RegistroDeCalificaciones.cpp` y completa la implementación de las siguientes funciones:
1. `agregarNota(std::vector<double>& notas)`: Solicita una nota numérica, valida que esté en el rango `[0.0, 20.0]` y que el flujo de `std::cin` no haya colapsado. Si es válida, la inserta con `.push_back()`.
2. `mostrarNotas(const std::vector<double>& notas)`: Si el vector está vacío (`.empty()`), muestra un aviso. De lo contrario, imprime cada nota junto a su posición de índice.
3. `consultarNota(const std::vector<double>& notas)`: Solicita un índice al usuario y realiza el acceso con `.at(indice)` dentro de un bloque `try/catch`, capturando `const std::out_of_range&` para manejar índices inexistentes.
4. `mostrarEstadisticas(const std::vector<double>& notas)`: Si no está vacío, recorre el vector para calcular el promedio, identificar la nota máxima y la nota mínima.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E09_RegistroDeCalificaciones.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
