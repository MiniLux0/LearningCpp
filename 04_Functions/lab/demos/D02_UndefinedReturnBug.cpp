// ============================================================================
// Laboratorio D02: BUG DEMO - Undefined Return
// ============================================================================
// Objetivo: Observar el comportamiento indefinido al incumplir la firma de
//           retorno de una funcion en un flujo condicional.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D02_UndefinedReturnBug.cpp -o bug
// Observa como el segundo descuento devuelve un fragmento de RAM corrupta.
// ============================================================================

#include <iostream>

int obtenerDescuento(int edad) {
    if (edad > 60) {
        return 50; // Retorna 50% de descuento
    }
    
    // BUG INTENCIONAL: ¿Que pasa si la condicion no se cumple?
    // El hilo de ejecucion escapa sin toparse con un 'return 0;'.
    // Al incumplir la firma 'int', C++ inyectara basura de la memoria RAM.
}

int main() {
    int edad_abuelo{65};
    int edad_joven{25};
    
    std::cout << "Descuento para el cliente (65 anios): " << obtenerDescuento(edad_abuelo) << "%\n";
    
    std::cout << "------------------------------------------\n";
    std::cout << "Analizando cliente de 25 anios (Undefined Behavior)...\n";
    std::cout << "Descuento devuelto: " << obtenerDescuento(edad_joven) << "%\n";
    
    return 0;
}
