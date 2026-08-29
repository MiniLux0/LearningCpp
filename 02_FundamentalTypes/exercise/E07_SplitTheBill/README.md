# 🏢 Reto E07: Split the Bill (Final Boss)

## 🚀 Contexto

Este es tu proyecto final del Módulo 02. Has sido contratado por una startup para crear un programa que divida los gastos del alquiler de un departamento.

El usuario debe pagar el alquiler base y los servicios públicos (luz, agua). Luego, debe dividir el costo entre los compañeros de cuarto (roommates). Como aún no manejamos bloques condicionales (`if`), deberás imprimir un "Estado de Sistema" utilizando un solo booleano que verifique varias reglas lógicas al mismo tiempo.

## 🛠️ Reglas de Aceptación
- Debes inicializar todas las variables usando inicialización uniforme estricta `{}`.
- Debes usar `static_cast<double>()` para calcular la cuota por roommate de manera exacta, sin perder dinero.
- Crea un `bool` llamado `sistema_ok` que sea verdadero **SOLO SI** se cumplen todas estas condiciones a la vez:
  - Hay al menos 1 roommate.
  - El alquiler base es mayor a 0.
  - El costo de servicios es mayor o igual a 0.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
