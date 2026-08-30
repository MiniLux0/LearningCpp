# Reto E03: Inventario Dinámico

## Contexto
Eres el oficial de sistemas a bordo de la fragata de exploración estelar *Nébula Prime*. La tripulación se prepara para saltar al hiperespacio y el sistema de soporte vital requiere inicializar tres compartimentos del almacén con suministros críticos:
1. **Compartimento de Oxígeno:** Requiere almacenar exactamente 4 botellas con los niveles de pureza: 95, 98, 100 y 92.
2. **Compartimento de Baterías de Emergencia:** Requiere inicializar 6 celdas vacías listas para ser cargadas (todas en valor 0).
3. **Compartimento de Raciones:** Requiere inicializar 3 paquetes de supervivencia con exactamente 50 unidades de energía cada uno.

El software heredado que controlaba la nave usaba variables desconectadas y no compilaba de forma moderna. Tu misión es inicializar estos inventarios utilizando `std::vector<int>` y las técnicas idiomáticas de C++17.

## Tu Misión
Abre el archivo `E03_InventarioDinamico.cpp` y completa los `TODOs`:
1. Inicializa `oxigeno` usando la lista de inicialización uniforme con llaves `{}` con los 4 valores indicados.
2. Inicializa `baterias` usando el constructor de tamaño con paréntesis `()` para crear 6 casillas inicializadas en cero.
3. Inicializa `raciones` usando el constructor con paréntesis `(3, 50)` para crear 3 casillas de 50 unidades cada una.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E03_InventarioDinamico.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
