#include <iostream>
#include <utility>  // std::swap
using namespace std;

// Exercise 5 — QuickSort
// Big-O: Time O(n log n) average, O(n^2) worst case (sorted input + last-element pivot).
// Space: O(log n) average (recursive call stack), O(n) worst case.
// Key insight: partition places pivot in its FINAL position, then recurse on both sides.

// Lomuto partition scheme — pivot = last element
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // choose last element as pivot
    int i     = low - 1;    // index of smaller element boundary

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);  // move smaller element to left side
        }
    }
    swap(arr[i + 1], arr[high]);   // place pivot in its correct position
    return i + 1;                  // return pivot's final index
}

void quickSort(int arr[], int low, int high) {
    if (low >= high) return;        // base case: 0 or 1 elements

    int pivotIdx = partition(arr, low, high);
    quickSort(arr, low, pivotIdx - 1);   // sort left of pivot
    quickSort(arr, pivotIdx + 1, high);  // sort right of pivot
}

void printArray(const int arr[], int n, const char* label) {
    cout << label << ": ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}

int main() {
    cout << "--- QuickSort ---" << endl;

    int arr1[] = {10, 7, 8, 9, 1, 5};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printArray(arr1, n1, "Before");
    quickSort(arr1, 0, n1 - 1);
    printArray(arr1, n1, "After ");

    cout << endl;

    // Worst case: already sorted array with last-element pivot → O(n^2) partitions
    int arr2[] = {1, 2, 3, 4, 5, 6};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printArray(arr2, n2, "Before (already sorted — worst case)");
    quickSort(arr2, 0, n2 - 1);
    printArray(arr2, n2, "After ");

    cout << endl;

    int arr3[] = {3};               // single element
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    printArray(arr3, n3, "Before");
    quickSort(arr3, 0, n3 - 1);
    printArray(arr3, n3, "After ");

    return 0;
}
