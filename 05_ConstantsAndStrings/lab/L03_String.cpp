// ============================================================================
// Laboratorio L03: std::string
// ============================================================================
// Objetivo: Aprender a instanciar y concatenar objetos de texto dinamicos.
// ============================================================================

#include <iostream>
#include <string> // Funciones de la libreria estandar para manipular cadenas

int main() {
    // 1. Inicializacion uniforme de un objeto std::string
    std::string profesion{"Guerrero"};
    std::string arma{"Espada"};

    // 2. Concatenacion dinamica
    // Funciona porque 'profesion' es un objeto std::string dinamico,
    // por lo que el operador '+' posee la logica para reservar memoria y fusionar el literal.
    std::string perfilJugador = profesion + " con " + arma;

    std::cout << "Perfil: " << perfilJugador << '\n';

    // 3. Puedes concatenar al vuelo dentro del flujo si uno es std::string
    std::string jugador{"Arthur"};
    std::cout << "Bienvenido, " + jugador + " a la arena.\n";

    return 0;
}
