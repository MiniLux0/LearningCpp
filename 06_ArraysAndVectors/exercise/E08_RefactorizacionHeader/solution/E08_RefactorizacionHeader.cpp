// ============================================================================
// Reto E08: Refactorizacion Header (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>
#include "VectorUtils.h"

int main() {
    std::cout << "--- PROCESAMIENTO MODULAR DE SENALES ---\n";

    const std::vector<int> senales{45, 92, 18, 73, 105, 33};

    const int suma{sumarElementos(senales)};
    const int maximo{encontrarMaximo(senales)};

    std::cout << "Suma total de senales: " << suma << '\n';
    std::cout << "Senal de mayor potencia: " << maximo << '\n';

    return 0;
}
