# Reto E04: El Índice Perdido

## Contexto
El telescopio espacial de espacio profundo *Hubble II* procesa señales astronómicas recibidas en un vector de frecuencias. El código original utilizaba el operador de subíndice desprotegido `[]` para leer las frecuencias críticas de los canales 0, 2 y 4.

Ayer, una ráfaga solar redujo el vector de frecuencias captadas a solo 3 elementos (índices 0, 1 y 2). Al intentar leer el canal con índice 4 usando `[]`, el programa leyó basura de la memoria y envió coordenadas corruptas a la antena principal, desorientando el satélite.

## Tu Misión
Abre el archivo `E04_ElIndicePerdido.cpp` y realiza las siguientes refactorizaciones:
1. Reemplaza todos los accesos con corchetes `[]` por el método seguro `.at()`.
2. Corrige los accesos para leer únicamente los índices válidos que existan dentro del tamaño del vector.
3. Actualiza el valor del canal central (índice 1) a `1420` (la frecuencia de la línea de hidrógeno) utilizando `.at(1) = 1420`.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E04_ElIndicePerdido.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
