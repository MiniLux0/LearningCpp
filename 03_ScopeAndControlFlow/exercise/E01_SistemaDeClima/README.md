# 🌧️ Reto E01: Sistema De Clima

## 🚨 Contexto
Has sido contratado por la granja "Cosechas Felices" para programar el sistema de riego automático. 
La granja tiene sensores que miden la humedad del suelo (en un rango del 0 al 100).

Las reglas del cultivo son simples:
1. Si la humedad es menor a 40, el sistema debe encender los aspersores.
2. Si la humedad es 40 o mayor, el sistema debe mantener los aspersores apagados para no ahogar las raíces.

**El problema:** 
El programador junior anterior escribió el código a las 3 AM y dejó un desastre. Los aspersores se están encendiendo incluso cuando el suelo está inundado, ahogando las plantas de tomate.

## 🛠️ Tu misión
1. Abre el archivo `E01_SistemaDeClima.cpp`.
2. Encuentra y elimina el error de sintaxis ("el punto y coma asesino") que hace que la primera condición falle.
3. Unifica la lógica usando un solo bloque `if-else` en lugar de dos comprobaciones separadas.

### ⚙️ Instrucciones de Compilación:
Compila tu programa desde la terminal con:
```bash
g++ -std=c++17 E01_SistemaDeClima.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
