# 🏴‍☠️ Reto E03: Rescate de Variables

## 🚨 Contexto
Estás programando el panel de seguridad de una base de datos segura. El programa debe pedir una clave de acceso. Si la clave es correcta, debe calcular el balance total de los fondos (Fondos iniciales + Interés).

El código base tiene dos defectos estructurales relacionados con el Scope:
1. **Pérdida de Memoria (Scope Error):** El programador declaró la variable `recompensaTotal` de forma estrictamente local DENTRO del bloque condicional `if`. Por lo tanto, cuando el bloque `if` finaliza, la variable es liberada de la memoria y el programa no compila al intentar acceder a ella más abajo.
2. **Variable Shadowing (Ocultamiento):** Al aplicar el interés, el desarrollador volvió a declarar el identificador `int oro{...}` dentro del bloque, creando una nueva dirección de memoria local que bloqueó el acceso a la original. El interés se sumó a la local y luego fue destruido, dejando la cuenta principal intacta.

## 🛠️ Tu misión
1. Abre `E03_RescateDeVariables.cpp`.
2. Mueve la declaración de `recompensaTotal` hacia el Scope exterior (`main`) para extender su ciclo de vida y visibilidad.
3. Elimina la redeclaración engañosa (Shadowing) removiendo la palabra clave `int` durante la operación aritmética para que la mutación modifique la variable correcta en memoria.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
