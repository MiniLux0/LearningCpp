// ============================================================================
// Laboratorio L02: Inicialización Uniforme Moderna
// ============================================================================
// Objetivo: Observar en vivo cómo el estilo clásico (=) pierde datos en silencio y cómo la inicialización moderna ({}) te protege con un error.
// ============================================================================

#include <iostream>

int main() {
    std::cout << "=== El Peligro del Narrowing ===\n\n";

    // 1. EL PROBLEMA (Estilo clásico con =)
    // Queríamos guardar 4.9, pero el tipo int no soporta decimales.
    // C++ clásico no avisa: recorta el .9 y guarda un 4.
    int balas_clasico = 4.9; 
    
    std::cout << "[Estilo '=' ] Balas que pedimos : 4.9\n";
    std::cout << "[Estilo '=' ] Balas guardadas   : " << balas_clasico << " (Se perdio el 0.9!)\n\n";

    // 2. LA SOLUCIÓN (Inicialización uniforme con {})
    // Si usas {} en lugar de =, el compilador de C++ detecta la pérdida de datos
    // y CANCELA la compilación con un error, protegiéndote de bugs silenciosos.
    // NOTA: Ve a la carpeta `demos/` y abre `D02_NarrowingBug.cpp` para ver
    //       este error de compilación en acción.
    
    // 3. LA FORMA CORRECTA
    // Si realmente querías decimales, el tipo debía ser double desde el principio.
    // Con double y llaves, todo encaja perfecto.
    double balas_reales{4.9};
    std::cout << "[C++ Moderno] Balas correctas   : " << balas_reales << " (Todo encaja)\n";

    return 0;
}
