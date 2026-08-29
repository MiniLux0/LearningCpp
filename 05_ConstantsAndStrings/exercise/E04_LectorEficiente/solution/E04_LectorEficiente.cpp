// ============================================================================
// Reto E04: Lector Eficiente (SOLUCIÓN)
// ============================================================================

#include <iostream>
#include <string>
#include <string_view> // Solucion 1

// Solucion 2: Cambiado a std::string_view para evitar copias masivas en RAM
void analizarArticulo(std::string_view textoPesado) {
    std::cout << "Analizando lectura... " << textoPesado << '\n';
}

int main() {
    std::string articuloGigante{"[... millones de palabras sobre el universo ...]"};
    
    // Ahora solo pasamos "una referencia de lectura" en lugar de clonar el bloque de memoria. Es instantaneo.
    analizarArticulo(articuloGigante);
    
    // Solucion 3: Usamos std::string_view para observar el literal estático directamente,
    // sin necesidad de instanciar un objeto dinámico std::string intermedio en la memoria.
    std::string_view notaRapida{"Nota: Buscar mas sobre estrellas enanas."};
    analizarArticulo(notaRapida);

    return 0;
}
