// ============================================================================
// Reto E04: Saludo Interactivo (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string>

int main() {
    // 1. Inicialización uniforme {} que previene variables basura en RAM
    std::string nombre{""};
    int edad{0};

    // 2. Extracción de datos con std::cin
    std::cout << "Escribe tu primer nombre: ";
    std::cin >> nombre;

    std::cout << "Escribe tu edad: ";
    std::cin >> edad;

    // 3. Encadenando variables y texto en el mismo cout
    std::cout << "\nHola, " << nombre << "! Tienes " << edad << " anios.\n";

    return 0;
}
