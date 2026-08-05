#include <iostream>
#include <cassert>

using namespace std;

// E04 — Increment All Array Elements In-Place
void incrementarTodo(int arr[], int size, int delta) {
    for (int i = 0; i < size; i++) {
        arr[i] += delta;
    }
}

int main() {
    int data[]{10, 20, 30};
    int size = sizeof(data) / sizeof(data[0]);

    incrementarTodo(data, size, 5);

    cout << "Incremented array: [ ";
    for (int i = 0; i < size; i++) {
        cout << data[i] << " ";
    }
    cout << "]" << endl;

    assert(data[0] == 15 && data[2] == 35);

    return 0;
}