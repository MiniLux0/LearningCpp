#include <iostream>
#include <string>
#include <cctype>

using namespace std;

// ============================================================================
// L30D — STRING PROCESSING ALGORITHMS & APPLICATIONS
// Stanford CS106B Chapter 3 (Sections 3.6 - 3.7)
// ============================================================================

// 1. Efficient O(N) Palindrome Verification with Frontier Indices
bool isPalindromeIterative(const string& str) {
    int low = 0;
    int high = static_cast<int>(str.length()) - 1;
    while (low < high) {
        if (str[low] != str[high]) return false;
        low++;
        high--;
    }
    return true;
}

// 2. Pig Latin Translation
bool isVowel(char ch) {
    ch = static_cast<char>(tolower(static_cast<unsigned char>(ch)));
    return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}

string wordToPigLatin(const string& word) {
    if (word.empty()) return "";
    
    if (isVowel(word[0])) {
        return word + "way";
    }
    
    size_t firstVowelIdx = string::npos;
    for (size_t i = 0; i < word.length(); i++) {
        if (isVowel(word[i])) {
            firstVowelIdx = i;
            break;
        }
    }
    
    if (firstVowelIdx == string::npos) {
        return word + "ay";
    }
    
    string prefix = word.substr(0, firstVowelIdx);
    string remainder = word.substr(firstVowelIdx);
    return remainder + prefix + "ay";
}

// 3. Caesar Cipher (Shift k)
string caesarCipher(const string& str, int shift) {
    string result = "";
    shift = (shift % 26 + 26) % 26; // Normalize shift to range [0, 25]
    
    for (char ch : str) {
        if (isupper(static_cast<unsigned char>(ch))) {
            result += static_cast<char>('A' + (ch - 'A' + shift) % 26);
        } else if (islower(static_cast<unsigned char>(ch))) {
            result += static_cast<char>('a' + (ch - 'a' + shift) % 26);
        } else {
            result += ch;
        }
    }
    return result;
}

int main() {
    cout << "=== STRING PROCESSING ALGORITHMS ===" << endl << endl;

    // Palindrome test
    string p1 = "racecar";
    string p2 = "cpp";
    cout << "Is \"" << p1 << "\" a palindrome? " << (isPalindromeIterative(p1) ? "YES" : "NO") << endl;
    cout << "Is \"" << p2 << "\" a palindrome? " << (isPalindromeIterative(p2) ? "YES" : "NO") << endl;

    // Pig Latin test
    cout << "\n--- Pig Latin Translation ---" << endl;
    cout << "apple -> " << wordToPigLatin("apple") << endl;
    cout << "trash -> " << wordToPigLatin("trash") << endl;

    // Caesar Cipher test
    cout << "\n--- Caesar Cipher ---" << endl;
    string secret = "Attack at Dawn!";
    string encrypted = caesarCipher(secret, 3);
    string decrypted = caesarCipher(encrypted, -3);
    cout << "Original:  " << secret << endl;
    cout << "Encrypted (+3): " << encrypted << endl;
    cout << "Decrypted (-3): " << decrypted << endl;

    return 0;
}
