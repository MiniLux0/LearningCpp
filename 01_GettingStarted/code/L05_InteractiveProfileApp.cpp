// ============================================================================
// L05 — Mini-Project: Interactive User Profile App
// ============================================================================
// Objective: Combine text printing, namespaces, and user input into a complete project!
// ============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
    // Banner Header
    cout << "========================================\n";
    cout << "    WELCOME TO C++ PROFILE GENERATOR    \n";
    cout << "========================================\n\n";

    // Variables to store user data
    string full_name;
    string favorite_subject;
    int lucky_number;

    // Collect user input
    cout << "1. Enter your name: ";
    cin >> full_name;

    cout << "2. Enter your favorite subject: ";
    cin >> favorite_subject;

    cout << "3. Enter your lucky number: ";
    cin >> lucky_number;

    // Output Formatted Summary Card
    cout << "\n----------------------------------------\n";
    cout << "          USER PROFILE CARD             \n";
    cout << "----------------------------------------\n";
    cout << " Name            : " << full_name << "\n";
    cout << " Favorite Topic  : " << favorite_subject << "\n";
    cout << " Lucky Number    : " << lucky_number << "\n";
    cout << " Status          : Ready to master C++!\n";
    cout << "----------------------------------------\n";

    return 0;
}