// ============================================================================
// Laboratorio L06: Mini-Proyecto Aplicación Interactiva
// ============================================================================
// Objetivo: Integrar salida, entrada, variables y formato en una terminal interactiva.
// ============================================================================

#include <iostream>
#include <string>

int main() {
    // 1. Encabezado de la aplicacion
    std::cout << "========================================\n";
    std::cout << "    GENERADOR DE PERFIL DE USUARIO      \n";
    std::cout << "========================================\n\n";

    // 2. Inicializacion uniforme de variables (C++17 / C++20)
    std::string nombreCompleto{""};
    std::string temaFavorito{""};
    int numeroFavorito{0};

    // 3. Captura de cadenas completas con espacios mediante std::getline
    std::cout << "1. Ingresa tu nombre completo: ";
    std::getline(std::cin, nombreCompleto);

    std::cout << "2. Ingresa tu tema favorito de programacion: ";
    std::getline(std::cin, temaFavorito);

    std::cout << "3. Ingresa tu numero de la suerte: ";
    std::cin >> numeroFavorito;

    // 4. Tarjeta de perfil estructurada
    std::cout << "\n----------------------------------------\n";
    std::cout << "         TARJETA DE IDENTIFICACION      \n";
    std::cout << "----------------------------------------\n";
    std::cout << " Nombre         : " << nombreCompleto  << "\n";
    std::cout << " Tema favorito  : " << temaFavorito    << "\n";
    std::cout << " Numero elegido : " << numeroFavorito  << "\n";
    std::cout << " Estado         : Modulo 01 completado exitosamente!\n";
    std::cout << "----------------------------------------\n";

    return 0;
}
