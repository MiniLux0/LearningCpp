// ============================================================================
// Reto E06: Generador de Contrasenas (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string>
#include <string_view> // Solucion 1

// Solucion 2: Uso de std::string_view para evitar clonacion en RAM
void imprimirAlerta(std::string_view mensaje) {
    std::cout << "[ALERTA] " << mensaje << '\n';
}

int main() {
    // Solucion 3: constexpr e inicializacion uniforme
    constexpr int codigoMaestro{42};
    constexpr int multiplicador{10};
    constexpr int semilla{codigoMaestro * multiplicador};

    int pinEmpleado{0};
    bool entradaValida{false};

    // Solucion 4, 5, 6: Validacion y limpieza del buffer
    while (entradaValida == false) {
        std::cout << "Ingrese su PIN numerico: ";
        std::cin >> pinEmpleado;

        if (std::cin.fail()) {
            imprimirAlerta("Formato invalido. Intento de sabotaje detectado.");
            std::cin.clear();
            std::cin.ignore(10000, '\n');
        } else {
            entradaValida = true;
        }
    }

    std::string departamento{""};
    std::cout << "Ingrese su departamento (ej. Ventas): ";
    std::cin >> departamento;

    // Solucion 7: Encapsulamos el primer literal estático en un objeto std::string dinámico
    // para invocar los métodos internos de concatenacion.
    std::string password{std::string{"SEC_"} + "2026_" + departamento};

    // Solucion 8: const correctness. Blindamos el string contra modificaciones.
    const std::string passwordFinal{password};

    std::cout << "\nGeneracion Exitosa.\n";
    std::cout << "Semilla calculada por compilador: " << semilla << '\n';
    std::cout << "Password asignada: " << passwordFinal << '\n';

    return 0;
}
