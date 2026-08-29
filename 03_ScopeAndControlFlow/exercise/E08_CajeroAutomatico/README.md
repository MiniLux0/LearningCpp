# 🏧 Reto Final E08: Cajero Automático (Mini-proyecto)

## 🚨 Contexto
¡Felicidades! Has sido asignado a la ingeniería core del Banco Central para desarrollar la interfaz transaccional de su nuevo modelo de cajero automático. 

Este es el reto final del Módulo 03. Deberás orquestar los conceptos de *Local Scope*, *Exclusión Condicional* (`if / else`, `switch`), e *Iteración Infinita Controlada* para construir un menú persistente de consola.

El sistema debe instanciar un balance inicial de $1000 y gestionar un menú de 3 operaciones.

## 🛠️ Tu misión
1. Abre `E08_CajeroAutomatico.cpp`.
2. Implementa un bucle de iteración perpetua (ej. `while (true)`) para que el sistema mantenga la sesión del usuario abierta.
3. Solicita una instrucción (input) e impleméntalo utilizando un enrutador `switch`:
   - **Caso 1 (Consultar Balance):** Imprime el saldo actual.
   - **Caso 2 (Retirar Fondos):** Solicita un monto. Aplica una evaluación condicional (`if / else`) para prevenir sobregiros. Si hay fondos, aplica la mutación aritmética. Si no, deniega la transacción por "Fondos insuficientes".
   - **Caso 3 (Cerrar Sesión):** Imprime un mensaje de despedida e invoca una instrucción de terminación prematura (`break` o `return 0;`) para abortar la sesión.
   - **Caso Default:** Atrapa *inputs* anómalos imprimiendo "Opción inválida".
4. **Arquitectura de Memoria Estricta:** Asegura que la declaración de la variable `saldo` ocurra en el *Scope Exterior* (antes de iniciar la iteración) para evitar que la memoria sea reasignada a $1000 en cada ciclo. Aplica bloques de aislamiento `{ }` en tus ramas `case` si requieres inicializar variables locales.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
