// ============================================================================
// Reto E02: Protección contra Narrowing
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Estadisticas del Jugador ---\n";

    // TODO 1: Cambia estos '=' por '{}'. Intenta compilar para ver el error.
    // TODO 2: Arregla los tipos de dato para que los valores quepan perfectamente.
    
    int salud_porcentaje = 99.5;      // ¡Peligro de narrowing!
    int multiplicador_dano = 1.25;    // ¡Peligro de narrowing!
    int nivel = 5;                    // Este está bien, pero usa la sintaxis vieja.

    std::cout << "Salud: " << salud_porcentaje << "%\n";
    std::cout << "Multiplicador de dano: x" << multiplicador_dano << "\n";
    std::cout << "Nivel: " << nivel << "\n";

    return 0;
}
