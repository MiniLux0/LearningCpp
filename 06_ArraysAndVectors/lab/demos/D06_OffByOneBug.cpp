// ============================================================================
// Laboratorio D06: BUG DEMO - Error Off-By-One en Bucle Tradicional
// ============================================================================
// Objetivo: Demostrar el fallo de limites al utilizar <= en lugar de < en la
//           condicion de parada de un bucle for tradicional.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D06_OffByOneBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>

int main() {
    std::cout << "--- DEMO DE BUG: ERROR OFF-BY-ONE EN BUCLE ---\n";

    std::vector<int> puntos{5, 10, 15}; // size = 3 (indices: 0, 1, 2)

    std::cout << "Recorriendo vector con error <= puntos.size()...\n";

    try {
        // [FALLO] ERROR OFF-BY-ONE: La condicion i <= puntos.size() intentara
        // evaluar i = 3 cuando puntos.size() == 3. El indice 3 no existe.
        for (std::size_t i{0}; i <= puntos.size(); ++i) {
            std::cout << "Indice [" << i << "]: " << puntos.at(i) << '\n';
        }
    }
    catch (const std::out_of_range& error) {
        std::cout << "\n[COLAPSO DETECTADO] El bucle intento acceder fuera de limites:\n";
        std::cout << "Diagnostico tecnico: " << error.what() << '\n';
    }

    std::cout << "\nConclusion: Range-based for elimina este error al no requerir condiciones manuales.\n";
    return 0;
}
