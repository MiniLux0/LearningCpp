#include <iostream>
using namespace std;

// Exercise 3 — Binary Search (recursive)
// Precondition: arr[] must be sorted in ascending order.
// Big-O: Time O(log n), Space O(log n) due to recursive call stack.
// Compare: linear search is O(n) time, O(1) space.

int binarySearch(const int arr[], int low, int high, int target) {
    if (low > high) return -1;          // base case: not found

    int mid = low + (high - low) / 2;  // avoids integer overflow vs (low+high)/2

    if (arr[mid] == target) return mid; // base case: found
    if (arr[mid] < target)
        return binarySearch(arr, mid + 1, high, target);   // search right half
    else
        return binarySearch(arr, low, mid - 1, target);    // search left half
}

// Wrapper — hides low/high from caller
int search(const int arr[], int size, int target) {
    return binarySearch(arr, 0, size - 1, target);
}

void printResult(int idx, int target) {
    if (idx == -1)
        cout << target << " → NOT FOUND" << endl;
    else
        cout << target << " → found at index " << idx << endl;
}

int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 45, 56, 72};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "--- Binary Search ---" << endl;
    cout << "Array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl << endl;

    printResult(search(arr, n, 23),  23);   // present — middle
    printResult(search(arr, n, 2),    2);   // present — first
    printResult(search(arr, n, 72),  72);   // present — last
    printResult(search(arr, n, 99),  99);   // absent
    printResult(search(arr, n, 1),    1);   // absent — below min

    return 0;
}
