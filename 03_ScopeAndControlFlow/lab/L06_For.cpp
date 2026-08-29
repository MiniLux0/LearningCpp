// ============================================================================
// Laboratorio L06: Bucle For
// ============================================================================
// Objetivo: Entender la anatomía de un bucle for y sus tres secciones.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- TABLA DEL 7 ---\n";
    
    // 1. Inicializacion: int i{1} (Empieza en 1)
    // 2. Condicion: i <= 10 (Termina en el 10)
    // 3. Incremento: i = i + 1 (Sube de a 1)
    for (int i{1}; i <= 10; i = i + 1) {
        int resultado{7 * i};
        std::cout << "7 x " << i << " = " << resultado << "\n";
    }
    
    // NOTA: La variable 'i' ya no existe aqui, murio al terminar el bucle.
    
    std::cout << "\n--- SALTANDO DE 2 EN 2 ---\n";
    
    for (int par{2}; par <= 10; par = par + 2) {
        std::cout << "Numero par: " << par << "\n";
    }

    return 0;
}
