// ============================================================================
// Laboratorio D06: BUG DEMO - OffByOneBug
// ============================================================================
// Objetivo: Mostrar el temido error "por uno" al confundir <= con <
//
// INSTRUCCIONES:
// Compila con `g++ D06_OffByOneBug.cpp -o bug`
// ============================================================================

#include <iostream>

int main() {
    int capacidadElevador{5};
    int personasSubidas{0};
    
    std::cout << "El sistema admite un limite maximo de iteracion de " << capacidadElevador << " personas.\n";
    std::cout << "Iniciando abordaje...\n";
    
    // BUG INTENCIONAL: El buffer de memoria esta indexado en base-0.
    // Sin embargo, la iteracion usa un limite inclusivo (<= 5).
    // Esto genera 6 iteraciones (0, 1, 2, 3, 4, 5),
    // desencadenando un Buffer Overflow.
    
    for (int i{0}; i <= capacidadElevador; i = i + 1) {
        std::cout << "Ocupando bloque de memoria (Index " << i << ").\n";
        personasSubidas = personasSubidas + 1;
    }
    
    std::cout << "\nTotal de bloques ocupados: " << personasSubidas << "\n";
    
    if (personasSubidas > capacidadElevador) {
        std::cout << "CRITICAL ERROR: Buffer Overflow detectado. Fuera de limites.\n";
    }
    
    return 0;
}
