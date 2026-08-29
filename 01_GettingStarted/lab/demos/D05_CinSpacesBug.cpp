// ============================================================================
// Laboratorio D05: BUG DEMO - El bug de los espacios en cin
// ============================================================================
// Objetivo: Demostrar cómo cin trunca en espacios y desborda el buffer hacia la siguiente lectura.
//
// INSTRUCCIONES:
// Compila con: g++ -std=c++17 D05_CinSpacesBug.cpp -o bug
// ============================================================================

#include <iostream>
#include <string>

int main() {
    std::string nombreCompleto{""};
    int edad{0};

    std::cout << "Escribe tu nombre y apellido: ";
    // EL BUG: std::cin >> se detiene en el primer espacio en blanco.
    // La primera palabra se almacena en nombreCompleto, y el resto permanece atorado en el buffer.
    std::cin >> nombreCompleto;

    std::cout << "Escribe tu edad: ";
    // El programa intenta extraer un entero, pero encuentra el texto remanente en el buffer,
    // provocando un fallo silencioso de extraccion (cin.fail()).
    std::cin >> edad;

    std::cout << "\nResultados:\n";
    std::cout << "Nombre : " << nombreCompleto << "\n";
    std::cout << "Edad   : " << edad << "\n";

    return 0;
}
