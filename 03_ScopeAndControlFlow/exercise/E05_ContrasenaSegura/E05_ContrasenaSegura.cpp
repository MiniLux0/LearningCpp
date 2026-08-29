// ============================================================================
// Reto E05: ContrasenaSegura
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    int pinCorrecto{1234};
    int intento{0};
    
    std::cout << "Terminal del bunker. Ingresa PIN: ";
    std::cin >> intento;
    
    // TODO: Mueve el std::cin hacia adentro del bucle usando un do-while
    // para evitar el bucle infinito.
    while (intento != pinCorrecto) {
        std::cout << "Acceso denegado. Intenta de nuevo.\n";
    }
    
    std::cout << "Acceso concedido. Bienvenido.\n";
    return 0;
}
