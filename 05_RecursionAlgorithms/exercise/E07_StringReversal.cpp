#include <iostream>
#include <string>
using namespace std;

// Exercise 7 — String Reversal (recursive, no loops)
// Big-O: Time O(n), Space O(n) — n recursive frames + n new strings built.
// Base case: empty string or single character is its own reverse.
// Recursive case: reverse(s) = reverse(s[1..end]) + s[0]

string reverseString(const string& s) {
    if (s.length() <= 1) return s;                     // base case
    return reverseString(s.substr(1)) + s[0];          // recursive case
}

// Bonus: in-place version using index parameters (avoids string copies)
void reverseInPlace(string& s, int left, int right) {
    if (left >= right) return;                         // base case
    swap(s[left], s[right]);
    reverseInPlace(s, left + 1, right - 1);
}

int main() {
    cout << "--- String Reversal (Recursive) ---" << endl;

    cout << "\n[reverseString — returns new string]" << endl;
    cout << "\"hello\"   → \"" << reverseString("hello")   << "\"" << endl;
    cout << "\"abcde\"   → \"" << reverseString("abcde")   << "\"" << endl;
    cout << "\"a\"       → \"" << reverseString("a")       << "\"" << endl;
    cout << "\"\"        → \"" << reverseString("")        << "\"" << endl;
    cout << "\"racecar\" → \"" << reverseString("racecar") << "\"" << endl;

    cout << "\n[reverseInPlace — modifies original]" << endl;
    string s1 = "recursion";
    reverseInPlace(s1, 0, static_cast<int>(s1.length()) - 1);
    cout << "\"recursion\" reversed in-place → \"" << s1 << "\"" << endl;

    string s2 = "ab";
    reverseInPlace(s2, 0, static_cast<int>(s2.length()) - 1);
    cout << "\"ab\" reversed in-place        → \"" << s2 << "\"" << endl;

    return 0;
}
