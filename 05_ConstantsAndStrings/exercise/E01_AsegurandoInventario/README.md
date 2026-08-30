# Reto E01: Asegurando el Inventario

## Contexto
Eres el programador principal de un pequeño videojuego de aventuras. Las reglas de diseño establecen que el número máximo de jugadores en una partida es 4, y el identificador (ID) del objeto "Jefe Final" es el 99.

Un programador junior escribió el código base, pero declaró todas las constantes arquitectónicas como variables mutables (sin `const`). Durante las pruebas de ayer, ocurrió un desastre: un error en el flujo de ejecución reasignó accidentalmente el límite de jugadores a 50, lo que provocó que el servidor colapsara.

## Tu Misión
Abre el archivo `E01_AsegurandoInventario.cpp`. Tu tarea es aplicar el principio de **Const Correctness**:
1. Declara como `const` las variables que por diseño de sistema **nunca** deberían ser reasignadas en tiempo de ejecución.
2. Utiliza la inicialización uniforme con llaves `{}` en lugar de la asignación clásica `=`.
3. Borra o comenta la línea defectuosa que intenta alterar la dirección de memoria protegida, de lo contrario, el compilador abortará el proceso.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 E01_AsegurandoInventario.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
