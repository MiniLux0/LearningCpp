#include <iostream>
#include <utility>
#include <cassert>

using namespace std;

// E03 — In-Place Array Reversal
void invertir(int arr[], int size) {
    int low = 0;
    int high = size - 1;
    while (low < high) {
        swap(arr[low], arr[high]);
        low++;
        high--;
    }
}

int main() {
    int data[]{1, 2, 3, 4, 5};
    int size = sizeof(data) / sizeof(data[0]);

    invertir(data, size);

    cout << "Reversed array: [ ";
    for (int i = 0; i < size; i++) {
        cout << data[i] << " ";
    }
    cout << "]" << endl;

    assert(data[0] == 5 && data[4] == 1);

    return 0;
}
