// ============================================================================
// Laboratorio L05: Manejo Tactico de Excepciones (try / catch)
// ============================================================================
// Objetivo: Demostrar la captura de excepciones std::out_of_range generadas
//           por el metodo .at() para garantizar la continuidad del proceso.
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>

int main() {
    std::cout << "--- DEMOSTRACION DE CONTENCION CON TRY / CATCH ---\n";

    std::vector<int> registros{1001, 1002, 1003}; // size = 3

    std::cout << "Intentando acceder a indices de forma segura:\n";

    try {
        // Acceso valido
        std::cout << "Indice 0: " << registros.at(0) << '\n';
        std::cout << "Indice 2: " << registros.at(2) << '\n';

        // Intento de acceso fuera de limites (detonara excepcion)
        std::cout << "Intentando acceder a indice 10...\n";
        std::cout << "Indice 10: " << registros.at(10) << '\n';

        std::cout << "Esta linea NUNCA se imprimira.\n";
    }
    catch (const std::out_of_range& error) {
        std::cout << "\n[EXCEPCION DETECTADA Y CONTENIDA]\n";
        std::cout << "Mensaje tecnico del contenedor: " << error.what() << '\n';
    }

    std::cout << "\nEl programa no colapso y finaliza de manera controlada.\n";
    return 0;
}
