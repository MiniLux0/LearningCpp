#include <iostream>
using namespace std;

int* maximoPtr(int *p, int n) {
    int* max= p;
    for (int i = 1; i < n; i++) {
        if(*max < *(p+i))
        max = (p+i);
    }
    return max;
}

int main() {
    int arr[] = {3, 7, 1, 9, 4};
    int n = 5;

    int *m = maximoPtr(arr, n);

    cout << "Max value: " << *m << endl;
    *m = 0;
    cout << "Array after modification: ";
    for (int i = 0; i < n; i++)
        cout << *(arr + i) << " ";
    cout << endl;

    return 0;
}