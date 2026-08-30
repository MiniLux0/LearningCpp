// ============================================================================
// Laboratorio L09: Mini-proyecto Integrador - Registro de Calificaciones
// ============================================================================
// Objetivo: Implementar una aplicacion interactiva de consola que gestione
//           calificaciones dinamicas con validacion, acceso seguro y estadisticas.
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>
#include <limits>

void mostrarMenu() {
    std::cout << "\n======================================================\n";
    std::cout << "     SISTEMA DE GESTION DE CALIFICACIONES ACADEMICAS\n";
    std::cout << "======================================================\n";
    std::cout << "1. Registrar nueva calificacion\n";
    std::cout << "2. Listar todas las calificaciones registradas\n";
    std::cout << "3. Consultar calificacion por posicion de indice\n";
    std::cout << "4. Calcular estadisticas (Promedio, Maxima, Minima)\n";
    std::cout << "5. Salir\n";
    std::cout << "Seleccione una opcion [1-5]: ";
}

void agregarCalificacion(std::vector<double>& notas) {
    std::cout << "Ingrese la calificacion [0.0 - 20.0]: ";
    double nota{0.0};
    std::cin >> nota;

    if (std::cin.fail() || nota < 0.0 || nota > 20.0) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "[ERROR] Calificacion invalida. Debe ser un numero entre 0.0 y 20.0.\n";
        return;
    }

    notas.push_back(nota);
    std::cout << "[EXITO] Calificacion " << nota << " registrada correctamente.\n";
}

void listarCalificaciones(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] No hay calificaciones registradas en el sistema.\n";
        return;
    }

    std::cout << "\n--- LISTADO DE CALIFICACIONES REGISTRADAS ---\n";
    std::size_t indice{0};
    for (double nota : notas) {
        std::cout << "Indice [" << indice << "]: " << nota << '\n';
        ++indice;
    }
    std::cout << "Total de registros: " << notas.size() << '\n';
}

void consultarPorIndice(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] No hay calificaciones registradas para consultar.\n";
        return;
    }

    std::cout << "Ingrese el indice que desea consultar: ";
    std::size_t indice{0};
    std::cin >> indice;

    if (std::cin.fail()) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "[ERROR] Entrada invalida. Ingrese un numero entero positivo.\n";
        return;
    }

    try {
        double valor = notas.at(indice);
        std::cout << "[CONSULTA EXITOSA] La calificacion en el indice [" << indice << "] es: " << valor << '\n';
    }
    catch (const std::out_of_range& error) {
        std::cout << "[ERROR DE RANGO] El indice [" << indice << "] no existe en el sistema.\n";
        std::cout << "Diagnostico tecnico: " << error.what() << '\n';
    }
}

void calcularEstadisticas(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] Se requieren calificaciones registradas para calcular estadisticas.\n";
        return;
    }

    double suma{0.0};
    double maxima{notas.at(0)};
    double minima{notas.at(0)};

    for (double nota : notas) {
        suma += nota;
        if (nota > maxima) {
            maxima = nota;
        }
        if (nota < minima) {
            minima = nota;
        }
    }

    double promedio{suma / static_cast<double>(notas.size())};

    std::cout << "\n--- REPORTE ESTADISTICO DEL GRUPO ---\n";
    std::cout << "Total de calificaciones evaluadas: " << notas.size() << '\n';
    std::cout << "Promedio general: " << promedio << '\n';
    std::cout << "Calificacion mas alta: " << maxima << '\n';
    std::cout << "Calificacion mas baja: " << minima << '\n';
}

int main() {
    std::vector<double> registroNotas{};
    bool ejecutando{true};

    while (ejecutando) {
        mostrarMenu();
        int opcion{0};
        std::cin >> opcion;

        if (std::cin.fail()) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "[ERROR] Opcion invalida. Intente de nuevo.\n";
            continue;
        }

        switch (opcion) {
            case 1:
                agregarCalificacion(registroNotas);
                break;
            case 2:
                listarCalificaciones(registroNotas);
                break;
            case 3:
                consultarPorIndice(registroNotas);
                break;
            case 4:
                calcularEstadisticas(registroNotas);
                break;
            case 5:
                std::cout << "\nCerrando el sistema de calificaciones. Hasta pronto.\n";
                ejecutando = false;
                break;
            default:
                std::cout << "[ERROR] Opcion no reconocida. Seleccione entre 1 y 5.\n";
                break;
        }
    }

    return 0;
}
