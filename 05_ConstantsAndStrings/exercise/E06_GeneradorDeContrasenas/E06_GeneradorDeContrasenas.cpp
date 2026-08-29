// ============================================================================
// Reto E06: Generador de Contrasenas
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>
#include <string>
// TODO 1: Incluye la cabecera necesaria para utilizar referencias de texto de solo lectura.

// TODO 2: Evita la clonacion. Convierte el parametro a una referencia de solo lectura.
void imprimirAlerta(std::string mensaje) {
    std::cout << "[ALERTA] " << mensaje << '\n';
}

int main() {
    // TODO 3: Este calculo es 100% estatico. Obliga al compilador a evaluarlo 
    // en Compile-time usando el modificador correspondiente e inicializacion uniforme {}.
    int codigoMaestro = 42;
    int multiplicador = 10;
    int semilla = codigoMaestro * multiplicador;

    int pinEmpleado{0};
    bool entradaValida{false};

    // TODO 4: Validacion anti-trolls. Protege el estado del buffer std::cin.
    while (entradaValida == false) {
        std::cout << "Ingrese su PIN numerico: ";
        std::cin >> pinEmpleado;

        // Reemplaza 'false' por la comprobacion del estado de error
        if (false) { 
            imprimirAlerta("Formato invalido.");
            
            // TODO 5: Restablece las banderas operativas de std::cin.
            
            // TODO 6: Purga la basura residual del buffer (ignora 10000 chars o el salto de linea).
            
        } else {
            entradaValida = true;
        }
    }

    std::string departamento{""};
    std::cout << "Ingrese su departamento (ej. Ventas): ";
    std::cin >> departamento;

    // TODO 7: Arregla este Type Error que actualmente intenta 
    // concatenar dos literales estaticos directos ("SEC_" y "2026_").
    std::string password = "SEC_" + "2026_" + departamento;

    // TODO 8: Aplica el modificador 'const' para que esta version final sea 
    // estrictamente inmutable usando inicializacion uniforme.
    std::string passwordFinal = password;

    std::cout << "\nGeneracion Exitosa.\n";
    std::cout << "Semilla utilizada: " << semilla << '\n';
    std::cout << "Password: " << passwordFinal << '\n';

    return 0;
}
