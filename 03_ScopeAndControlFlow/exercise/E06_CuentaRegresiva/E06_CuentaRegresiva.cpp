// ============================================================================
// Reto E06: CuentaRegresiva
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Preparando lanzamiento orbital...\n";
    std::cout << "Iniciando reloj:\n";
    
    // TODO: El bucle actual suma en lugar de restar, y su limite es un peligro.
    // Ajusta la anatomia del for para que cuente desde 10 bajando hasta 1.
    for (int reloj{10}; reloj < 0; reloj = reloj + 1) {
        std::cout << "T-Minus " << reloj << "...\n";
    }
    
    std::cout << "¡IGNICION! Cohete en el aire.\n";
    return 0;
}
