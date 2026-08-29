// ============================================================================
// Reto E05: ContrasenaSegura (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int pinCorrecto{1234};
    int intento{0};
    
    // SOLUCION: Usar do-while asegura que se pida el PIN al menos una vez,
    // y mantiene la peticion viva DENTRO de la habitacion (bloque) del bucle.
    do {
        std::cout << "Terminal del bunker. Ingresa PIN: ";
        std::cin >> intento;
        
        if (intento != pinCorrecto) {
            std::cout << "Acceso denegado. Intenta de nuevo.\n";
        }
    } while (intento != pinCorrecto);
    
    std::cout << "Acceso concedido. Bienvenido.\n";
    return 0;
}
