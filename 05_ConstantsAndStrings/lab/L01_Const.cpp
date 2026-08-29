// ============================================================================
// Laboratorio L01: Inmutabilidad con Const
// ============================================================================
// Objetivo: Aprender a implementar 'Const Correctness' para evitar
//           modificaciones accidentales en direcciones de memoria criticas.
// ============================================================================

#include <iostream>

int main() {
    // 1. Variable de estado mutable
    int nivelDelJugador{1};
    std::cout << "Nivel inicial: " << nivelDelJugador << '\n';

    // Se puede reasignar su valor durante el ciclo de vida del programa
    nivelDelJugador = 2;
    std::cout << "Nivel actual tras ganar experiencia: " << nivelDelJugador << '\n';

    // 2. Variable inmutable (Read-only)
    // El limite arquitectonico de niveles no debe mutar en tiempo de ejecucion.
    const int nivelMaximo{100};
    std::cout << "El nivel maximo permitido es: " << nivelMaximo << '\n';

    // Descomenta la siguiente linea para observar el bloqueo del compilador:
    // nivelMaximo = 101; 

    // Al intentar compilar con la linea anterior activa, el compilador 
    // abortara arrojando un error de tipo "assignment of read-only variable".

    return 0;
}
