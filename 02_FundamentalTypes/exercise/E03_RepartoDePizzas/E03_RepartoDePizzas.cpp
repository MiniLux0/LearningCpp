// ============================================================================
// Reto E03: Reparto de Pizzas
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    // 1. Arregla la precedencia
    // Queremos sumar (120 + 150) y luego multiplicar todo por 2.
    // Actualmente da 420, ¡deberia dar 540!
    int precio_pizza1{120};
    int precio_pizza2{150};
    int costo_total{precio_pizza1 + precio_pizza2 * 2}; 

    std::cout << "El costo total es: $" << costo_total << '\n';

    // 2. Arregla la division entera
    // Queremos dividir 11 porciones entre 4 personas y ver los decimales exactos.
    // Actualmente da 2. (Pista: Convierte al menos uno en decimal).
    int porciones{11};
    int personas{4};
    double porciones_exactas{porciones / personas};

    std::cout << "A cada persona le tocarian " << porciones_exactas << " porciones exactas.\n";

    // 3. El sobrante (modulo)
    // Calcula cuantas porciones sobran si solo repartimos porciones enteras completas.
    // Pista: Usa el operador %
    int porciones_sobrantes{0}; // TODO: Reemplaza el 0 con el calculo usando modulo

    std::cout << "Sobran " << porciones_sobrantes << " porciones en la caja.\n";

    return 0;
}
