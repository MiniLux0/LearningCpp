#include <iostream>
#include <string>
using namespace std;

int main()
{
    int age;
    string name;
    cout << "Enter your name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Hello " << name << " you are " << age;

    return 0;
}