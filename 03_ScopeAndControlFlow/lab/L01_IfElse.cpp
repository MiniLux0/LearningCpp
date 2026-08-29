// ============================================================================
// Laboratorio L01: IfElse
// ============================================================================
// Objetivo: Comprender el flujo basico de los bloques if y else.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Sistema de Validacion de Edad ---\n";
    
    int edadUsuario{0};
    std::cout << "Por favor, ingresa tu edad: ";
    std::cin >> edadUsuario;
    
    // Condicion: ¿Es la edad mayor o igual a 18?
    if (edadUsuario >= 18) {
        std::cout << "\n[ACCESO PERMITIDO] Eres mayor de edad.\n";
        std::cout << "Bienvenido a la plataforma de inversiones.\n";
    } else {
        std::cout << "\n[ACCESO DENEGADO] Eres menor de edad.\n";
        std::cout << "Debes regresar cuando cumplas 18.\n";
    }
    
    std::cout << "\nEl programa ha finalizado exitosamente.\n";
    return 0;
}
