// ============================================================================
// Laboratorio D02: BUG DEMO - UnreachableCodeBug
// ============================================================================
// Objetivo: Demostrar como un orden incorrecto genera codigo muerto.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D02_UnreachableCodeBug.cpp -o bug
// ============================================================================

#include <iostream>

int main() {
    int temperaturaAgua{100}; // El agua esta hirviendo!
    
    std::cout << "Analizando sensor de temperatura: " << temperaturaAgua << " grados.\n";
    
    // BUG INTENCIONAL: El orden esta invertido.
    // 100 es mayor que 0, asi que el primer IF se roba la ejecucion.
    if (temperaturaAgua > 0) {
        std::cout << "El agua esta en estado liquido. Seguro para nadar.\n";
    } else if (temperaturaAgua >= 100) {
        // CÓDIGO INALCANZABLE (Unreachable code)
        // El programa jamas entrara aqui, aunque haya 1000 grados.
        std::cout << "¡PELIGRO! Agua hirviendo. Evacuar zona.\n";
    } else {
        std::cout << "El agua esta congelada.\n";
    }
    
    std::cout << "Analisis terminado.\n";
    return 0;
}
