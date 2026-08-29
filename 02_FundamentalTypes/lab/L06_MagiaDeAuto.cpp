// ============================================================================
// Laboratorio L06: La Magia de auto
// ============================================================================
// Objetivo: Comprender cómo el compilador puede deducir el tipo de dato automáticamente, y por qué debemos usarlo con precaución (Regla de Oro).
// ============================================================================

#include <iostream>
#include <typeinfo> // Solo para demostrar el funcionamiento del compilador

int main() {
    std::cout << "--- El Compilador Detective ---\n";

    // Deduccion automatica y segura
    auto vidas{3};          
    auto escudo{50.5};      
    auto esta_envenenado{false}; 

    std::cout << "Vidas: " << vidas << "\n";
    std::cout << "Escudo: " << escudo << "\n";
    std::cout << "Envenenado (1=si, 0=no): " << esta_envenenado << "\n\n";

    // Mostremos como C++ no convirtio esto en tipado dinamico.
    // Usamos typeid().name() que nos devuelve un caracter representando el tipo interno
    // 'i' para int, 'd' para double, 'b' para bool (esto depende del compilador, en g++ es asi).
    std::cout << "--- Tipos deducidos en RAM ---\n";
    std::cout << "Tipo de vidas: " << typeid(vidas).name() << " (i = int)\n";
    std::cout << "Tipo de escudo: " << typeid(escudo).name() << " (d = double)\n";
    std::cout << "Tipo de esta_envenenado: " << typeid(esta_envenenado).name() << " (b = bool)\n\n";

    // El peligro del cambio de tipo
    auto puntaje{100};  // Esto es un int para siempre.
    puntaje = 105.99;   // Intentamos guardar un decimal, pero la variable nacio como int.

    std::cout << "--- Rigidez de Tipos ---\n";
    std::cout << "Intentamos guardar 105.99 en puntaje. Resultado: " << puntaje << "\n";
    std::cout << "El compilador truncó los decimales silenciosamente.\n";

    return 0;
}
