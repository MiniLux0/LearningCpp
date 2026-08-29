// ============================================================================
// Reto E04: Sistema de Acceso (SOLUCIÓN)
// ============================================================================

#include <iostream>

int main() {
    // Datos del cliente de prueba
    int edad{20}; // Cambiamos la edad a 20 para pasar el test final
    bool tiene_ticket{false};
    bool esta_en_lista_vip{true};
    
    std::cout << std::boolalpha; // Para imprimir "true"/"false" en vez de 1/0
    std::cout << "--- EVALUANDO SISTEMA DE ACCESO ---\n";

    // ======================================================================
    // BUG 1: Regla de Edad
    // El club exige que la persona tenga 18 años O MAS. 
    // CORRECCION: Usar >= (mayor o igual) en lugar de < (menor).
    // ======================================================================
    bool es_mayor_de_edad{edad >= 18};
    
    std::cout << "Test Regla 1 (Mayor de edad): " << es_mayor_de_edad << "\n";


    // ======================================================================
    // BUG 2: Regla de Autorizacion
    // Basta con que cumpla UNA de las dos condiciones (ticket o lista VIP).
    // CORRECCION: Usar el operador OR (||) en lugar del AND (&&).
    // ======================================================================
    bool esta_autorizado{tiene_ticket || esta_en_lista_vip};
    
    std::cout << "Test Regla 2 (Autorizado): " << esta_autorizado << "\n";


    // ======================================================================
    // BUG 3: Calculo final de acceso y la trampa mortal
    // Para que la puerta abra, deben cumplirse AMBAS reglas anteriores.
    // CORRECCION 1: Usar == para comparar (no = que es para asignar).
    // CORRECCION 2: Usar && para exigir ambas condiciones (no ||).
    // Nota: (es_mayor_de_edad == true) es redundante, basta con poner
    //       es_mayor_de_edad, pero lo dejamos explícito por la lección.
    // ======================================================================
    bool acceso_concedido{ (es_mayor_de_edad == true) && esta_autorizado };

    std::cout << "RESULTADO FINAL (Acceso concedido): " << acceso_concedido << "\n";


    // ======================================================================
    // META:
    // Si cambias la edad del cliente de prueba a 20 (arriba en la linea 34), 
    // el resultado final deberia imprimirse como "true".
    // ======================================================================

    return 0;
}
