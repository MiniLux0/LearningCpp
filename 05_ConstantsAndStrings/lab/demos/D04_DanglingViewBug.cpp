// ============================================================================
// Laboratorio D04: BUG DEMO - Dangling View
// ============================================================================
// Objetivo: Observar el comportamiento indefinido (Undefined Behavior) al acceder a un Dangling View.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D04_DanglingViewBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <string>
#include <string_view>

std::string_view obtenerSaludo() {
    std::string saludoLocal{"Hola, soy un bloque de texto temporal"};
    
    // TRAMPA: Retornamos una vista apuntando a la variable local 'saludoLocal'.
    // Al llegar a la llave de cierre '}', TODAS las variables locales 
    // son destruidas y liberadas de la memoria RAM.
    return saludoLocal; 
}

int main() {
    // Recibimos la vista de la funcion.
    std::string_view vistaFantasmal = obtenerSaludo();
    
    // PELIGRO: Intentamos leer la vista, pero la memoria original ya fue liberada.
    // Esto es un "Dangling View" e imprimira basura de la RAM o causara un crash.
    std::cout << "El saludo es: " << vistaFantasmal << '\n';

    return 0;
}
