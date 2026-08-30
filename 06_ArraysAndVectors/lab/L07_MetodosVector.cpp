// ============================================================================
// Laboratorio L07: Metodos Esenciales y Capacidad en std::vector
// ============================================================================
// Objetivo: Inspeccionar los metodos de insercion, extraccion, tamano y
//           capacidad de memoria en el Heap (size vs capacity).
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- METODOS DINAMICOS Y GESTION DE MEMORIA ---\n";

    std::vector<int> datos{};
    std::cout << "Vector inicial -> Size: " << datos.size() 
              << " | Capacity: " << datos.capacity() 
              << " | Empty: " << (datos.empty() ? "Si" : "No") << '\n';

    // Insercion dinamica con push_back
    std::cout << "\nInsertando elementos con push_back():\n";
    for (int i{1}; i <= 5; ++i) {
        datos.push_back(i * 10);
        std::cout << "Insertado: " << i * 10 
                  << " -> Size: " << datos.size() 
                  << " | Capacity: " << datos.capacity() << '\n';
    }

    // Consulta de extremos
    std::cout << "\nPrimer elemento (.front()): " << datos.front() << '\n';
    std::cout << "Ultimo elemento (.back()): " << datos.back() << '\n';

    // Eliminacion del ultimo elemento
    datos.pop_back();
    std::cout << "\nDespues de pop_back() -> Size: " << datos.size() 
              << " | Ultimo elemento: " << datos.back() << '\n';

    // Demostracion de .reserve()
    std::vector<int> optimizado{};
    optimizado.reserve(100);
    std::cout << "\nVector optimizado con reserve(100) -> Size: " << optimizado.size() 
              << " | Capacity: " << optimizado.capacity() << '\n';

    // Limpieza total
    datos.clear();
    std::cout << "Despues de clear() -> Size: " << datos.size() 
              << " | Capacity: " << datos.capacity() 
              << " | Empty: " << (datos.empty() ? "Si" : "No") << '\n';

    return 0;
}
