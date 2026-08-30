# ☢️ Reto E05: Contraseña Segura

## 🚨 Contexto
El servidor de acceso de la base de datos requiere una autenticación mediante un PIN (1234).
Si el usuario ingresa un PIN incorrecto, el programa debe denegar el acceso y solicitar el PIN de nuevo de forma persistente. 

El código actual implementó un bucle `while` (Pre-comprobación) con un defecto estructural severo: el programador posicionó la recolección de datos (`std::cin`) fuera del bloque de iteración. Esto impide que el estado se actualice, disparando un Bucle Infinito (*Infinite Loop*) que satura la terminal.

## 🛠️ Tu misión
1. Abre `E05_ContrasenaSegura.cpp`.
2. Refactoriza el bloque de iteración para utilizar una arquitectura `do-while` (Post-comprobación). De este modo, garantizas que la solicitud de recolección de datos (`std::cin`) ocurra al menos una vez, encapsulándola de forma segura dentro del ciclo de iteración.

### ⚙️ Instrucciones de Compilación:
Compila tu programa desde la terminal con:
```bash
g++ -std=c++17 E05_ContrasenaSegura.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
