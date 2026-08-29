// ============================================================================
// Reto E01: Asegurando Inventario
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    // TODO 1: Vuelve inmutables estas variables usando 'const' e inicializacion uniforme {}
    int maxJugadores = 4;
    int idJefeFinal = 99;

    // TODO 2: Una vez que apliques 'const' arriba, el compilador abortara
    // el proceso al encontrar esta reasignacion. Comenta o elimina esta linea.
    maxJugadores = 50; 
    
    std::cout << "El limite de jugadores es: " << maxJugadores << '\n';
    std::cout << "ID del Jefe: " << idJefeFinal << '\n';

    return 0;
}
