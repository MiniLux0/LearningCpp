// ============================================================================
// Laboratorio L02: Constexpr
// ============================================================================
// Objetivo: Aprender a usar constexpr para delegar calculos matematicos al compilador.
// ============================================================================

#include <iostream>

int main() {
    // 1. Valores conocidos en Tiempo de Compilacion (Compile-time)
    // El compilador interpretara 'diasSemana' directamente como el numero 7.
    constexpr int diasSemana{7};
    constexpr int horasPorDia{24};
    
    // 2. Optimizacion estatica de expresiones.
    // El compilador resolvera matematicamente 7 * 24 ANTES de crear el ejecutable.
    // Durante el Runtime, la CPU no invertira ciclos en procesar esta multiplicacion.
    constexpr int horasPorSemana{diasSemana * horasPorDia};
    
    std::cout << "Un ano tiene " << 52 << " semanas.\n";
    std::cout << "Horas totales por semana: " << horasPorSemana << '\n';
    
    return 0;
}
