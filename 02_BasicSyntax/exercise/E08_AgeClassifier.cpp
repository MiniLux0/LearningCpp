/*
 * E08 — Age Classifier
 * --------------------
 * Pide la edad de una persona y clasificala:
 *   0-12:   "Nino"
 *   13-17:  "Adolescente"
 *   18-64:  "Adulto"
 *   65+:    "Adulto mayor"
 *
 * Ejemplo:
 *   Input:  25
 *   Output: Adulto
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
        cout << "adolescent";
    }else{
        cout << "Kid";
    }
    

    return 0;
}
