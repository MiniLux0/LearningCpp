// ============================================================================
// Laboratorio D07: BUG DEMO - NestedBreakBug
// ============================================================================
// Objetivo: Demostrar la suposicion erronea de que un 'break' destruye multiples
//           niveles de bucles anidados. En C++, 'break' solo escapa del bucle mas
//           interno en el que se encuentra contenido.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D07_NestedBreakBug.cpp -o bug
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Iniciando simulacion de radar de 3 capas...\n";

    // Bucle exterior: Itera por capas
    for (int capa{1}; capa <= 3; capa = capa + 1) {
        std::cout << "\n>>> Analizando Capa " << capa << " <<<\n";

        // Bucle interior: Itera por sectores de cada capa
        for (int sector{1}; sector <= 5; sector = sector + 1) {
            std::cout << "  - Escaneando sector " << sector << "...\n";

            if (sector == 2) {
                std::cout << "  [ALERTA] Anomalía encontrada en sector 2. Ejecutando 'break'...\n";
                // BUG CONCEPTUAL: El programador cree que esto apaga todo el escaneo.
                // En realidad, solo termina el bucle interior de la capa actual.
                // El bucle exterior pasara a la siguiente capa inmediatamente.
                break;
            }
        }
    }

    std::cout << "\nSimulacion terminada. Observa como las Capas 2 y 3 continuaron ejecutandose.\n";
    return 0;
}
