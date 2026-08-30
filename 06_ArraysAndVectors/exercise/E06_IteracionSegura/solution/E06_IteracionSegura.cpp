// ============================================================================
// Reto E06: Iteracion Segura (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- PROCESADOR SISMOLOGICO AUTOMATIZADO ---\n";

    const std::vector<double> sismos{3.2, 5.8, 2.1, 6.4, 4.0, 7.1};

    double sumaIntensidad{0.0};
    int sismosPeligrosos{0};

    // 1. Recorrido seguro con range-based for para acumulacion
    for (double s : sismos) {
        sumaIntensidad += s;
    }

    // 2. Recorrido seguro con range-based for para conteo condicional
    for (double s : sismos) {
        if (s > 5.0) {
            ++sismosPeligrosos;
        }
    }

    double promedio{0.0};
    if (!sismos.empty()) {
        promedio = sumaIntensidad / static_cast<double>(sismos.size());
    }

    std::cout << "Total de sismos registrados: " << sismos.size() << '\n';
    std::cout << "Intensidad promedio: " << promedio << '\n';
    std::cout << "Sismos sobre umbral critico (> 5.0): " << sismosPeligrosos << '\n';

    return 0;
}
