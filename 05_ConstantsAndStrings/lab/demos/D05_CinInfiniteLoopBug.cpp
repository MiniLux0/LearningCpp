// ============================================================================
// Laboratorio D05: BUG DEMO - Bucle Infinito de la Muerte
// ============================================================================
// Objetivo: Observar un bucle infinito provocado por un buffer de entrada corrompido.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D05_CinInfiniteLoopBug.cpp -o bug
// Al ejecutar, escribe una palabra (ej. "hola") en lugar de un numero.
// PREPARATE PARA PULSAR [Ctrl + C] en tu terminal para detener el bucle infinito.
// ============================================================================

#include <iostream>

int main() {
    int nivel{0};
    bool nivelValido{false};
    
    // Un bucle aparentemente inocente esperando un numero
    while (nivelValido == false) {
        std::cout << "Ingresa un nivel del 1 al 10: ";
        std::cin >> nivel;
        
        // TRAMPA FATAL: Si el usuario escribe texto, ocurre una falla de extraccion.
        // Al no restablecer el estado (clear) ni vaciar el buffer (ignore),
        // std::cin fallara silenciosamente en cada iteracion del bucle 
        // e imprimira este mensaje miles de veces por segundo, bloqueando tu PC.
        
        if (nivel > 0 && nivel <= 10) {
            nivelValido = true;
        } else {
            std::cout << "Nivel invalido, intenta de nuevo.\n";
        }
    }

    std::cout << "Juego iniciado.\n";

    return 0;
}
