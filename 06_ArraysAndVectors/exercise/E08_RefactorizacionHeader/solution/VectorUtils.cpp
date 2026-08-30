// ============================================================================
// Reto E08: VectorUtils.cpp (SOLUCION)
// ============================================================================

#include "VectorUtils.h"

int sumarElementos(const std::vector<int>& v) {
    int suma{0};
    for (int num : v) {
        suma += num;
    }
    return suma;
}

int encontrarMaximo(const std::vector<int>& v) {
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
