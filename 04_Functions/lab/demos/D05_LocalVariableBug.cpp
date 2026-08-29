// ============================================================================
// Laboratorio D05: BUG DEMO - Fuga de Scope Local 
// ============================================================================
// Objetivo: Forzar el aborto de la compilacion al intentar invocar una
//           variable cuyo ciclo de vida fue destruido en un Scope adyacente.
//
// INSTRUCCIONES:
// Compila con `g++ D05_LocalVariableBug.cpp -o bug` y audita el error.
// ============================================================================

#include <iostream>

void auditarImpuestos() {
    // Esta variable nace y muere exclusivamente entre estas dos llaves {}
    int total_impuestos{42};
}

int main() {
    auditarImpuestos();
    
    // BUG ARQUITECTONICO: El Scope principal carece de visibilidad sobre
    // la memoria local de la rutina delegada (Ocultamiento de Informacion).
    // El compilador abortara: "total_impuestos was not declared in this scope"
    
    std::cout << "El total a pagar es: " << total_impuestos << '\n';
    
    // Para resolverlo, la rutina delegada debe inyectar el valor hacia el
    // bloque invocador mediante 'return', y este debe reasignarlo localmente.
    
    return 0;
}
