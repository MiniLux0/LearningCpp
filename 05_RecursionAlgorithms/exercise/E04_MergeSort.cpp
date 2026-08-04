#include <iostream>
using namespace std;

// Exercise 4 — MergeSort
// Big-O: Time O(n log n) all cases, Space O(n) auxiliary array.
// Key insight: divide until single elements (always sorted),
// then merge pairs back together maintaining sorted order.

// Merge two sorted halves arr[low..mid] and arr[mid+1..high]
void merge(int arr[], int low, int mid, int high) {
    int leftSize  = mid - low + 1;
    int rightSize = high - mid;

    // Auxiliary arrays (temporary copies)
    int* left  = new int[leftSize];
    int* right = new int[rightSize];

    for (int i = 0; i < leftSize;  i++) left[i]  = arr[low + i];
    for (int j = 0; j < rightSize; j++) right[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = low;
    while (i < leftSize && j < rightSize) {
        if (left[i] <= right[j]) arr[k++] = left[i++];
        else                     arr[k++] = right[j++];
    }
    while (i < leftSize)  arr[k++] = left[i++];   // leftover left elements
    while (j < rightSize) arr[k++] = right[j++];  // leftover right elements

    delete[] left;
    delete[] right;
}

// Divide & Conquer — recursively split, then merge
void mergeSort(int arr[], int low, int high) {
    if (low >= high) return;            // base case: single element or empty

    int mid = low + (high - low) / 2;
    mergeSort(arr, low, mid);           // sort left half
    mergeSort(arr, mid + 1, high);      // sort right half
    merge(arr, low, mid, high);         // combine sorted halves
}

void printArray(const int arr[], int n, const char* label) {
    cout << label << ": ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}

int main() {
    cout << "--- MergeSort ---" << endl;

    int arr1[] = {38, 27, 43, 3, 9, 82, 10};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printArray(arr1, n1, "Before");
    mergeSort(arr1, 0, n1 - 1);
    printArray(arr1, n1, "After ");

    cout << endl;

    int arr2[] = {5, 1};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    printArray(arr2, n2, "Before");
    mergeSort(arr2, 0, n2 - 1);
    printArray(arr2, n2, "After ");

    cout << endl;

    int arr3[] = {42};                  // single element — already sorted
    int n3 = sizeof(arr3) / sizeof(arr3[0]);
    printArray(arr3, n3, "Before");
    mergeSort(arr3, 0, n3 - 1);
    printArray(arr3, n3, "After ");

    return 0;
}
