// ============================================================================
// Laboratorio D03: BUG DEMO - Concatenacion de Literales
// ============================================================================
// Objetivo: Entender que los literales de texto estaticos carecen de metodos de concatenacion.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D03_LiteralConcatBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <string>

int main() {
    // TRAMPA: Intentar sumar dos literales estaticos (C-strings primitivos).
    // El compilador abortara la operacion porque estos arrays primitivos 
    // carecen de logica interna de concatenacion. El operador '+' 
    // requiere que al menos uno de los operandos sea un objeto std::string dinamico.
    
    std::string titulo = "Senor " + "de los Anillos"; // ERROR DEL COMPILADOR
    
    // std::cout << titulo << '\n';
    
    return 0;
}
