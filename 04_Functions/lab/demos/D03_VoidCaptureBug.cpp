// ============================================================================
// Laboratorio D03: BUG DEMO - Capturando Tipo Incompleto
// ============================================================================
// Objetivo: Forzar al compilador a abortar el proceso mostrando el error 
//           "void value not ignored as it ought to be".
//
// INSTRUCCIONES: Intenta compilar con `g++ D03_VoidCaptureBug.cpp -o bug`. 
// Observa como la compilacion es rechazada debido a la asignacion ilegal.
// ============================================================================

#include <iostream>

void encenderSistema() {
    std::cout << "Sistemas en linea. Motores listos.\n";
}

int main() {
    std::cout << "Preparando lanzamiento...\n";
    
    // BUG INTENCIONAL: 'encenderSistema' tiene una firma de retorno 'void'.
    // Al intentar inicializar una direccion de memoria 'int' con el output
    // de una rutina de accion pura, C++ abortara para proteger el sistema.
    
    int estado_del_motor{encenderSistema()}; 
    
    // Para arreglar esto, debes invocar la funcion de manera independiente:
    // encenderSistema();
    
    return 0;
}
