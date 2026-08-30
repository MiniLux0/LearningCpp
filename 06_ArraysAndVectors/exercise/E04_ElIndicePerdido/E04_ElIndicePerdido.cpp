// ============================================================================
// Reto E04: El Indice Perdido
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- TELEMETRIA DEL TELESCOPIO ESPACIAL ---\n";

    std::vector<int> frecuencias{433, 868, 915}; // size = 3 (indices: 0, 1, 2)

    // TODO 1: Reemplaza el uso de [] por el metodo seguro .at()
    int f0 = frecuencias[0];
    int f1 = frecuencias[1];
    
    // TODO 2: Corrige este acceso peligroso fuera de rango:
    // El vector solo tiene 3 elementos. Reemplaza frecuencias[4] por frecuencias.at(2)
    int f2 = frecuencias[4];

    // TODO 3: Modifica la frecuencia del indice 1 usando .at(1) = 1420
    frecuencias[1] = 1420;

    std::cout << "Canal 0: " << f0 << " MHz\n";
    std::cout << "Canal 1 (Modificado): " << frecuencias.at(1) << " MHz\n";
    std::cout << "Canal 2: " << f2 << " MHz\n";

    return 0;
}
