// ============================================================================
// L04 — Interactive User Input (cin & cout)
// ============================================================================
// Objective: Learn how to ask the user for input and display it back.
// ============================================================================

#include <iostream>
#include <string>

// We bring standard tools into scope for cleaner beginner code
using namespace std;

int main() {
    // 1. Declare variables to store user data
    string user_name;
    int user_age;

    // 2. Prompt the user for their name
    cout << "Enter your first name: ";
    cin >> user_name; // Reads a single word from the keyboard

    // 3. Prompt the user for their age
    cout << "Enter your age: ";
    cin >> user_age; // Reads an integer number from the keyboard

    // 4. Display a personalized response using chained outputs
    cout << "\n--- Welcome Message ---\n";
    cout << "Hello, " << user_name << "! You are " << user_age << " years old.\n";
    cout << "Great job writing your first interactive C++ program!\n";

    return 0;
}