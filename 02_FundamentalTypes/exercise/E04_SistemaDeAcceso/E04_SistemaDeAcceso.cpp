// ============================================================================
// Reto E04: Sistema de Acceso
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la misión del reto.
// ============================================================================

#include <iostream>

int main() {
    // Datos del cliente de prueba
    int edad{17}; 
    bool tiene_ticket{false};
    bool esta_en_lista_vip{true};
    
    std::cout << std::boolalpha; // Para imprimir "true"/"false" en vez de 1/0
    std::cout << "--- EVALUANDO SISTEMA DE ACCESO ---\n";

    // ======================================================================
    // BUG 1: Regla de Edad
    // El club exige que la persona tenga 18 años O MAS. 
    // Actualmente el codigo solo permite entrar a los menores de 18.
    // ======================================================================
    bool es_mayor_de_edad{edad < 18}; // CORRIGE AQUI
    
    std::cout << "Test Regla 1 (Mayor de edad): " << es_mayor_de_edad << "\n";


    // ======================================================================
    // BUG 2: Regla de Autorizacion
    // Basta con que cumpla UNA de las dos condiciones (ticket o lista VIP).
    // Actualmente el codigo exige que tenga AMBAS cosas (&&).
    // ======================================================================
    bool esta_autorizado{tiene_ticket && esta_en_lista_vip}; // CORRIGE AQUI
    
    std::cout << "Test Regla 2 (Autorizado): " << esta_autorizado << "\n";


    // ======================================================================
    // BUG 3: Calculo final de acceso y la trampa mortal
    // Para que la puerta abra, deben cumplirse AMBAS reglas anteriores.
    // ¡Hay dos errores en la linea de abajo! Encuentralos.
    // Pista: mira bien los simbolos lógicos y los simbolos de igual.
    // ======================================================================
    bool acceso_concedido{ (es_mayor_de_edad = true) || esta_autorizado }; // CORRIGE AQUI

    std::cout << "RESULTADO FINAL (Acceso concedido): " << acceso_concedido << "\n";


    // ======================================================================
    // META:
    // Si cambias la edad del cliente de prueba a 20 (arriba en la linea 34), 
    // el resultado final deberia imprimirse como "true".
    // ======================================================================

    return 0;
}
