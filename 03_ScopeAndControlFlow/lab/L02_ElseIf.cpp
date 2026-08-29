// ============================================================================
// Laboratorio L02: ElseIf
// ============================================================================
// Objetivo: Explorar el comportamiento en cascada de if y else if.
// ============================================================================

#include <iostream>

int main() {
    int poderHeroe{0};
    
    std::cout << "--- Escaner de Poder ---\n";
    std::cout << "Ingresa el nivel de poder del heroe: ";
    std::cin >> poderHeroe;
    
    // Las condiciones se evaluan en estricto orden descendente.
    if (poderHeroe > 9000) {
        std::cout << "¡Es mas de 9000! Nivel: Dios.\n";
    } else if (poderHeroe >= 5000) {
        std::cout << "Nivel: Heroe de Clase S.\n";
    } else if (poderHeroe >= 1000) {
        std::cout << "Nivel: Heroe Profesional.\n";
    } else if (poderHeroe >= 100) {
        std::cout << "Nivel: Novato destacado.\n";
    } else {
        std::cout << "Nivel: Ciudadano normal.\n";
    }
    
    return 0;
}
