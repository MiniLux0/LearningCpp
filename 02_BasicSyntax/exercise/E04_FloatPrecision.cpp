/*
 * E04 — Float vs Double Precision
 * -------------------------------
 * Declare float and double with 1.0/3.0.
 * Print them with setprecision(20) to see the difference.
 *
 * Question: Which has more significant digits?
 * 
 * Answer : double has more significant digits than float
 */

 
#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    float fvalue = 1.0/3.0;
    double dvalue = 1.0/3.0;
    cout << fvalue << "\n";
    cout << dvalue << "\n";
    cout << fixed;
    cout << setprecision(20) << fvalue << "\n";
    cout << setprecision(20) << dvalue << "\n";

    return 0;
}
