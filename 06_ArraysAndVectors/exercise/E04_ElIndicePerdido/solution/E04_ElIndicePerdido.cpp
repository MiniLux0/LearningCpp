// ============================================================================
// Reto E04: El Indice Perdido (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- TELEMETRIA DEL TELESCOPIO ESPACIAL ---\n";

    std::vector<int> frecuencias{433, 868, 915}; // size = 3 (indices: 0, 1, 2)

    // Acceso verificado y seguro con .at()
    const int f0{frecuencias.at(0)};
    
    // Acceso seguro al ultimo elemento valido (indice 2)
    const int f2{frecuencias.at(2)};

    // Modificacion protegida con .at()
    frecuencias.at(1) = 1420;

    std::cout << "Canal 0: " << f0 << " MHz\n";
    std::cout << "Canal 1 (Modificado): " << frecuencias.at(1) << " MHz\n";
    std::cout << "Canal 2: " << f2 << " MHz\n";

    return 0;
}
