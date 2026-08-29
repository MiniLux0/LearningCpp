# 🔍 Reto E07: Buscador de Archivos

## 🚨 Contexto
Estás programando un escáner heurístico de auditoría de ciberseguridad.
El sistema tiene acceso secuencial a 20 archivos críticos indexados del 1 al 20. 

Las reglas de la auditoría estipulan dos excepciones al flujo:
1. El archivo índice 13 es una bóveda en cuarentena (*honeypot*). Leer sus metadatos disparará un bloqueo de red. Debes aplicar un salto de iteración para evitar su procesamiento.
2. El archivo índice 18 es el objetivo primario de la auditoría. Una vez leído, el escaneo debe terminar de forma prematura para ahorrar ciclos de CPU (los archivos 19 y 20 deben ser ignorados).

## 🛠️ Tu misión
1. Abre `E07_BuscadorDeArchivos.cpp`.
2. Implementa una instrucción `continue` para abortar la iteración correspondiente al archivo índice 13.
3. Implementa una instrucción `break` para destruir el bucle inmediatamente tras extraer la información del índice 18.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
