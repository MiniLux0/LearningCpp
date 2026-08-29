// ============================================================================
// Laboratorio D02: BUG DEMO - Constexpr vs Runtime
// ============================================================================
// Objetivo: Ver que pasa cuando intentas adivinar el futuro con constexpr.
//
// INSTRUCCIONES:
// Compila con `g++ D02_RuntimeConstexprBug.cpp -o bug`
// ============================================================================

#include <iostream>

int main() {
    int edadUsuario{0};
    
    std::cout << "Ingresa tu edad en anos: ";
    std::cin >> edadUsuario;
    
    // TRAMPA: Intentamos forzar una evaluacion en Compile-time (constexpr)
    // utilizando una variable 'edadUsuario' cuyo valor es estrictamente de 
    // Tiempo de Ejecucion (Runtime).
    // El compilador abortara la operacion porque no puede procesar un input en vivo.
    
    constexpr int mesesVividos{edadUsuario * 12}; 
    
    std::cout << "Has vivido " << mesesVividos << " meses.\n";
    
    return 0;
}
