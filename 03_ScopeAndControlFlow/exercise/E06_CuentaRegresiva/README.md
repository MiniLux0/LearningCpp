# 🚀 Reto E06: Cuenta Regresiva

## 🚨 Contexto
Estás programando el secuenciador de lanzamiento de una agencia aeroespacial.
El sistema demanda un ciclo de iteración inversa estricto que comience en 10 y finalice en 1 antes de ceder el control de flujo para la ignición.

El programador junior asignado cometió dos errores arquitectónicos críticos en el diseño del bucle `for`:
1. Configuró una mutación ascendente (sumar) en un bucle diseñado lógicamente para descender, provocando un ciclo divergente.
2. Definió un límite relacional erróneo que produce un *Off-By-One Bug*, causando que la secuencia alcance el valor nulo (0) y aborte la misión en plataforma.

## 🛠️ Tu misión
1. Abre `E06_CuentaRegresiva.cpp`.
2. Refactoriza el encabezado de control del `for`: corrige la Inicialización, ajusta la Condición relacional y repara la Mutación para configurar un decremento estricto (`10, 9, 8... 1`).
3. Verifica la ejecución del proceso iterativo, garantizando que el sistema no incurra en un error *Off-By-One* que procese el índice 0.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
