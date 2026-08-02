/*
 * E08 — Age Classifier
 * --------------------
 * Asks for a person's age and classifies it:
 *   0-12:   "Child"
 *   13-17:  "Adolescent"
 *   18-64:  "Adult"
 *   65+:    "Older Adult"
 *
 * Example:
 *   Input:  25
 *   Output: Adult
 */

#include <iostream>
using namespace std;

int main() {

    int age;
    cout << "Enter your age: ";
    cin >> age;

    if(age >= 65){
        cout << "Older Adult";
    } else if ( 18<=age  && age <= 64){
        cout << "Adult";
    } else if (13<= age && age <=17){
        cout << "Adolescent";
    }else{
        cout << "Child";
    }
    

    return 0;
}
