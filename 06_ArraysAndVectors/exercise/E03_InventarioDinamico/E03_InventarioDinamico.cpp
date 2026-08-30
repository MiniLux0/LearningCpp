// ============================================================================
// Reto E03: Inventario Dinamico
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- INICIALIZACION DEL INVENTARIO DE LA NAVE ---\n";

    // TODO 1: Inicializa 'oxigeno' con una lista uniforme {} que contenga: 95, 98, 100, 92
    std::vector<int> oxigeno{};

    // TODO 2: Inicializa 'baterias' con parentesis () para reservar 6 casillas en cero
    std::vector<int> baterias{};

    // TODO 3: Inicializa 'raciones' con parentesis (3, 50) para crear 3 casillas de 50
    std::vector<int> raciones{};

    std::cout << "Oxigeno registrado -> Tamano: " << oxigeno.size() << '\n';
    std::cout << "Baterias activas   -> Tamano: " << baterias.size() << '\n';
    std::cout << "Raciones listas    -> Tamano: " << raciones.size() << '\n';

    return 0;
}
