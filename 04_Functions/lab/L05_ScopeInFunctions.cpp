// ============================================================================
// Laboratorio L05: Ambito Local en Funciones (Scope)
// ============================================================================
// Objetivo: Observar como el ciclo de vida de la memoria local permite
//           la coexistencia de identificadores iguales sin generar colisiones.
// ============================================================================

#include <iostream>

void auditarSectorA() {
    // La variable 'temperatura' se aloja en el Scope local de este bloque
    int temperatura{40}; 
    std::cout << "[Sector A] La temperatura aislada es de " << temperatura << " grados.\n";
}

void auditarSectorB() {
    // Este identificador 'temperatura' mapea a una direccion de memoria DIFERENTE.
    // No hay colision de nombres por el Aislamiento de Scope.
    int temperatura{15}; 
    std::cout << "[Sector B] La temperatura aislada es de " << temperatura << " grados.\n";
}

int main() {
    // El Scope principal (main) declara su propia direccion de memoria local
    int temperatura{25}; 
    
    std::cout << "[Main] Iniciando lectura de sensores...\n";
    std::cout << "[Main] La temperatura en el bloque central es " << temperatura << " grados.\n\n";
    
    auditarSectorA();
    auditarSectorB();
    
    std::cout << "\n[Main] Memoria central preservada, la temperatura sigue en " << temperatura << " grados.\n";
    
    return 0;
}
