// ============================================================================
// Reto E07: BuscadorDeArchivos
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Conectando al servidor corporativo...\n";
    
    for (int archivo{1}; archivo <= 20; archivo = archivo + 1) {
        
        // TODO 1: Si el archivo es el 13, imprime "Malware detectado. Saltando..." 
        // y usa continue para evitar extraerlo.
        
        // TODO 2: Si el archivo es el 18, extraelo normalmente, imprime 
        // "¡Codigos secretos obtenidos! Abortando conexion...", y usa break para huir.
        
        std::cout << "Extrayendo archivo " << archivo << "...\n";
    }
    
    std::cout << "Conexion cerrada. Has salido sin ser detectado.\n";
    return 0;
}
