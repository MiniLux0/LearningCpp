// ============================================================================
// Reto E01: Tipos y Memoria (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    // 1. Declaración con inicialización uniforme {}
    int    puntos{100};
    double gravedad{9.81};
    char   inicial{'M'};
    bool   juego_terminado{false};

    // 2. Impresión de valores y uso de sizeof() sobre las variables
    std::cout << "Variable 'puntos' vale " << puntos 
              << " y ocupa " << sizeof(puntos) << " bytes.\n";

    std::cout << "Variable 'gravedad' vale " << gravedad 
              << " y ocupa " << sizeof(gravedad) << " bytes.\n";

    std::cout << "Variable 'inicial' vale " << inicial 
              << " y ocupa " << sizeof(inicial) << " bytes.\n";

    std::cout << "Variable 'juego_terminado' vale " << juego_terminado 
              << " y ocupa " << sizeof(juego_terminado) << " bytes.\n";

    return 0;
}
