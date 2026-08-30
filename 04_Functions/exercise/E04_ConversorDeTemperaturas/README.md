# Reto E04: El Termostato Congelado

## La Misión

Estás trabajando para un laboratorio de biotecnología. Han programado un sistema que lee la temperatura de una muestra en grados Celsius y necesita una rutina para convertirla matemáticamente a Fahrenheit.

El código actual invoca a la función `convertirAFahrenheit(temperatura)`. El programador junior que la diseñó pensó que, al mutar el parámetro de entrada dentro del Scope local de la función, la variable original en la memoria del `main()` se actualizaría mágicamente por referencia cruzada.

Como resultado del aislamiento de memoria (*Pass-by-value*), todas las muestras del laboratorio reportan estar congeladas en su valor original de Celsius porque el resultado del cálculo matemático se está perdiendo (y destruyendo) junto con la rutina temporal.

Tu misión es arreglar el flujo de retorno de los datos.

### Reglas de Oro:
1. No alteres la fórmula matemática, el cálculo aritmético ya es correcto.
2. Añade la capacidad de **retornar** la transformación matemática de vuelta al Scope que invocó a la función.
3. Modifica la invocación en el `main()` para que atrape (reasigne) el valor que devuelve la función en lugar de perder el cálculo temporal.

### ⚙️ Instrucciones de Compilación

Compila tu solución desde la terminal con:
```bash
g++ -std=c++17 E04_ConversorDeTemperaturas.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
