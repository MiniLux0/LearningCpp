// ============================================================================
// Laboratorio D05: BUG DEMO - El problema contable (Casting)
// ============================================================================
// Objetivo: Mostrar que asignar una división de enteros a un double no salva
//           los decimales; se pierden antes de la asignación.
//
// INSTRUCCIONES:
// Intenta compilar y ejecutar este archivo:
// g++ D05_DivisionEnteraBug.cpp -o bug
//
// Observa la falta de 1 dólar en la recolección total.
// ============================================================================

#include <iostream>

int main() {
    int precio_producto{99};
    int cantidad_personas{2};

    std::cout << "Precio total: $" << precio_producto << "\n";
    std::cout << "Dividido entre: " << cantidad_personas << " personas\n";

    // BUG INTENCIONAL: El programador olvido hacer casting.
    // Piensa que por usar double, obtendra decimales.
    double pago_por_persona{precio_producto / cantidad_personas};

    std::cout << "\nCada persona debe pagar: $" << pago_por_persona << "\n";
    
    // 99 / 2 es 49.5, pero como es division entera, da 49.
    // 49 * 2 = 98.
    // ¡Falta $1 para completar el pago! El restaurante se enojara.
    std::cout << "Total recolectado: $" << (pago_por_persona * 2) << "\n";
    std::cout << "¡Houston, tenemos un problema contable!\n";

    return 0;
}
