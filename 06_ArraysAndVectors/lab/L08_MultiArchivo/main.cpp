// ============================================================================
// Laboratorio L08: main.cpp (Consumidor del Modulo)
// ============================================================================
// Objetivo: Consumir las funciones del modulo Estadisticas mediante su cabecera.
//
// INSTRUCCIONES DE COMPILACION:
// g++ -std=c++17 -Wall -Wextra Estadisticas.cpp main.cpp -o app
// ============================================================================

#include <iostream>
#include <vector>
#include "Estadisticas.h"

int main() {
    std::cout << "--- PROYECTO MULTI-ARCHIVO: ESTADISTICAS ---\n";

    std::vector<double> mediciones{14.5, 18.0, 12.5, 20.0, 16.0};

    std::cout << "Cantidad de datos procesados: " << mediciones.size() << '\n';
    std::cout << "Suma total: " << calcularSuma(mediciones) << '\n';
    std::cout << "Promedio: " << calcularPromedio(mediciones) << '\n';
    std::cout << "Valor Maximo: " << obtenerMaximo(mediciones) << '\n';
    std::cout << "Valor Minimo: " << obtenerMinimo(mediciones) << '\n';

    return 0;
}
