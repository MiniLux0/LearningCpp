// ============================================================================
// Reto E06: Iteracion Segura
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- PROCESADOR SISMOLOGICO AUTOMATIZADO ---\n";

    std::vector<double> sismos{3.2, 5.8, 2.1, 6.4, 4.0, 7.1};

    double sumaIntensidad{0.0};
    int sismosPeligrosos{0};

    // TODO 1: Reemplaza bucles tradicionales por un range-based for
    // que acumule la suma de todos los valores en 'sumaIntensidad'.
    // for (double s : sismos) ...

    // TODO 2: Con otro range-based for, incrementa 'sismosPeligrosos'
    // para todo sismo estrictamente mayor a 5.0.

    double promedio{0.0};
    if (!sismos.empty()) {
        promedio = sumaIntensidad / static_cast<double>(sismos.size());
    }

    std::cout << "Total de sismos registrados: " << sismos.size() << '\n';
    std::cout << "Intensidad promedio: " << promedio << '\n';
    std::cout << "Sismos sobre umbral critico (> 5.0): " << sismosPeligrosos << '\n';

    return 0;
}
