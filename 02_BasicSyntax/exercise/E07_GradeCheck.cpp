/*
 * E07 — Grade Check
 * -----------------
 * Asks for a student's grade (0-100).
 * Prints "Approved" if it is >= 60, "Disapproved" if it is < 60.
 *
 * Example:
 *   Input:  75
 *   Output: Approved
 */

#include <iostream>
using namespace std;

int main()
{

    double dValue;

    cout << "Enter your grade: ";
    cin >> dValue;

    if(dValue >= 60){
        cout << "Approved";
    } else{
        cout<< "Disapproved";
    }

    return 0;
}
