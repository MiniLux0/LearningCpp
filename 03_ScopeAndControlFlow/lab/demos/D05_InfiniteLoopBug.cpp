// ============================================================================
// Laboratorio D05: BUG DEMO - InfiniteLoopBug
// ============================================================================
// Objetivo: Mostrar el peligro de olvidar modificar la variable de control.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D05_InfiniteLoopBug.cpp -o bug
// ¡Prepara Ctrl+C para matar el programa cuando se cuelgue!
// ============================================================================

#include <iostream>

int main() {
    int bateriaRobo{100};
    
    std::cout << "Iniciando aspiradora robot...\n";
    
    while (bateriaRobo > 0) {
        std::cout << "Limpiando el cuarto... Bateria al " << bateriaRobo << "%\n";
        
        // BUG INTENCIONAL: Omision de mutacion de estado.
        // bateriaRobo = bateriaRobo - 10;
        
        // La expresion nunca evaluara a false. Colapso por bucle infinito.
    }
    
    std::cout << "Robot apagado.\n";
    return 0;
}
