// ============================================================================
// Laboratorio D07: BUG DEMO - HiddenInfiniteLoopBug
// ============================================================================
// Objetivo: Mostrar el temido bug del continue en un while que omite el incremento.
//
// INSTRUCCIONES:
// Compila con `g++ D07_HiddenInfiniteLoopBug.cpp -o bug`
// ¡Prepara Ctrl+C para matar el programa cuando se cuelgue!
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Escaneando sectores de memoria del 1 al 5...\n";
    
    int sector{1};
    
    while (sector <= 5) {
        
        if (sector == 3) {
            std::cout << "Sector 3 corrupto. Saltando...\n";
            // BUG INTENCIONAL: Se invoca continue ANTES de la mutacion de estado (incremento).
            // Al omitir la mutacion, el bucle iterara estaticamente en el sector 3, causando un Bucle Infinito Silencioso.
            continue; 
        }
        
        std::cout << "Sector " << sector << " escaneado correctamente.\n";
        
        // El incremento esta al final, ¡pero el continue se lo salta!
        sector = sector + 1;
    }
    
    std::cout << "Escaneo completo.\n";
    return 0;
}
