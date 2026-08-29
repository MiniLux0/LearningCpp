// ============================================================================
// Laboratorio D04: BUG DEMO - ScopeAndFallthroughBug
// ============================================================================
// Objetivo: Mostrar como el Fallthrough ejecuta condigo indeseado y el error de Scope.
//
// INSTRUCCIONES:
// Compila con `g++ D04_ScopeAndFallthroughBug.cpp -o bug`
// ============================================================================

#include <iostream>

int main() {
    int estadoAlarma{1}; // 1 = Amarilla, 2 = Naranja, 3 = Roja
    
    std::cout << "Activando protocolo de seguridad nivel " << estadoAlarma << "...\n";
    
    switch (estadoAlarma) {
        case 1:
            std::cout << "Alerta Amarilla: Encender luces preventivas.\n";
            // BUG INTENCIONAL 1: Falta el break! Fuga de flujo (Fallthrough) incontrolada hacia la alerta Naranja.
        
        case 2:
            std::cout << "Alerta Naranja: Cerrar puertas de seguridad.\n";
            break;
            
        case 3:
            // BUG INTENCIONAL 2: Declarando variable sin llaves {} crea error de Scope.
            // Dependiendo del compilador, esto cruza la inicializacion.
            int personalEvacuado{50}; 
            std::cout << "Alerta Roja: Evacuar a " << personalEvacuado << " personas.\n";
            break;
    }
    
    return 0;
}
