// ============================================================================
// Reto E08: Refactorizacion Header
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
//
// INSTRUCCIONES DE COMPILACION:
// g++ -std=c++17 -Wall -Wextra VectorUtils.cpp E08_RefactorizacionHeader.cpp -o app
// ============================================================================

#include <iostream>
#include <vector>
#include "VectorUtils.h"

int main() {
    std::cout << "--- PROCESAMIENTO MODULAR DE SENALES ---\n";

    std::vector<int> senales{45, 92, 18, 73, 105, 33};

    // Invocamos las funciones declaradas en VectorUtils.h y definidas en VectorUtils.cpp
    int suma = sumarElementos(senales);
    int maximo = encontrarMaximo(senales);

    std::cout << "Suma total de senales: " << suma << '\n';
    std::cout << "Senal de mayor potencia: " << maximo << '\n';

    return 0;
}
