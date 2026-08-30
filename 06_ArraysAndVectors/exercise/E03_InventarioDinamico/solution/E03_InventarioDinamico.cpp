// ============================================================================
// Reto E03: Inventario Dinamico (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- INICIALIZACION DEL INVENTARIO DE LA NAVE ---\n";

    // 1. Inicializacion uniforme {} con valores especificos
    const std::vector<int> oxigeno{95, 98, 100, 92};

    // 2. Inicializacion con constructor de conteo (6 casillas en cero)
    const std::vector<int> baterias(6);

    // 3. Inicializacion con constructor de conteo y valor (3 casillas de 50)
    const std::vector<int> raciones(3, 50);

    std::cout << "Oxigeno registrado -> Tamano: " << oxigeno.size() << '\n';
    std::cout << "Baterias activas   -> Tamano: " << baterias.size() << '\n';
    std::cout << "Raciones listas    -> Tamano: " << raciones.size() << '\n';

    return 0;
}
