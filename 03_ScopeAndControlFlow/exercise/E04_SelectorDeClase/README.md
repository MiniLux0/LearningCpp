# ⚔️ Reto E04: Selector de Clase

## 🚨 Contexto
Estás programando el motor lógico de asignación de atributos para un simulador de combate.
El usuario selecciona un rol inicial ingresando un número identificador (1: Infantería, 2: Táctico, 3: Reconocimiento).

El programador junior anterior desconocía la mecánica de exclusión de la estructura `switch`. No implementó las instrucciones de escape, causando un *Fallthrough* masivo. Además, intentó inicializar variables locales dentro de las etiquetas `case` sin proveer un *Local Scope* privado, rompiendo la compilación del programa.

## 🛠️ Tu misión
1. Abre `E04_SelectorDeClase.cpp`.
2. Interrumpe el *Fallthrough* añadiendo las instrucciones de escape (`break`) para garantizar que cada rama sea mutuamente excluyente.
3. Resuelve la vulnerabilidad de memoria encapsulando cada `case` con llaves `{ }` para crear un Scope aislado estricto.

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
