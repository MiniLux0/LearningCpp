// ============================================================================
// Laboratorio L04: Acceso Seguro (.at() vs [])
// ============================================================================
// Objetivo: Comparar el acceso por subindice [] con el metodo seguro .at()
//           comprobando la verificacion de limites en std::vector.
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- ACCESO VERIFICADO CON .AT() ---\n";

    std::vector<int> inventario{50, 120, 300}; // size = 3 (indices 0, 1, 2)

    // Lectura segura con .at()
    std::cout << "Elemento en indice 0: " << inventario.at(0) << '\n';
    std::cout << "Elemento en indice 1: " << inventario.at(1) << '\n';
    std::cout << "Elemento en indice 2: " << inventario.at(2) << '\n';

    // Modificacion segura mediante .at()
    inventario.at(1) = 150;
    std::cout << "Elemento en indice 1 actualizado: " << inventario.at(1) << '\n';

    std::cout << "\nTamano actual del vector: " << inventario.size() << '\n';
    std::cout << "Acceso completado con exito sin violaciones de limites.\n";

    return 0;
}
