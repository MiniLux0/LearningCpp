#include <iostream>
#include <cassert>

using namespace std;

// E01 — Find Maximum Value of an Array
int maximo(const int arr[], int size) {
    assert(size > 0);
    int maxVal = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}

int main() {
    int data[]{3, 7, 2, 9, 5};
    int size = sizeof(data) / sizeof(data[0]);

    cout << "Maximum value: " << maximo(data, size) << endl;
    assert(maximo(data, size) == 9);

    return 0;
}
