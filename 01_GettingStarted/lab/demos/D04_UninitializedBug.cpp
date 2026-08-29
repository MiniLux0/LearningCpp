// ============================================================================
// Laboratorio D04: BUG DEMO - Trampa de variables sin inicializar
// ============================================================================
// Objetivo: Demostrar los valores basura de la RAM al omitir la inicialización {}.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D04_UninitializedBug.cpp -o bug
// ============================================================================

#include <iostream>

int main() {
    // EL BUG: Variable declarada sin inicialización uniforme {}
    // Contendrá cualquier residuo de memoria binaria previa que haya estado en la RAM
    int puntajeJugador;
    
    std::cout << "--- Inicio del Juego ---\n";
    std::cout << "Puntaje actual: " << puntajeJugador << "\n";
    
    // Si sumas puntos a esta variable basura, el estado de la aplicación queda corrupto
    return 0;
}
