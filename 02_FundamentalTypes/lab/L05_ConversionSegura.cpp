// ============================================================================
// Laboratorio L05: Conversión Segura (static_cast)
// ============================================================================
// Objetivo: Descubrir cómo rescatar decimales de una división de enteros transformando un tipo de dato en otro de manera segura.
// ============================================================================

#include <iostream>

int main() {
    int total_puntos{450};
    int partidas_jugadas{7};

    std::cout << "--- Estadisticas del Jugador ---\n";
    std::cout << "Puntos totales: " << total_puntos << "\n";
    std::cout << "Partidas jugadas: " << partidas_jugadas << "\n\n";

    // 1. El problema: Division entera
    // Como ambos operandos son int, C++ descarta los decimales (450 / 7 = 64.28...)
    int promedio_entero{total_puntos / partidas_jugadas};
    std::cout << "Promedio (Division Entera - INEXACTO): " << promedio_entero << "\n";

    // Incluso si lo guardamos en un double, ya se perdieron los decimales
    double promedio_falso{total_puntos / partidas_jugadas};
    std::cout << "Promedio Falso (Sigue perdiendo datos): " << promedio_falso << "\n\n";

    // 2. La solucion: static_cast
    // Convertimos temporalmente 'total_puntos' a double.
    // Double entre int = double.
    double promedio_real{static_cast<double>(total_puntos) / partidas_jugadas};
    
    std::cout << "Promedio Real (Con static_cast - EXACTO): " << promedio_real << "\n";

    return 0;
}
