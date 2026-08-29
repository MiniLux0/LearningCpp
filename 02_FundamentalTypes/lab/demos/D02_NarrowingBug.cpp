// ============================================================================
// Laboratorio D02: BUG DEMO - El Escudo del Narrowing
// ============================================================================
// Objetivo: Mostrar cómo C++ moderno se niega a compilar si usas llaves {}
//           y existe riesgo de pérdida de datos.
//
// INSTRUCCIONES:
// Intenta compilar este archivo manualmente desde la terminal:
// g++ D02_NarrowingBug.cpp -o bug
//
// Observa el error protector que te lanza el compilador.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Intentando guardar 4.9 en un int...\n";

    // ERROR DE COMPILACIÓN AQUÍ
    // Las llaves {} evalúan que 4.9 no cabe en un int sin perder el .9
    // El compilador detiene el proceso y te salva de un bug silencioso.
    int balas{4.9}; 

    std::cout << "Balas: " << balas << "\n";

    return 0;
}
