// ============================================================================
// Laboratorio L01: Tipos Primitivos y la Memoria
// ============================================================================
// Objetivo: Demostrar la inicialización uniforme de los 4 tipos primitivos básicos y utilizar sizeof() para comprobar su tamaño en memoria.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "=== Explorando Tipos Primitivos ===\n\n";

    // 1. Inicialización uniforme estricta (Modern C++)
    int    edad{25};           // Números enteros
    double temperatura{36.5};  // Números con decimales
    char   inicial{'A'};       // Un solo carácter (comillas simples)
    bool   esta_activo{true};  // Verdadero o falso

    // 2. Mostrar los valores
    std::cout << "Valores almacenados:\n";
    std::cout << "Edad        : " << edad << '\n';
    std::cout << "Temperatura : " << temperatura << '\n';
    std::cout << "Inicial     : " << inicial << '\n';
    std::cout << "Activo      : " << esta_activo << "\n\n";

    // 3. Comprobar la memoria física (sizeof devuelve tamaño en bytes)
    std::cout << "--- Tamano en Memoria RAM ---\n";
    std::cout << "Un int ocupa    : " << sizeof(int) << " bytes\n";
    std::cout << "Un double ocupa : " << sizeof(double) << " bytes\n";
    std::cout << "Un char ocupa   : " << sizeof(char) << " byte\n";
    std::cout << "Un bool ocupa   : " << sizeof(bool) << " byte\n";

    // Observa cómo un double necesita mucho más espacio físico que un int
    // para poder almacenar decimales con alta precisión.

    return 0;
}
