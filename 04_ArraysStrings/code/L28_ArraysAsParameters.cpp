#include <iostream>
using namespace std;

// ============================================================================
// L28 — ARRAYS COMO PARAMETROS: PASO POR DIRECCION Y CONST
// ============================================================================
// Concepto clave: el nombre del arreglo ES la direccion de inicio.
// Cuando pasas arr a una funcion, no se copian los elementos,
// se copia solo la direccion — la funcion accede a la misma memoria.
// ============================================================================

// ---------------------------------------------------------------------------
// 1. sum() — const para solo lectura
//    const int array[] = "esta funcion NO puede modificar el arreglo"
//    Usa el for compacto con i++ en el indice (post-incremento):
//      array[i++] → primero lee array[i], LUEGO incrementa i
//    El cuerpo del for esta vacio (;) — todo el trabajo ocurre
//    en la parte de "actualizacion"
// ---------------------------------------------------------------------------

int sum(const int array[], const int length) {
    long sum = 0;
    for (int i = 0; i < length; sum += array[i++]);
    return sum;
}

// ---------------------------------------------------------------------------
// 2. duplicar() — SIN const, porque necesita ESCRIBIR en el arreglo
//    Multiplica cada elemento por 2 in-place (modifica el original)
//    Esto funciona porque el arreglo se pasa por direccion:
//    la funcion accede a las MISMAS casas de memoria que main()
// ---------------------------------------------------------------------------

void duplicar(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        arr[i] *= 2;
    }
}

// ---------------------------------------------------------------------------
// 3. intentarModificar() — CONTRASTE con int normal pasado sin &
//    Un int se pasa por VALOR (copia) — modificar x aqui
//    NO afecta la variable original en main()
//    Esto es lo que hace ESPECIAL a los arreglos: ellos siempre
//    se pasan por direccion, como si tuvieran & implicito
// ---------------------------------------------------------------------------

void intentarModificar(int x) {
    x = 999;  // solo modifica la copia local
    cout << "  Dentro de intentarModificar: x = " << x << endl;
}

// ---------------------------------------------------------------------------
// MAIN — Demostracion
// ---------------------------------------------------------------------------

int main() {
    cout << "=== L28: Arrays como Parametros ===" << endl;

    // --- 1. sum() con const y for compacto ---
    cout << "\n--- 1. sum() con const (solo lectura) ---" << endl;
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    const int tam = 7;

    cout << "Arreglo: ";
    for (int i = 0; i < tam; i++) cout << arr[i] << " ";
    cout << endl;

    cout << "Sum: " << sum(arr, tam) << endl;  // 28

    // Despues de sum(), arr NO cambio (const lo protege)
    cout << "Despues de sum(), arr[0] = " << arr[0] << " (no cambio)" << endl;

    // --- 2. duplicar() sin const (modifica el original) ---
    cout << "\n--- 2. duplicar() sin const (modifica el original) ---" << endl;
    int datos[] = {10, 20, 30, 40, 50};
    const int tamDatos = 5;

    cout << "Antes de duplicar:  ";
    for (int i = 0; i < tamDatos; i++) cout << datos[i] << " ";
    cout << endl;

    duplicar(datos, tamDatos);

    cout << "Despues de duplicar: ";
    for (int i = 0; i < tamDatos; i++) cout << datos[i] << " ";
    cout << endl;
    // datos ahora es {20, 40, 60, 80, 100} — SI cambio en main()
    // porque el arreglo se paso por direccion (misma memoria)

    // --- 3. Contraste con int normal pasado sin & ---
    cout << "\n--- 3. Contraste: int normal pasado sin & ---" << endl;
    int miVariable = 42;
    cout << "Antes: miVariable = " << miVariable << endl;

    intentarModificar(miVariable);

    cout << "Despues: miVariable = " << miVariable << " (NO cambio)" << endl;
    // miVariable sigue siendo 42 porque se COPIO el valor a x
    // Con arreglos no hay copia de contenido, solo copia de la direccion
    // — por eso el arreglo SI se modifica y el int NO

    return 0;
}

/*
RESUMEN CLAVE L28:
------------------
POR QUE ARRAYS SE PASAN "POR DIRECCION":
  - El nombre del arreglo (arr) es la DIRECCION DE INICIO
  - Al pasar a funcion, se copia solo esa direccion (4-8 bytes)
  - La funcion accede a la MISMA memoria que main()
  - No necesitas & — es automatico

CONST:
  void f(const int arr[], int n)   // solo lectura
  void f(int arr[], int n)         // lectura + escritura
  - const = promesa: "no voy a modificar el arreglo"
  - Sin const, la funcion PUEDE escribir en el arreglo original

FOR COMPACTO CON i++:
  for (int i = 0; i < n; sum += arr[i++]);
  - Cuerpo vacio (;) — trabajo en la "actualizacion"
  - array[i++]: primero usa i, LUEGO incrementa
  - Equivale a: sum += arr[i]; i++;

CONTRASTE CON INT NORMAL:
  void f(int x)    // se COPIA el valor — dos casas distintas
  void f(int &x)   // se pasa ALIAS — misma casa (L29)
  void f(int arr[]) // se pasa DIRECCION — misma casa (automatico)
*/