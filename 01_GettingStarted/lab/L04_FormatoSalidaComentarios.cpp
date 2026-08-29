// ============================================================================
// Laboratorio L04: Formato de Salida y Comentarios
// ============================================================================
// Objetivo: Formatear la consola usando secuencias de escape y comentarios limpios.
// ============================================================================

#include <iostream>

int main() {
    // 1. Salto de linea con caracter de escape '\n'
    // En C++ Moderno preferimos '\n' para evitar forzar vaciados de buffer innecesarios
    std::cout << "Linea 1: Inicio del reporte\n";
    std::cout << "Linea 2: Procesando datos del sistema...\n\n";

    // 2. Tabulacion horizontal ('\t') para formateo en columnas
    std::cout << "ID\tLENGUAJE\tESTANDAR\n";
    std::cout << "01\tC++\t\tC++17 / C++20\n";
    std::cout << "02\tAssembly\tx86-64\n\n";

    // 3. Comillas dobles (\") y Barra invertida (\\)
    std::cout << "El instructor dijo: \"Inicializa siempre tus variables\".\n";
    std::cout << "Ruta en disco: C:\\Proyectos\\LearningCpp\\01_GettingStarted\n";

    return 0;
}
