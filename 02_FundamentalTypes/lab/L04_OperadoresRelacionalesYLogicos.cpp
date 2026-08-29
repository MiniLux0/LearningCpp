// ============================================================================
// Laboratorio L04: Operadores Relacionales y Lógicos
// ============================================================================
// Objetivo: Aprender a hacer preguntas a la computadora usando comparaciones (==, !=, >, <) y a combinar condiciones usando compuertas lógicas (&&, ||, !).
// ============================================================================

#include <iostream>

int main() {
    // Inicializacion uniforme usando llaves {}
    int edad_jugador{16};
    int edad_requerida{18};

    std::cout << "--- OPERADORES RELACIONALES ---\n";
    
    // Al imprimir booleanos, C++ por defecto imprime 1 (true) o 0 (false)
    // Usamos std::boolalpha para obligarlo a imprimir las palabras "true" o "false"
    std::cout << std::boolalpha;

    bool es_mayor_de_edad{edad_jugador >= edad_requerida};
    std::cout << "Es mayor de edad (>=): " << es_mayor_de_edad << "\n";

    bool es_menor_de_edad{edad_jugador < edad_requerida};
    std::cout << "Es menor de edad (<): " << es_menor_de_edad << "\n";

    // Advertencia: La diferencia entre = y ==
    int vidas{3};
    bool sin_vidas{vidas == 0}; // Pregunta: ¿vidas es idéntico a 0? (false)
    std::cout << "Tiene cero vidas (==): " << sin_vidas << "\n";

    /*
    BUG SILENCIOSO Y PELIGROSO:
    Si escribieramos: bool error = (vidas = 0);
    C++ no haria una pregunta. Sobrescribiria nuestras 3 vidas dejandolas en 0.
    Siempre usa == para comparar, NUNCA un solo =.
    */


    std::cout << "\n--- OPERADORES LOGICOS ---\n";

    bool tiene_ticket{true};
    bool esta_abierto{false};

    // Operador AND (&&) - Necesita que TODAS las condiciones sean ciertas
    bool puede_entrar_al_cine{tiene_ticket && esta_abierto};
    std::cout << "Puede entrar al cine (ticket Y abierto): " << puede_entrar_al_cine << "\n";

    bool paga_con_tarjeta{false};
    bool paga_con_efectivo{true};

    // Operador OR (||) - Necesita que AL MENOS UNA condicion sea cierta
    bool compra_exitosa{paga_con_tarjeta || paga_con_efectivo};
    std::cout << "Compra exitosa (tarjeta O efectivo): " << compra_exitosa << "\n";

    // Operador NOT (!) - Invierte el resultado de una condicion
    bool llueve{true};
    bool es_dia_soleado{!llueve};
    std::cout << "Es dia soleado (NO llueve): " << es_dia_soleado << "\n";


    std::cout << "\n--- COMBINANDO OPERADORES ---\n";
    // Verificando si un numero esta dentro de un rango especifico (mayor que 0 Y menor que 100)
    int salud{85};
    bool rango_valido{(salud > 0) && (salud <= 100)};
    std::cout << "La salud esta en un rango valido: " << rango_valido << "\n";

    return 0;
}
