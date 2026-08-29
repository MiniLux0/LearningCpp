// ============================================================================
// Reto E01: Asegurando Inventario (SOLUCION)
// ============================================================================

#include <iostream>

int main() {
    // Variables arquitectonicas protegidas (Read-only) e inicializadas uniformemente
    const int maxJugadores{4};
    const int idJefeFinal{99};

    // La siguiente linea esta comentada porque al intentar mutar una 
    // direccion de memoria 'const', el compilador aborta el programa, previniendo el bug.
    // maxJugadores = 50; 
    
    std::cout << "El limite de jugadores es: " << maxJugadores << '\n';
    std::cout << "ID del Jefe: " << idJefeFinal << '\n';

    return 0;
}
