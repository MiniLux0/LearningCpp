// ============================================================================
// Laboratorio L06: Modularidad y Refactoring
// ============================================================================
// Objetivo: Observar el patron arquitectonico de un programa cuando el main() 
//           actua exclusivamente como un orquestador de flujos delegados.
// ============================================================================

#include <iostream>

// --- RUTINAS DELEGADAS (Separation of Concerns) ---

void imprimirBienvenida() {
    std::cout << "==========================\n";
    std::cout << " SIMULADOR DE LANZAMIENTO \n";
    std::cout << "==========================\n";
}

bool verificarSistemas() {
    std::cout << "Auditando telemetria de combustible...\n";
    std::cout << "Auditando integridad de motores...\n";
    // Simulamos una auditoria exitosa
    return true; 
}

void iniciarCuentaRegresiva(int segundos) {
    std::cout << "Iniciando secuencia de ignicion: ";
    // (Aprenderemos a construir bucles dinamicos luego, simulamos el output)
    std::cout << segundos << "... " << segundos - 1 << "... LANZAMIENTO!\n";
}

void abortarMision() {
    std::cout << "[ERROR FATAL] Tolerancia de sistemas excedida. Mision abortada.\n";
}

// --- FLUJO PRINCIPAL (Orquestador) ---

int main() {
    // Observa el alto nivel de abstraccion de este bloque.
    // El codigo se auto-documenta omitiendo los detalles de implementacion local.
    
    imprimirBienvenida();
    
    bool sistemas_ok{verificarSistemas()};
    
    if (sistemas_ok) {
        iniciarCuentaRegresiva(3);
    } else {
        abortarMision();
    }
    
    return 0;
}
