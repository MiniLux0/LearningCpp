// ============================================================================
// Laboratorio D01: BUG DEMO - IfSemicolonBug
// ============================================================================
// Objetivo: Demostrar como un simple punto y coma destruye el control de flujo.
//
// INSTRUCCIONES:
// Compila con `g++ D01_IfSemicolonBug.cpp -o bug`
// ============================================================================

#include <iostream>

int main() {
    int municionRestante{0};
    
    std::cout << "Jugador intentando disparar con municion: " << municionRestante << "\n";
    
    // BUG INTENCIONAL: Nota el punto y coma al final de esta linea.
    if (municionRestante > 0); 
    {
        std::cout << "BANG! Disparo exitoso.\n";
    }
    
    std::cout << "Fin del turno.\n";
    
    return 0;
}
