// ============================================================================
// Reto E09: Registro de Calificaciones (SOLUCION)
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>
#include <limits>

void agregarNota(std::vector<double>& notas) {
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

void mostrarNotas(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] No hay calificaciones registradas en el sistema.\n";
        return;
    }

    std::cout << "\n--- LISTADO DE CALIFICACIONES ---\n";
    std::size_t idx{0};
    for (double n : notas) {
        std::cout << "Indice [" << idx << "]: " << n << '\n';
        ++idx;
    }
}

void consultarNota(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] No hay calificaciones registradas para consultar.\n";
        return;
    }

    std::cout << "Ingrese el indice que desea consultar: ";
    std::size_t idx{0};
    std::cin >> idx;

    if (std::cin.fail()) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "[ERROR] Entrada invalida. Debe ingresar un indice numerico.\n";
        return;
    }

    try {
        double valor = notas.at(idx);
        std::cout << "[CONSULTA] Indice [" << idx << "] = " << valor << '\n';
    }
    catch (const std::out_of_range& error) {
        std::cout << "[ERROR DE RANGO] El indice [" << idx << "] no existe.\n";
        std::cout << "Detalle: " << error.what() << '\n';
    }
}

void mostrarEstadisticas(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] No hay calificaciones registradas para calcular estadisticas.\n";
        return;
    }

    double suma{0.0};
    double maximo{notas.at(0)};
    double minimo{notas.at(0)};

    for (double n : notas) {
        suma += n;
        if (n > maximo) {
            maximo = n;
        }
        if (n < minimo) {
            minimo = n;
        }
    }

    double promedio{suma / static_cast<double>(notas.size())};

    std::cout << "\n--- ESTADISTICAS DEL GRUPO ---\n";
    std::cout << "Cantidad de registros: " << notas.size() << '\n';
    std::cout << "Promedio:              " << promedio << '\n';
    std::cout << "Nota maxima:           " << maximo << '\n';
    std::cout << "Nota minima:           " << minimo << '\n';
}

int main() {
    std::vector<double> notas{};

    std::cout << "--- SISTEMA DE GESTION DE CALIFICACIONES (SOLUCION) ---\n";
    std::cout << "Demostracion automatizada con datos de prueba:\n";

    notas.push_back(18.5);
    notas.push_back(14.0);
    notas.push_back(19.0);
    notas.push_back(12.5);

    mostrarNotas(notas);
    mostrarEstadisticas(notas);

    std::cout << "\nProbando consulta segura con indice valido (1):\n";
    std::cout << "Nota en indice [1]: " << notas.at(1) << '\n';

    std::cout << "\nProbando consulta segura con indice invalido (99):\n";
    try {
        std::cout << notas.at(99) << '\n';
    }
    catch (const std::out_of_range& error) {
        std::cout << "[CAPTURA SEGURA] Excepcion capturada correctamente: " << error.what() << '\n';
    }

    return 0;
}
