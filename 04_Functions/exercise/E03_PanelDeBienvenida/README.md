# Reto E03: Panel de Bienvenida

## La Misión

Estás desarrollando el software para los terminales de auto-servicio de un hotel de lujo.
Al iniciar sesión, el sistema debe imprimir un panel enorme con gráficos hechos de texto (ASCII Art).

El problema es doble:
1. El programador anterior escribió todas las líneas de dibujo (`cout`) directamente dentro del `main()`, volviéndolo ilegible.
2. Peor aún, en un intento de delegar el trabajo, intentó extraer parte del código a una rutina, pero **intentó inicializar una variable `int` asignándole el llamado de la rutina**, lo cual corrompió el compilador por ser un retorno incompleto (`void`).

Tu misión es refactorizar este desastre arquitectónico.

### Reglas de Oro:
1. Mueve TODO el código de impresión (Efecto Secundario) del banner del hotel a una nueva rutina aislada que se llame `imprimirBanner`.
2. Como esta función solo ejecuta una acción y no transfiere datos de regreso, **su firma de retorno debe ser estrictamente `void`**.
3. Asegúrate de invocar `imprimirBanner()` desde el `main()` como una instrucción independiente, sin intentar asignar su ejecución a la memoria.

### ⚙️ Instrucciones de Compilación

Compila tu solución desde la terminal con:
```bash
g++ -std=c++17 E03_PanelDeBienvenida.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
