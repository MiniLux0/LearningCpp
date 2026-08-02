#include <iostream>
using namespace std;

int main() {
    // char variables
    char letter = 'A';
    char numberChar = '7'; // character '7' (ASCII 55), not integer 7
    char letter2;

    cout << "ASCII value of (A): " << (int)letter << "\n";
    cout << "Number character: " << numberChar << " (ASCII: " << (int)numberChar << ")\n";
    cout << "Number (65) to ASCII character: " << (char)65 << "\n";
    cout << "Sizeof(char): " << sizeof(char) << " bytes\n\n";

    // Bool
    bool isStudent = true;
    bool isTeacher = false;

    cout << "Is student: " << isStudent << "\n";
    cout << "Is teacher: " << isTeacher << "\n\n";

    // ASCII arithmetic
    char nextLetter = letter + 1;
    cout << "Next letter is: " << nextLetter << "\n\n";

    cout << "Enter a character: ";
    cin >> letter2;
    cout << "ASCII value of entered letter: " << (int)letter2 << "\n";

    return 0;
}