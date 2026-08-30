// ============================================================================
// Reto E09: Registro de Calificaciones
// ============================================================================
// Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <vector>
#include <stdexcept>
#include <limits>

void agregarNota(std::vector<double>& notas) {
    std::cout << "Ingrese la calificacion [0.0 - 20.0]: ";
    double nota{0.0};
    std::cin >> nota;

    // TODO 1: Valida que la entrada no haya fallado y que este entre 0.0 y 20.0
    // Si es valida, agregala con notas.push_back(nota)
    if (std::cin.fail() || nota < 0.0 || nota > 20.0) {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "[ERROR] Calificacion invalida.\n";
        return;
    }
    notas.push_back(nota);
    std::cout << "[EXITO] Nota registrada.\n";
}

void mostrarNotas(const std::vector<double>& notas) {
    // TODO 2: Si notas.empty(), muestra un aviso.
    // De lo contrario, lista cada nota usando range-based for.
    if (notas.empty()) {
        std::cout << "[AVISO] No hay notas registradas.\n";
        return;
    }
    std::size_t idx{0};
    for (double n : notas) {
        std::cout << "Nota [" << idx << "]: " << n << '\n';
        ++idx;
    }
}

void consultarNota(const std::vector<double>& notas) {
    if (notas.empty()) {
        std::cout << "[AVISO] Lista vacia.\n";
        return;
    }
    std::cout << "Ingrese el indice a consultar: ";
    std::size_t idx{0};
    std::cin >> idx;

    // TODO 3: Realiza la consulta con .at(idx) dentro de un bloque try/catch
    try {
        std::cout << "Nota en posicion " << idx << ": " << notas.at(idx) << '\n';
    }
    catch (const std::out_of_range& error) {
        std::cout << "[ERROR] Indice fuera de rango: " << error.what() << '\n';
    }
}

void mostrarEstadisticas(const std::vector<double>& notas) {
    // TODO 4: Calcula y muestra el promedio, nota maxima y nota minima
    if (notas.empty()) {
        std::cout << "[AVISO] No hay datos para calcular estadisticas.\n";
        return;
    }
    double suma{0.0};
    double maximo{notas.at(0)};
    double minimo{notas.at(0)};

    for (double n : notas) {
        suma += n;
        if (n > maximo) maximo = n;
        if (n < minimo) minimo = n;
    }

    std::cout << "Promedio: " << suma / static_cast<double>(notas.size()) << '\n';
    std::cout << "Maxima:   " << maximo << '\n';
    std::cout << "Minima:   " << minimo << '\n';
}

int main() {
    std::vector<double> notas{};
    
    // Menu basico para pruebas
    std::cout << "--- SISTEMA DE GESTION DE CALIFICACIONES ---\n";
    std::cout << "Modo de prueba rapido:\n";
    
    agregarNota(notas);
    mostrarNotas(notas);
    mostrarEstadisticas(notas);

    return 0;
}
