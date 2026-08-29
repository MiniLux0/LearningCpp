// ============================================================================
// Reto E02: Protección contra Narrowing (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Estadisticas del Jugador ---\n";

    // 1. Las llaves de inicialización forzaron a cambiar 'int' por 'double'
    //    para no perder los decimales (99.5 y 1.25).
    double salud_porcentaje{99.5};     
    double multiplicador_dano{1.25};   

    // 2. El nivel se queda como 'int', pero se actualizó a llaves modernas.
    int nivel{5};                      

    std::cout << "Salud: " << salud_porcentaje << "%\n";
    std::cout << "Multiplicador de dano: x" << multiplicador_dano << "\n";
    std::cout << "Nivel: " << nivel << "\n";

    return 0;
}
