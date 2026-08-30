// ============================================================================
// Reto E08: VectorUtils.cpp (Implementacion)
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include "VectorUtils.h"

int sumarElementos(const std::vector<int>& v) {
    // TODO 1: Implementa la suma de todos los elementos del vector usando range-based for
    int suma{0};
    for (int num : v) {
        suma += num;
    }
    return suma;
}

int encontrarMaximo(const std::vector<int>& v) {
    // TODO 2: Implementa la busqueda del valor maximo
    if (v.empty()) {
        return 0;
    }
    int maximo{v.at(0)};
    for (int num : v) {
        if (num > maximo) {
            maximo = num;
        }
    }
    return maximo;
}
