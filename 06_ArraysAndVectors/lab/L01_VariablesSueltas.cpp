// ============================================================================
// Laboratorio L01: Variables Sueltas vs Colecciones
// ============================================================================
// Objetivo: Demostrar el colapso del codigo al procesar datos individuales
//           desconectados frente a la necesidad de estructuras en memoria contigua.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- ENFOQUE TRADICIONAL: VARIABLES SUELTAS ---\n";

    // Variables independientes en el Stack (Cada una con su propio identificador)
    double calificacion1{18.5};
    double calificacion2{14.0};
    double calificacion3{19.5};
    double calificacion4{16.0};

    // Para calcular el promedio debemos sumar cada variable a mano
    double sumaTotal{calificacion1 + calificacion2 + calificacion3 + calificacion4};
    double promedio{sumaTotal / 4.0};

    std::cout << "Nota 1: " << calificacion1 << '\n';
    std::cout << "Nota 2: " << calificacion2 << '\n';
    std::cout << "Nota 3: " << calificacion3 << '\n';
    std::cout << "Nota 4: " << calificacion4 << '\n';
    std::cout << "Promedio obtenido: " << promedio << '\n';

    // CONCLUSION TECNICA:
    // Si la cantidad de alumnos creciera a 100, este enfoque requeriria 100
    // nombres de variables distintos y seria imposible procesarlos con bucles.
    return 0;
}
