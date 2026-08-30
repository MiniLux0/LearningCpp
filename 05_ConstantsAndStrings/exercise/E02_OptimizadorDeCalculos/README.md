# E02: Optimizador de Cálculos

## Contexto
Trabajas como programador en la agencia espacial para la sonda satelital Voyager 3. En el espacio profundo, la energía (batería) y la capacidad de procesamiento son extremadamente limitadas. 

Por regla de oro, cualquier cálculo matemático que pueda realizarse **antes del despegue** (en los servidores de la Tierra) salvará valiosos ciclos de batería del satélite durante el vuelo. Un programador novato dejó toda la física configurada con variables normales, lo que significa que el pobre satélite tiene que hacer las multiplicaciones de la velocidad de la luz en vivo.

## Tu Misión
Abre el archivo `E02_OptimizadorDeCalculos.cpp`. 
1. Utiliza `constexpr` y la inicialización uniforme `{}` para todas las variables y cálculos cuyas respuestas el compilador puede saber por adelantado.
2. Existe un sistema de simulación de temperatura que lee el estado térmico de los paneles solares usando `std::cin`. Este valor **solo** se conoce en el espacio, en vivo. Asegúrate de proteger esa variable correctamente (piensa: ¿aquí va `const` o `constexpr`?).

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 E02_OptimizadorDeCalculos.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
