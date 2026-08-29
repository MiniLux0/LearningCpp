// ============================================================================
// Laboratorio L05: While y Do-While
// ============================================================================
// Objetivo: Observar las diferencias entre un bucle de comprobacion previa y comprobacion posterior.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- PRUEBA DE RESISTENCIA ---\n";
    
    int flexiones{1};
    
    std::cout << "Entrando al bucle while:\n";
    // El while comprueba antes de hacer la accion
    while (flexiones <= 3) {
        std::cout << "Haciendo flexion numero " << flexiones << "\n";
        flexiones = flexiones + 1; // Condicion de salida
    }
    
    std::cout << "\nEntrando al bucle do-while:\n";
    int sentadillas{10};
    
    // El do-while ejecuta la accion AL MENOS una vez, aunque la condicion sea falsa.
    do {
        std::cout << "Haciendo sentadilla numero " << sentadillas << "\n";
        sentadillas = sentadillas + 1;
    } while (sentadillas <= 3); // 11 no es <= 3, asi que se detiene, pero ya hizo una.
    
    std::cout << "\nEntrenamiento finalizado.\n";
    return 0;
}
