# 🕵️ Reto E06: Detective Auto

## 🚨 Contexto

¡Desastre! Un desarrollador perezoso acaba de pasar por el código y reemplazó absolutamente TODOS los tipos de datos por la palabra clave `auto`. Ahora el código sufre de "amnesia". Ya nadie sabe qué tipo de dato devuelve cada función, el autocompletado del editor está roto y los bugs se esconden fácilmente.

## 🛠️ Tu misión

1. Conviértete en el compilador. Lee el valor que está a la derecha del signo igual para cada variable y deduce lógicamente qué tipo de dato debe ser.
2. Reemplaza cada `auto` por su tipo estricto (`int`, `double`, `bool`, `char`).
3. Hay un solo lugar donde sí está permitido dejar el `auto`: en la variable `resultado_final` (porque tiene un `static_cast` explícito en la misma línea). ¡Déjalo ahí!

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
