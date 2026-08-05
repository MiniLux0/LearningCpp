#include <iostream>
#include <cassert>

using namespace std;

// E05 — Linear Search
int buscar(const int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i; // Returns index of first occurrence
        }
    }
    return -1; // Not found
}

int main() {
    int data[]{15, 42, 8, 23, 99};
    int size = sizeof(data) / sizeof(data[0]);

    int idxFound = buscar(data, size, 23);
    int idxNotFound = buscar(data, size, 100);

    cout << "Index of 23: " << idxFound << endl;
    cout << "Index of 100: " << idxNotFound << endl;

    assert(idxFound == 3);
    assert(idxNotFound == -1);

    return 0;
}
