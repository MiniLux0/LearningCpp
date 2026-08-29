# 📝 Reto E05: Promedio (Conversión Segura)

## 🏫 Contexto

Eres el desarrollador del sistema de calificaciones de una escuela. El código actual suma las calificaciones de los estudiantes correctamente, pero cuando calcula el promedio, pierde todos los decimales. ¡Un estudiante que sacó 8.7 está recibiendo un 8 cerrado!

## 🛠️ Tu misión

1. Abre el archivo y analiza cómo se está calculando el promedio. 
2. Ambos operandos (suma y cantidad de materias) son enteros, lo que provoca la "trampa de la división entera".
3. Utiliza la máquina transformadora `static_cast<double>()` para convertir uno de los valores temporalmente a decimal justo antes de la división, rescatando así el promedio exacto.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
