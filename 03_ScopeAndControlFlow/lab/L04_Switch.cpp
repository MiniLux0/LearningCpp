// ============================================================================
// Laboratorio L04: Switch
// ============================================================================
// Objetivo: Observar el comportamiento normal de un switch y la utilidad de 'default'.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "=== MENU DE CAFE ===\n";
    std::cout << "1. Cafe Solo\n";
    std::cout << "2. Cortado\n";
    std::cout << "3. Capuchino\n";
    std::cout << "Elige una opcion (1-3): ";
    
    int eleccion{0};
    std::cin >> eleccion;
    
    switch (eleccion) {
        case 1:
            std::cout << "Preparando un Cafe Solo oscuro y fuerte.\n";
            break;
        case 2:
            std::cout << "Preparando un Cortado con un toque de leche.\n";
            break;
        case 3:
            std::cout << "Preparando un Capuchino con mucha espuma.\n";
            break;
        default:
            std::cout << "Opcion invalida. Por favor, selecciona 1, 2 o 3.\n";
            break;
    }
    
    std::cout << "Gracias por tu visita.\n";
    return 0;
}
