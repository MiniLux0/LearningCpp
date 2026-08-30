// ============================================================================
// Laboratorio L08: Estadisticas.cpp (Implementacion)
// ============================================================================
// Objetivo: Definir la logica de las funciones declaradas en Estadisticas.h.
// ============================================================================

#include "Estadisticas.h"

double calcularSuma(const std::vector<double>& valores) {
    double suma{0.0};
    for (double v : valores) {
        suma += v;
    }
    return suma;
}

double calcularPromedio(const std::vector<double>& valores) {
    if (valores.empty()) {
        return 0.0;
    }
    return calcularSuma(valores) / static_cast<double>(valores.size());
}

double obtenerMaximo(const std::vector<double>& valores) {
    if (valores.empty()) {
        return 0.0;
    }
    double maximo{valores.at(0)};
    for (double v : valores) {
        if (v > maximo) {
            maximo = v;
        }
    }
    return maximo;
}

double obtenerMinimo(const std::vector<double>& valores) {
    if (valores.empty()) {
        return 0.0;
    }
    double minimo{valores.at(0)};
    for (double v : valores) {
        if (v < minimo) {
            minimo = v;
        }
    }
    return minimo;
}
