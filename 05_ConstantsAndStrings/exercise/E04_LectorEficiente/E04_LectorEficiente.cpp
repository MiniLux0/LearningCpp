// ============================================================================
// Reto E04: Lector Eficiente
// ============================================================================
//  Lee el archivo README.md para conocer el contexto y la mision del reto.
// ============================================================================

#include <iostream>
#include <string>
// TODO 1: Incluye la cabecera moderna para utilizar referencias de texto de solo lectura.

// TODO 2: Modifica el parametro para evitar clonar el objeto en memoria.
// Utiliza la estructura ligera de solo lectura.
void analizarArticulo(std::string textoPesado) {
    std::cout << "Analizando lectura... " << textoPesado << '\n';
}

int main() {
    std::string articuloGigante{"[... millones de palabras sobre el universo ...]"};
    
    // Actualmente, esto clona todo el string gigante dentro de la funcion.
    analizarArticulo(articuloGigante);
    
    // TODO 3: Haz que esta variable sea una vista ligera (std::string_view) en lugar de 
    // asignar un nuevo bloque de memoria std::string para este literal constante.
    std::string notaRapida{"Nota: Buscar mas sobre estrellas enanas."};
    analizarArticulo(notaRapida);

    return 0;
}
