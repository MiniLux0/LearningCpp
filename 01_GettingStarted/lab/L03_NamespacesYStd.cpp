// ============================================================================
// Laboratorio L03: Namespaces y el universo std::
// ============================================================================
// Objetivo: Comprender los espacios de nombres y la regla de acceso explícito.
// ============================================================================

#include <iostream>

// Definimos un namespace personalizado para demostrar aislamiento de nombres
namespace ServidorA {
    void conectar() {
        std::cout << "[ServidorA] Conexion establecida al puerto 8080.\n";
    }
}

namespace ServidorB {
    void conectar() {
        std::cout << "[ServidorB] Conexion establecida al puerto 9090.\n";
    }
}

int main() {
    std::cout << "=== Demostracion de Namespaces en C++ Moderno ===\n\n";

    // 1. Acceso explicito con el operador de resolucion de ambito (::)
    // Esto evita cualquier ambiguedad entre funciones con el mismo nombre.
    ServidorA::conectar();
    ServidorB::conectar();

    // 2. Uso explicito de std:: (La regla de oro de la industria)
    std::cout << "\nRegla fundamental de ingenieria:\n";
    std::cout << "Escribir 'std::cout' de forma explicita previene colisiones accidentales\n";
    std::cout << "y mantiene el codigo claro y profesional sin contaminar el ambito global.\n";

    return 0;
}
