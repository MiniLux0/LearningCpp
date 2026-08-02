#include <iostream>
#include <iterator> // std::size (C++17)
#include <cstring>  // strlen
using namespace std;

// ============================================================================
// L27 — ARRAY BASICS: DECLARATION, INITIALIZATION AND TRAVERSAL
// ============================================================================

int main()
{
    cout << "=== L27: Array Basics ===" << endl;

    // 1. Three ways to initialize
    cout << "\n--- 1. Initialization Methods ---" << endl;

    // Method 1: Declare and assign later
    int arr1[4];
    arr1[0] = 6;
    arr1[1] = 0;
    arr1[2] = 9;
    arr1[3] = 6;
    cout << "Method 1 (Manual assignment): arr1[0]=" << arr1[0] << ", arr1[3]=" << arr1[3] << endl;

    // Method 2: Initialize on declaration (explicit size)
    int arr2[4] = {6, 0, 9, 6};
    cout << "Method 2 (Explicit braces): arr2[2]=" << arr2[2] << endl;

    // Method 3: Size inferred by the compiler
    int arr3[] = {6, 0, 9, 6, 2, 0, 1, 1}; // size = 8
    cout << "Method 3 (Inferred size): arr3 has " << std::size(arr3) << " elements." << endl;

    // 2. Index access and modification
    cout << "\n--- 2. Index Access and Modification ---" << endl;
    int datos[5] = {10, 20, 30, 40, 50};
    cout << "Original datos[2] = " << datos[2] << endl;
    datos[2] = 99; // Modify the third element
    cout << "Modified datos[2] = " << datos[2] << endl;

    int idx = 3;
    cout << "Using a variable as an index datos[" << idx << "] = " << datos[idx] << endl;
    cout << "Using an expression as an index datos[" << idx << " - 1] = " << datos[idx - 1] << endl;

    // 3. Partial initialization and zeros
    cout << "\n--- 3. Partial Initialization ---" << endl;
    int parcial[5] = {1, 2}; // the rest is automatically filled with 0
    cout << "int parcial[5] = {1, 2}: ";
    for (int i = 0; i < 5; i++)
    {
        cout << parcial[i] << " ";
    }
    cout << endl;

    int ceros[10] = {0}; // All zeros
    cout << "int ceros[10] = {0}: ";
    for (int i = 0; i < 10; i++)
    {
        cout << ceros[i] << " ";
    }
    cout << endl;

    // 4. Runtime size (sizeof vs std::size)
    cout << "\n--- 4. Array Size ---" << endl;
    int n_sizeof = sizeof(datos) / sizeof(datos[0]);
    cout << "Size using sizeof(datos)/sizeof(datos[0]): " << n_sizeof << endl;

    int n_cpp17 = std::size(datos); // C++17
    cout << "Size using std::size(datos) [C++17]: " << n_cpp17 << endl;

    // 5. Ways to traverse an array
    cout << "\n--- 5. Classic Traversal vs Range-based for ---" << endl;

    cout << "Classic for with index: ";
    for (int i = 0; i < n_cpp17; i++)
    {
        cout << datos[i] << " ";
    }
    cout << endl;

    cout << "Range-based for (read-only): ";
    for (int x : datos)
    {
        cout << x << " ";
    }
    cout << endl;

    // Range-based for with reference to modify
    for (int &x : datos)
    {
        x *= 2; // Doubles each element in-place
    }

    cout << "After range-for by reference (x *= 2): ";
    for (int x : datos)
    {
        cout << x << " ";
    }
    cout << endl;

    // 6. Demonstration of the Proposed Exercise (Reading TAM elements)
    cout << "\n--- 6. Proposed Exercise: Demonstration ---" << endl;
    const int TAM = 6;
    int entrada[TAM] = {10, 20, 30, 40, 50, 60}; // Predefined test data

    cout << "Array with constant TAM = " << TAM << ":" << endl;
    for (int i = 0; i < TAM; i++)
    {
        cout << "entrada[" << i << "] = " << entrada[i] << endl;
    }

    return 0;
}