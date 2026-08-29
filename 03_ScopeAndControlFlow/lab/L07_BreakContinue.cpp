// ============================================================================
// Laboratorio L07: Break y Continue
// ============================================================================
// Objetivo: Observar como alterar manualmente el flujo normal de un bucle.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- SISTEMA DE COMUNICACION ---\n";
    
    // Simulemos buscar una señal de radio del 1 al 10.
    // Solo nos interesa el canal 7. Los canales 3 y 4 estan bloqueados por estatica.
    
    for (int canal{1}; canal <= 10; canal = canal + 1) {
        
        if (canal == 3 || canal == 4) {
            std::cout << "Canal " << canal << ": [Estatica]... saltando.\n";
            continue; // Anula esta vuelta y pasa al siguiente canal.
        }
        
        if (canal == 7) {
            std::cout << "Canal " << canal << ": ¡SEÑAL ENCONTRADA! Deteniendo busqueda.\n";
            break; // Anula TODO el bucle. Ya no importa si faltan canales por revisar.
        }
        
        std::cout << "Canal " << canal << ": Vacio.\n";
    }
    
    std::cout << "Busqueda finalizada.\n";
    
    return 0;
}
