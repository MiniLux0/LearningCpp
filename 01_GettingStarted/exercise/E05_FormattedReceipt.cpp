// ============================================================================
// E05 — Formatted Store Receipt Mini-Project Exercise
// ============================================================================
// Problem Statement:
// Prompt the user for an item name and price, then print a formatted receipt banner.
// ============================================================================

#include <iostream>
#include <string>

using namespace std;

int main() {
    string item_name;
    double item_price;

    cout << "Enter item name: ";
    cin >> item_name;

    cout << "Enter item price ($): ";
    cin >> item_price;

    cout << "\n----------------------------------------\n";
    cout << "          STORE PURCHASE RECEIPT        \n";
    cout << "----------------------------------------\n";
    cout << " Item     : " << item_name << "\n";
    cout << " Price    : $" << item_price << "\n";
    cout << " Status   : PAID IN FULL\n";
    cout << "----------------------------------------\n";

    return 0;
}
