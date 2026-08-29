// ============================================================================
// Reto E05: Promedio (Conversión Segura)
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    int suma_calificaciones{254};
    int cantidad_examenes{3};

    std::cout << "Calculando el promedio del estudiante...\n";

    // TODO: El estudiante esta perdiendo decimales importantes.
    // Arregla la division utilizando static_cast<double>() en la siguiente linea.
    double promedio_final{suma_calificaciones / cantidad_examenes};

    std::cout << "El promedio final es: " << promedio_final << "\n";

    return 0;
}
