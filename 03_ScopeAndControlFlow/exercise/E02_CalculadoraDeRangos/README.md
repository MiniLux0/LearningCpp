# 🛣️ Reto E02: Calculadora de Rangos

## 🚨 Contexto
Eres el encargado del sistema de cobros de una autopista inteligente. El peaje varía dependiendo del peso del vehículo en kilogramos (kg).

Las tarifas son las siguientes:
- **Más de 5000 kg (Vehículo pesado):** Paga $50.
- **De 2500 kg a 5000 kg (Vehículo mediano):** Paga $25.
- **Menos de 2500 kg (Vehículo ligero):** Paga $10.

El problema es que el sistema tiene el orden invertido. Un camión monstruo de 6,000 kg está siendo cobrado como un vehículo ligero ($10) porque el código cae en la trampa del código inalcanzable (*Unreachable code*).

## 🛠️ Tu misión
1. Abre el archivo `E02_CalculadoraDeRangos.cpp`.
2. Reorganiza los bloques `if` y `else if` en el orden correcto (de la restricción más grande a la más pequeña) para que el flujo en cascada funcione correctamente.

### ⚙️ Instrucciones de Compilación:
Compila tu programa desde la terminal con:
```bash
g++ -std=c++17 E02_CalculadoraDeRangos.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
