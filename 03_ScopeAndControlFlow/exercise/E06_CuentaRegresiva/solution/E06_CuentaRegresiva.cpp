// ============================================================================
// Reto E06: CuentaRegresiva (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Preparando lanzamiento orbital...\n";
    std::cout << "Iniciando reloj:\n";
    
    // SOLUCION:
    // 1. Inicia en 10.
    // 2. Continua MIENTRAS el reloj sea mayor o igual a 1.
    // 3. Decrementa (resta 1) en cada vuelta.
    for (int reloj{10}; reloj >= 1; reloj = reloj - 1) {
        std::cout << "T-Minus " << reloj << "...\n";
    }
    
    std::cout << "¡IGNICION! Cohete en el aire.\n";
    return 0;
}
