// ============================================================================
// Laboratorio L02: Arreglos de C (C-Arrays)
// ============================================================================
// Objetivo: Comprender la estructura de memoria contigua de los arreglos clasicos
//           de C y la indexacion base-cero en el Stack frame.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- ESTRUCTURA DE C-ARRAYS EN EL STACK ---\n";

    // Declaracion e inicializacion uniforme de un C-Array estatico de 4 elementos
    int puntajes[4]{100, 250, 400, 850};

    // Indexacion base-cero (indices validos: 0, 1, 2, 3)
    std::cout << "Elemento en indice 0: " << puntajes[0] << '\n';
    std::cout << "Elemento en indice 1: " << puntajes[1] << '\n';
    std::cout << "Elemento en indice 2: " << puntajes[2] << '\n';
    std::cout << "Elemento en indice 3: " << puntajes[3] << '\n';

    // Modificacion directa en la memoria contigua
    puntajes[1] = 300;
    std::cout << "Elemento en indice 1 modificado: " << puntajes[1] << '\n';

    // Tamano total en bytes
    std::cout << "Bytes totales ocupados en Stack: " << sizeof(puntajes) << " bytes\n";
    std::cout << "Cantidad de elementos calculada: " << sizeof(puntajes) / sizeof(int) << '\n';

    return 0;
}
