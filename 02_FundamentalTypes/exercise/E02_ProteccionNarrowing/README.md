# 🛡️ Reto E02: Protección contra Narrowing

## 👾 Contexto

Estás revisando código antiguo de un videojuego escrito por un novato. El programador usó el signo `=` clásico para asignar valores, y como resultado, hay pérdida silenciosa de datos (*narrowing*) por todas partes. ¡Los multiplicadores de daño están perdiendo sus decimales!

## 🛠️ Tu misión

1. Entra al código y cambia todas las inicializaciones que usan `=` por el estilo moderno y estricto de llaves `{}`.
2. Intenta compilar. Verás que las llaves activan las defensas del compilador y el programa no compilará, protegiéndote del error.
3. Corrige los tipos de datos (ej. cambiando `int` por `double` donde sea necesario) para que el programa compile sin errores y no pierda información valiosa.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
