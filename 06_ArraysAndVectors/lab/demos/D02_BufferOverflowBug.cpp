// ============================================================================
// Laboratorio D02: BUG DEMO - Buffer Overflow en C-Array
// ============================================================================
// Objetivo: Demostrar como una escritura fuera de limites en un C-Array
//           sobreescribe y corrompe variables vecinas en el Stack frame.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D02_BufferOverflowBug.cpp -o bug
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- DEMO DE BUG: BUFFER OVERFLOW ---\n";

    // En el Stack se reservan variables contiguas
    int variableVecina{12345};
    int arregloFijo[3]{10, 20, 30}; // Indices validos: 0, 1, 2

    std::cout << "Valor inicial de variableVecina: " << variableVecina << '\n';
    std::cout << "Direccion de arregloFijo[0]:    " << &arregloFijo[0] << '\n';
    std::cout << "Direccion de variableVecina:     " << &variableVecina << '\n';

    std::cout << "\n[PELIGRO] Escribiendo fuera de limites: arregloFijo[3] = 99999...\n";

    // [FALLO] BUFFER OVERFLOW: El indice 3 no existe en un arreglo de 3 elementos.
    // El procesador calcula la direccion contigua y sobreescribe la memoria del Stack.
    arregloFijo[3] = 99999;

    std::cout << "Valor de arregloFijo[0]: " << arregloFijo[0] << '\n';
    std::cout << "Valor de arregloFijo[1]: " << arregloFijo[1] << '\n';
    std::cout << "Valor de arregloFijo[2]: " << arregloFijo[2] << '\n';
    
    // Alerta: La variable vecina pudo haber sido alterada silenciosamente o causar UB
    std::cout << "Valor actual de variableVecina: " << variableVecina << '\n';

    std::cout << "\nConclusion: Los C-Arrays carecen de verificacion de limites y causan Undefined Behavior.\n";
    return 0;
}
