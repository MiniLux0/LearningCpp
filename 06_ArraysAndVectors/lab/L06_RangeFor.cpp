// ============================================================================
// Laboratorio L06: Recorridos con Range-based For
// ============================================================================
// Objetivo: Aprender a iterar sobre vectores de forma idiomatica y segura
//           sin necesidad de gestionar variables de indice manuales.
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- ITERACION MODERNA CON RANGE-BASED FOR ---\n";

    std::vector<int> velocidades{60, 80, 100, 120, 140};

    // 1. Recorrido clasico con indices
    std::cout << "Recorrido clasico con indices:\n";
    for (std::size_t i{0}; i < velocidades.size(); ++i) {
        std::cout << "  Velocidad en posicion " << i << ": " << velocidades.at(i) << " km/h\n";
    }

    // 2. Recorrido idiomatico moderno (Range-based for)
    std::cout << "\nRecorrido moderno (range-based for):\n";
    for (int v : velocidades) {
        std::cout << "  Velocidad: " << v << " km/h\n";
    }

    // Calculo acumulativo directo con range-based for
    int sumaVelocidades{0};
    for (int v : velocidades) {
        sumaVelocidades += v;
    }

    std::cout << "\nSuma total de velocidades: " << sumaVelocidades << " km/h\n";
    std::cout << "Promedio: " << static_cast<double>(sumaVelocidades) / static_cast<double>(velocidades.size()) << " km/h\n";

    return 0;
}
