# Reto E05: Fuga de Aislamiento (Scope)

## La Misión

Estás desarrollando el software para las puertas automáticas de un laboratorio de alto riesgo.

El sistema invoca una rutina encargada de escanear la tarjeta del empleado y procesar un `nivel_de_acceso` (1, 2 o 3). 
El problema arquitectónico es que el programador novato alojó la variable `nivel_de_acceso` exclusivamente en el bloque local de la función `escanearTarjeta()`. 

Cuando el Scope principal (`main()`) intenta leer esa variable para auditar los permisos lógicos, el compilador aborta el proceso de construcción, ya que el identificador invocable no existe en su entorno de memoria (*not declared in this scope*). ¡El código ni siquiera compila!

Tu misión es arreglar el flujo de retorno para que la puerta vuelva a funcionar.

### Reglas de Oro:
1. No modifiques el algoritmo interno de `escanearTarjeta()`.
2. Modifica la firma de la función para que **inyecte (retorne)** el nivel calculado hacia el Scope externo usando `return`.
3. Intercepta el flujo de retorno en el `main()` inicializando una variable local que almacene la transferencia del dato.

### ⚙️ Instrucciones de Compilación

Compila tu solución desde la terminal con:
```bash
g++ -std=c++17 E05_CamaraDeAislamiento.cpp -o app
./app
```

---
<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
