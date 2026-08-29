// ============================================================================
// Reto E05: Promedio (Conversión Segura) (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    int suma_calificaciones{254};
    int cantidad_examenes{3};

    std::cout << "Calculando el promedio del estudiante...\n";

    // SOLUCION: Convertir temporalmente la suma a double para forzar division decimal.
    double promedio_final{static_cast<double>(suma_calificaciones) / cantidad_examenes};

    std::cout << "El promedio final es: " << promedio_final << "\n";

    return 0;
}
