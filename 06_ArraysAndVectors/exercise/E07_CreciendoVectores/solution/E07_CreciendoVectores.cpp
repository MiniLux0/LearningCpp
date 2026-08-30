// ============================================================================
// Reto E07: Creciendo Vectores (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- SISTEMA DE EMBARQUE MARTE I ---\n";

    std::vector<int> pasajeros{};

    // 1. Pre-reserva en el Heap para evitar realocaciones sucesivas
    pasajeros.reserve(5);

    // 2. Insercion dinamica al final
    pasajeros.push_back(101);
    pasajeros.push_back(204);
    pasajeros.push_back(309);
    pasajeros.push_back(412);
    pasajeros.push_back(550);

    // 3. Consulta de tamano y capacidad
    std::cout << "Pasajeros abordados (size):     " << pasajeros.size() << '\n';
    std::cout << "Capacidad reservada (capacity): " << pasajeros.capacity() << '\n';

    // 4. Consulta semantica de estado y extremos
    if (!pasajeros.empty()) {
        std::cout << "Primer pasajero abordado: " << pasajeros.front() << '\n';
        std::cout << "Ultimo pasajero abordado: " << pasajeros.back() << '\n';
    }

    return 0;
}
