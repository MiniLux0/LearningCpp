# 🍕 Reto E03: Reparto de Pizzas

## 📦 Contexto

Estás organizando una fiesta y necesitas calcular la cantidad de comida y los gastos. Has escrito un pequeño programa en C++ para automatizarlo, pero **los cálculos están saliendo mal**. Esto se debe a un mal manejo de la precedencia de operadores (el orden en que C++ lee las matemáticas) y a la famosa trampa de la división entera.

## 🛠️ Tu misión

1. **Arregla la precedencia:** El cálculo del `costo_total` está multiplicando primero. Queremos sumar ambos precios primero y multiplicar el total por 2. *(El resultado esperado es $540)*.
2. **Arregla la división:** El cálculo de `porciones_exactas` está perdiendo los decimales y dando un resultado truncado. Cambia lo necesario para obtener el resultado con decimales *(esperado: 2.75)*.
3. **Usa el módulo (`%`):** Calcula cuántas porciones enteras sobran en la caja si repartes equitativamente.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
