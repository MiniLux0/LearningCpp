#include <iostream>
using namespace std;

// ============================================================================
// L28 — ARRAYS AS PARAMETERS: PASS BY ADDRESS AND CONST
// ============================================================================
// Key concept: The name of the array IS its starting address in memory.
// When passing an array to a function:
// 1. The elements are not copied — only the address is copied (pass by address).
// 2. The function accesses the SAME memory as main().
// 3. Use `const` if the function should ONLY READ the array (write protection).
// 4. Omit `const` if the function should MODIFY the array in-place.
// ============================================================================

// 1. sum() — const int array[] protects the array against accidental modifications
long long sum(const int array[], int length) {
    long long sumaTotal = 0;
    for (int i = 0; i < length; i++) {
        sumaTotal += array[i];
    }
    return sumaTotal;
}

// 2. duplicar() — WITHOUT const because it needs to write to the original array
void duplicar(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        arr[i] *= 2; // Modifies the original memory in main()
    }
}

// 3. intentarModificar() — Demonstrates the contrast with a normal `int` (passed by value)
void intentarModificar(int x) {
    x = 999; // Only modifies the local copy of x
    cout << "  [Inside intentarModificar] x = " << x << endl;
}

int main() {
    cout << "=== L28: Arrays as Parameters ===" << endl;

    // --- 1. Function sum() with const (Read-only) ---
    cout << "\n--- 1. Pass by Address + const (sum) ---" << endl;
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    const int tam = 7;

    cout << "Original array: ";
    for (int i = 0; i < tam; i++) cout << arr[i] << " ";
    cout << endl;

    long long resultadoSuma = sum(arr, tam);
    cout << "Total sum: " << resultadoSuma << endl;
    cout << "After sum(), arr[0] = " << arr[0] << " (Protected by const)" << endl;

    // --- 2. Function duplicar() without const (In-Place Modification) ---
    cout << "\n--- 2. Pass by Address WITHOUT const (duplicar) ---" << endl;
    int datos[] = {10, 20, 30, 40, 50};
    const int tamDatos = 5;

    cout << "Before duplicar:  ";
    for (int i = 0; i < tamDatos; i++) cout << datos[i] << " ";
    cout << endl;

    duplicar(datos, tamDatos);

    cout << "After duplicar: ";
    for (int i = 0; i < tamDatos; i++) cout << datos[i] << " ";
    cout << endl;
    cout << "(The changes ARE reflected in main because they share the same memory address)" << endl;

    // --- 3. Contrast: normal int (Pass by Value) ---
    cout << "\n--- 3. Contrast: normal int (Pass by Value) ---" << endl;
    int miVariable = 42;
    cout << "Before: miVariable = " << miVariable << endl;

    intentarModificar(miVariable);

    cout << "After: miVariable = " << miVariable << " (Did NOT change because normal int is passed by copy)" << endl;

    return 0;
}