# Reto E07: Creciendo Vectores

## Contexto
En la terminal de despegue hacia Marte, el sistema de embarque debe procesar los códigos de identificación (IDs) de los pasajeros. Sabemos que la nave tiene una capacidad fija de exactamente 5 pasajeros VIP en este vuelo.

Para garantizar la máxima velocidad de procesamiento en el procesador de la nave y evitar realocaciones repetidas en el Heap, debemos pre-reservar la capacidad necesaria usando `.reserve(5)`, insertar dinámicamente los IDs mediante `.push_back()`, verificar que el vector no esté vacío usando `.empty()` e inspeccionar el primer y último pasajero con `.front()` y `.back()`.

## Tu Misión
Abre el archivo `E07_CreciendoVectores.cpp`:
1. Optimiza el vector reservando espacio para 5 elementos con `pasajeros.reserve(5)`.
2. Inserta secuencialmente los siguientes 5 identificadores de pasajeros con `.push_back()`: `101`, `204`, `309`, `412`, `550`.
3. Comprueba mediante `!pasajeros.empty()` que la lista tiene datos.
4. Muestra en consola el tamaño final (`.size()`), la capacidad (`.capacity()`), el primer pasajero (`.front()`) y el último pasajero (`.back()`).

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E07_CreciendoVectores.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
