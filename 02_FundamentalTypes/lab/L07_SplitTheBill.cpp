// ============================================================================
// Laboratorio L07: Mini-proyecto 'Split the Bill'
// ============================================================================
// Objetivo: Integrar todos los conceptos del módulo (tipos, inicialización estricta, static_cast y booleanos lógicos) para crear una calculadora financiera.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "--- Calculadora de Cuenta (Lab Guiado) ---\n\n";

    // 1. Declaracion e inicializacion estricta
    int total_cuenta{150};
    int propina{20};
    int amigos{4};

    std::cout << "Cuenta: $" << total_cuenta << "\n";
    std::cout << "Propina: $" << propina << "\n";
    std::cout << "Amigos: " << amigos << "\n\n";

    // 2. Operadores relacionales y logicos (Sin usar IF)
    // Validamos que los datos tengan sentido en el mundo real.
    bool amigos_validos{amigos > 0};
    bool propina_valida{propina >= 0};
    bool cuenta_valida{total_cuenta > 0};

    // Juntamos todo con AND logico
    bool todo_ok{amigos_validos && propina_valida && cuenta_valida};
    
    std::cout << "Estado de los datos (1=OK, 0=Error): " << todo_ok << "\n\n";

    // 3. Matematicas y conversion segura
    int cuenta_mas_propina{total_cuenta + propina};
    
    // Casteo para no perder centavos al dividir enteros
    double pago_por_persona{static_cast<double>(cuenta_mas_propina) / amigos};

    std::cout << "Total a pagar con propina: $" << cuenta_mas_propina << "\n";
    std::cout << "Cada persona debe pagar: $" << pago_por_persona << "\n";

    return 0;
}
