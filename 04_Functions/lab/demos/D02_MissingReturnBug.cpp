// ============================================================================
// Laboratorio D02: BUG DEMO - Missing Return (Undefined Behavior)
// ============================================================================
// Objetivo: Demostrar el comportamiento indefinido (UB) que ocurre cuando una
// funcion no-void finaliza su flujo de ejecucion sin alcanzar un return con valor.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 -Wall -Wextra D02_MissingReturnBug.cpp -o bug
// ============================================================================

#include <iostream>

int obtenerDescuento(int edad) {
    if (edad > 60) {
        return 50; // Retorno valido solo para mayores de 60
    }
    // TRAMPA: Si edad <= 60, el flujo escapa sin retornar un valor int.
    // Esto genera Undefined Behavior (lee basura del registro de retorno).
}

int main() {
    std::cout << "[DEMO] Calculando descuento para usuario de 25 anios...\n";
    int descuento{obtenerDescuento(25)};
    std::cout << "Descuento obtenido: " << descuento << "%\n";
    std::cout << "[ADVERTENCIA] El valor impreso es basura de la memoria o provoco crash.\n";
    return 0;
}
