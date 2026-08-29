// ============================================================================
// Reto E07: BuscadorDeArchivos (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Conectando al servidor corporativo...\n";
    
    for (int archivo{1}; archivo <= 20; archivo = archivo + 1) {
        
        // SOLUCION 1: El continue salta la vuelta sin ejecutar el std::cout final.
        if (archivo == 13) {
            std::cout << "Malware detectado en el archivo 13. Saltando...\n";
            continue;
        }
        
        std::cout << "Extrayendo archivo " << archivo << "...\n";
        
        // SOLUCION 2: El break destruye todo el bucle al terminar el archivo 18.
        if (archivo == 18) {
            std::cout << "¡Codigos secretos obtenidos! Abortando conexion...\n";
            break;
        }
    }
    
    std::cout << "Conexion cerrada. Has salido sin ser detectado.\n";
    return 0;
}
