# Reto E01: El Constructor de Saludos

## La Misión

Has sido contratado para programar la inteligencia de un robot mayordomo. Su trabajo principal es saludar a los invitados de una fiesta según su nivel de prioridad (1 = VIP, 2 = Normal, 3 = Intruso).

El problema es que el ingeniero anterior puso **toda la lógica de saludo dentro del `main()`**, lo que hace que el código sea un bloque masivo y difícil de leer, especialmente porque tiene que saludar a 3 personas distintas.

Tu misión es **Refactorizar (Delegar)**:
1. Extraer la lógica de saludo hacia una nueva función llamada `saludarInvitado`.
2. Esa función debe recibir dos parámetros: el `std::string` con el nombre de la persona, y un `int` con el nivel de prioridad.
3. El `main()` debe quedar completamente limpio, limitándose a llamar a la función tres veces con diferentes personas.

### Reglas de Oro:
1. La función debe llamarse `saludarInvitado`.
2. Debe ir construida obligatoriamente **arriba** del `main()`.
3. Debe usar un `switch` o `if/else if` en su interior para determinar el tipo de saludo según la prioridad.
