# Reto E05: Atrapando la Bomba

## Contexto
El banco central de la metrópoli gestiona una terminal de transferencias que consulta saldos de cuentas en un vector de registros. Cuando un cliente ingresa un número de cuenta que no existe en el sistema, la consulta con `.at()` detona una excepción `std::out_of_range`.

Sin un mecanismo de contención, la excepción no atrapada hace que el sistema operativo mate el proceso del banco, apagando los cajeros automáticos de toda la ciudad. Tu misión es instalar un blindaje táctico con `try / catch` para contener el error, emitir una advertencia al usuario y permitir que el programa continúe funcionando.

## Tu Misión
Abre el archivo `E05_AtrapandoLaBomba.cpp`:
1. Envuelve la lectura de la cuenta con `.at(idCuenta)` dentro de un bloque `try`.
2. Implementa el bloque `catch (const std::out_of_range& error)` para capturar la excepción en caso de que el índice no exista.
3. Dentro del `catch`, imprime un mensaje de error claro y muestra el diagnóstico técnico utilizando `error.what()`.
4. Asegúrate de que el mensaje final `"El servidor bancario permanece en linea."` se imprima siempre sin interrupciones.

## 💻 Compilación y Ejecución
```bash
g++ -std=c++17 -Wall -Wextra E05_AtrapandoLaBomba.cpp -o app
./app
```

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
