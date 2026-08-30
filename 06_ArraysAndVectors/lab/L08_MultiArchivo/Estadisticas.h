// ============================================================================
// Laboratorio L08: Estadisticas.h (Interfaz Publica)
// ============================================================================
// Objetivo: Declarar funciones estadisticas para vectores de datos numericos.
// ============================================================================

#pragma once
#include <vector>

// Declaracion de prototipos de funciones
double calcularSuma(const std::vector<double>& valores);
double calcularPromedio(const std::vector<double>& valores);
double obtenerMaximo(const std::vector<double>& valores);
double obtenerMinimo(const std::vector<double>& valores);
