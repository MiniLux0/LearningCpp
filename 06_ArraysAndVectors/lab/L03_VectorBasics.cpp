// ============================================================================
// Laboratorio L03: Vector Basics (std::vector)
// ============================================================================
// Objetivo: Aprender a inicializar y consultar vectores dinamicos utilizando
//           la biblioteca estandar de C++ (<vector>).
// ============================================================================

#include <iostream>
#include <vector>

int main() {
    std::cout << "--- INICIALIZACION Y EXPLORACION DE STD::VECTOR ---\n";

    // 1. Vector vacio (size = 0)
    std::vector<int> vacio{};
    std::cout << "Vector vacio -> Tamano: " << vacio.size() << '\n';

    // 2. Vector con lista de inicializacion uniforme {} (size = 4)
    std::vector<int> niveles{10, 20, 30, 40};
    std::cout << "Vector niveles -> Tamano: " << niveles.size() << '\n';

    // 3. Vector con constructor de conteo () (size = 5 con ceros)
    std::vector<int> ceros(5);
    std::cout << "Vector ceros (5 casillas por defecto) -> Tamano: " << ceros.size() << '\n';

    // 4. Vector con conteo y valor especifico (3 casillas con valor 100)
    std::vector<int> vidas(3, 100);
    std::cout << "Vector vidas (3 casillas con valor 100) -> Tamano: " << vidas.size() << '\n';

    return 0;
}
