#include <iostream>
using namespace std;

// Exercise 5 — Linear search
// Returns the index of the first appearance of objetivo, or -1 if not found.
int buscar(const int arr[], int size, int objetivo) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == objetivo) {
            return i; // Returns on the first found occurrence
        }
    }
    return -1; // The target was not found
}

int main() {
    int datos[] = {12, 45, 78, 23, 56};
    int n = sizeof(datos) / sizeof(datos[0]);

    cout << "Search 78 (expected 2): " << buscar(datos, n, 78) << endl;
    cout << "Search 99 (expected -1): " << buscar(datos, n, 99) << endl;
    cout << "Search 12 (first, expected 0): " << buscar(datos, n, 12) << endl;
    cout << "Search 56 (last, expected 4): " << buscar(datos, n, 56) << endl;

    return 0;
}

// Theoretical explanation:
// 1. For loop condition (i < size): Guarantees iterating through the exact indices of the array [0, size - 1] without going out of bounds.
// 2. Early return: As soon as `arr[i] == objetivo`, the function returns `i` immediately. This ensures we return the FIRST occurrence of the element.
// 3. Complexity:
//    - Best case: O(1) if the element is in the first position (index 0).
//    - Worst case: O(n) if the element is not in the array or is at the end (traverses the entire array).
