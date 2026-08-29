// ============================================================================
// Laboratorio L05: Datos y Entrada Segura
// ============================================================================
// Objetivo: Declarar variables con inicialización uniforme y capturar entrada con std::cin.
// ============================================================================

#include <iostream>
#include <string>

int main() {
    std::cout << "=== L05: Variables Seguras e Inicializacion Uniforme ===\n\n";

    // 1. Inicializacion Uniforme en C++ Moderno (usando llaves {})
    // Previene que las variables retengan valores basura preexistentes en la RAM
    std::string nombreUsuario{""};
    int edadUsuario{0};

    // 2. Captura de una sola palabra desde el flujo de entrada (teclado)
    std::cout << "Ingresa tu primer nombre: ";
    std::cin >> nombreUsuario;

    std::cout << "Ingresa tu edad: ";
    std::cin >> edadUsuario;

    // 3. Salida de datos formateada
    std::cout << "\n--- Confirmacion de Registro ---\n";
    std::cout << "Usuario registrado : " << nombreUsuario << "\n";
    std::cout << "Edad asignada      : " << edadUsuario << " anios\n";
    std::cout << "Estado en RAM      : Inicializado correctamente sin valores basura.\n";

    return 0;
}
