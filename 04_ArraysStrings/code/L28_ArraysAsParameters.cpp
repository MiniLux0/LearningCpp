#include <iostream>

using namespace std;

// ============================================================================
// L28 — ARRAYS AS PARAMETERS: POINTER DECAY & CONST-CORRECTNESS
// Stanford CS106B Chapter 11 / MIT 6.096 Lecture 04
// ============================================================================

// Read-Only Traversal (const int arr[])
void printArray(const int arr[], int size) {
    cout << "Array contents: [ ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << "]" << endl;
}

// In-Place Modification (int arr[])
void doubleValues(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] *= 2; // Modifies original memory
    }
}

// Demonstration of sizeof inside receiving function (pointer decay)
void inspectDecay(int* arr) {
    cout << "Inside inspectDecay(int* arr):" << endl;
    cout << "  - sizeof(arr) = " << sizeof(arr) << " bytes (Pointer size)" << endl;
}

int main() {
    cout << "=== ARRAYS AS PARAMETERS & POINTER DECAY ===" << endl << endl;

    int numbers[5]{10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    cout << "In main():" << endl;
    cout << "  - sizeof(numbers) = " << sizeof(numbers) << " bytes (Total array size)" << endl << endl;

    inspectDecay(numbers);

    cout << "\n--- Initial Array ---" << endl;
    printArray(numbers, size);

    cout << "\n--- Doubling values in-place ---" << endl;
    doubleValues(numbers, size);

    cout << "\n--- Array after modification ---" << endl;
    printArray(numbers, size);

    return 0;
}