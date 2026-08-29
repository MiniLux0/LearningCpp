// ============================================================================
// Laboratorio D01: BUG DEMO - La trampa de la división entera
// ============================================================================
// Objetivo: Mostrar cómo una operación matemáticamente correcta falla en C++
//           porque los operandos son enteros y se pierden los decimales.
//
// INSTRUCCIONES:
// Intenta compilar y ejecutar este archivo:
// g++ D01_TrampaDivisionEntera.cpp -o bug
//
// Observa cómo el promedio da 8 en lugar de 8.3333...
// ============================================================================

#include <iostream>

int main() {
    std::cout << "Calculadora de promedio de calificaciones\n";
    std::cout << "----------------------------------------\n";

    int calificacion1{8};
    int calificacion2{9};
    int calificacion3{8};
    
    int suma{calificacion1 + calificacion2 + calificacion3}; // Da 25
    int cantidad_materias{3};

    // EL BUG ESTA AQUI: 
    // Estamos dividiendo un 'int' entre otro 'int'. 
    // C++ resuelve (25 / 3) como division entera y da 8. Luego guarda ese 8 en el double.
    // Se perdio la fraccion (.333) ANTES de guardarse.
    double promedio_bug{suma / cantidad_materias}; 

    std::cout << "Tus calificaciones suman: " << suma << '\n';
    std::cout << "Tu promedio (calculado con bug) es: " << promedio_bug << '\n';
    
    // COMO ARREGLARLO:
    // Al menos uno de los valores debe ser convertido a decimal (double) para forzar
    // a C++ a realizar una division decimal real.
    // En las proximas lecciones veremos la forma "oficial" (static_cast), pero 
    // por ahora podemos hacer esto:
    double suma_decimal{25.0}; // Lo guardamos en un double
    double promedio_correcto{suma_decimal / cantidad_materias}; 

    std::cout << "Tu promedio (calculado correctamente) es: " << promedio_correcto << '\n';

    return 0;
}
