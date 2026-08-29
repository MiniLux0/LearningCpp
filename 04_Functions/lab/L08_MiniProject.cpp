// ============================================================================
// Laboratorio L08: El Game Loop Modular
// ============================================================================
// Objetivo: Observar un patron de arquitectura para flujos iterativos (Loops)
//           usando rutinas delegadas y un orquestador altamente abstraido.
// ============================================================================

#include <iostream>

// --- 1. Rutinas Delegadas (Separation of Concerns) ---

void mostrarMenuPrincipal() {
    std::cout << "======================\n";
    std::cout << " ESCAPE DEL CALABOZO  \n";
    std::cout << "======================\n";
}

bool intentarAbrirPuerta() {
    std::cout << "Empujar la puerta? (1 para si, 0 para no): ";
    int accion{0};
    std::cin >> accion;
    
    if (accion == 1) {
        return true;
    }
    return false;
}

// --- 2. Flujo de Ejecucion Iterativa (Game Loop) ---

void ejecutarNivel() {
    int iteraciones{0};
    
    // Bucle indefinido controlado por Retorno Temprano
    while (true) {
        iteraciones = iteraciones + 1;
        std::cout << "\nIntento numero " << iteraciones << "...\n";
        
        bool puerta_abierta{intentarAbrirPuerta()};
        
        if (puerta_abierta) {
            std::cout << "[INFO] Brecha detectada en la puerta.\n";
            std::cout << "Proceso completado tras " << iteraciones << " intentos.\n";
            
            // El return intercepta el flujo, liberando la memoria del bucle y del Scope
            return; 
        } else {
            std::cout << "Operacion omitida. Reintentando ciclo.\n";
        }
    }
}

// --- 3. El Orquestador Central (main) ---

int main() {
    // El Scope principal orquesta el inicio y fin sin acoplar la logica de iteracion
    mostrarMenuPrincipal();
    
    ejecutarNivel();
    
    std::cout << "\nEjecucion del sistema finalizada.\n";
    
    return 0;
}
