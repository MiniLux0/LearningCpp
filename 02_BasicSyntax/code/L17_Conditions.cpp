// ============================================================================
// L17 — Complex Logical Conditions & Truth Tables
// ============================================================================
// Objective: Master logical operators (&&, ||, !), short-circuit evaluation,
//            and boolean expression evaluation in C++.
// ============================================================================

#include <iostream>

using namespace std;

int main() {
    cout << "=== Logical Operators & Truth Tables ===\n\n";

    bool is_student = true;
    bool has_discount_code = false;
    int age = 22;

    // 1. Logical AND (&&): Both conditions must be true
    cout << "1. Logical AND (&&):\n";
    if (age >= 18 && is_student) {
        cout << "  Eligible for student discount (Adult & Student)\n";
    }

    // 2. Logical OR (||): At least one condition must be true
    cout << "\n2. Logical OR (||):\n";
    if (is_student || has_discount_code) {
        cout << "  Special price applied (Student OR Discount Code)\n";
    }

    // 3. Logical NOT (!): Inverts a boolean value
    cout << "\n3. Logical NOT (!):\n";
    if (!has_discount_code) {
        cout << "  No discount code provided.\n";
    }

    // 4. Short-Circuit Evaluation: Second condition is NOT evaluated if first is false (AND) / true (OR)
    int divisor = 0;
    cout << "\n4. Short-Circuit Evaluation Prevention (Divisor Check):\n";
    if (divisor != 0 && (100 / divisor > 5)) {
        cout << "  Division result calculated safely.\n";
    } else {
        cout << "  Division skipped safely (avoided divide-by-zero crash!).\n";
    }

    return 0;
}
