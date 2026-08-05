#include <iostream>
#include <cassert>

using namespace std;

// E02 — Calculate Average of Array Elements
double promedio(const int arr[], int size) {
    assert(size > 0);
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return static_cast<double>(sum) / size;
}

int main() {
    int data[]{10, 20, 30, 40};
    int size = sizeof(data) / sizeof(data[0]);

    cout << "Average: " << promedio(data, size) << endl;
    assert(promedio(data, size) == 25.0);

    return 0;
}
